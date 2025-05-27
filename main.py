from io import BytesIO, StringIO
import os
import requests
import html2text
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import xml.etree.ElementTree as ET
from datetime import datetime
from markitdown import MarkItDown
import logging
import hashlib
import json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('d365stuff_downloader.log'),
        logging.StreamHandler()
    ]
)

def create_posts_directory():
    """Create posts directory if it doesn't exist."""
    directories = ['posts', 'posts_markitdown', 'html_pages']
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            logging.info(f"Created directory: {directory}")

def get_file_hash(content):
    """Generate a hash of the content for comparison."""
    return hashlib.md5(content.encode('utf-8')).hexdigest()

def download_page(url):
    """Download a webpage and return its content."""
    filename = get_filename_from_url(url)
    html_path = os.path.join('html_pages', f"{filename}.html")
    
    # Check if HTML file already exists
    if os.path.exists(html_path):
        logging.info(f"HTML file already exists for {url}, reading from disk")
        with open(html_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    try:
        logging.info(f"Downloading page: {url}")
        response = requests.get(url)
        response.raise_for_status()
        content = response.text
        
        # Save HTML content
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)
        logging.info(f"Saved HTML content to: {html_path}")
        
        return content
    except requests.RequestException as e:
        logging.error(f"Error downloading {url}: {e}")
        return None

def extract_main_content(html_content):
    """Extract the main content from HTML using BeautifulSoup."""
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find the main article content
    article = soup.find('article')
    if article:
        return str(article)
    return html_content

def convert_to_markdown_html2text(html_content):
    """Convert HTML content to markdown using html2text."""
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.ignore_emphasis = False
    return h.handle(html_content)

def convert_to_markdown_markitdown(html_content):
    """Convert HTML content to markdown using MarkItDown."""
    md = MarkItDown()
    # convert html_content to BytesIO
    html_content_io = BytesIO(html_content.encode('utf-8'))
    result = md.convert(html_content_io)
    
    return result.markdown

def get_filename_from_url(url):
    """Extract filename from URL."""
    parsed = urlparse(url)
    path = parsed.path.strip('/')
    # Remove any trailing slashes and get the last part
    filename = path.split('/')[-1]
    # Remove any query parameters
    filename = filename.split('?')[0]
    # Remove any special characters and replace spaces with hyphens
    filename = ''.join(c for c in filename if c.isalnum() or c in ('-', '_', '.'))
    # Ensure filename is not too long (max 50 chars)
    #if len(filename) > 50:
    #    filename = filename[:50]
    return filename

def extract_json_ld_metadata(html_content):
    """Extract metadata from JSON-LD script tag."""
    soup = BeautifulSoup(html_content, 'html.parser')
    script_tag = soup.find('script', {'type': 'application/ld+json'})
    
    if not script_tag:
        logging.warning("No JSON-LD metadata found in the page")
        return None
    
    try:
        metadata = json.loads(script_tag.string)
        return metadata
    except json.JSONDecodeError as e:
        logging.error(f"Error parsing JSON-LD metadata: {e}")
        return None

def create_frontmatter(metadata):
    """Create markdown frontmatter from metadata."""
    if not metadata:
        return ""
    
    frontmatter = "---\n"
    
    # Add basic metadata
    if 'headline' in metadata:
        frontmatter += f"title: {metadata['headline']}\n"
    if 'datePublished' in metadata:
        frontmatter += f"date: {metadata['datePublished']}\n"
    if 'dateModified' in metadata:
        frontmatter += f"lastmod: {metadata['dateModified']}\n"
    if 'description' in metadata:
        frontmatter += f"description: {metadata['description']}\n"
    if 'keywords' in metadata:
        frontmatter += f"tags: {metadata['keywords']}\n"
    
    # Add author information
    if 'author' in metadata:
        author = metadata['author']
        if isinstance(author, dict):
            frontmatter += f"author: {author.get('name', '')}\n"
            if 'url' in author:
                frontmatter += f"author_url: {author['url']}\n"
    
    # Add publisher information
    if 'publisher' in metadata:
        publisher = metadata['publisher']
        if isinstance(publisher, dict):
            frontmatter += f"publisher: {publisher.get('name', '')}\n"
            if 'url' in publisher:
                frontmatter += f"publisher_url: {publisher['url']}\n"
    
    frontmatter += "---\n\n"
    return frontmatter

def save_markdown(content, directory, filename, metadata=None):
    """Save markdown content to a file with frontmatter."""
    if not filename.endswith('.md'):
        filename += '.md'
    output_path = os.path.join(directory, filename)
    
    # Add frontmatter if metadata is available
    if metadata:
        frontmatter = create_frontmatter(metadata)
        content = frontmatter + content
    
    # Check if file exists and compare content
    if os.path.exists(output_path):
        with open(output_path, 'r', encoding='utf-8') as f:
            existing_content = f.read()
        if get_file_hash(existing_content) == get_file_hash(content):
            logging.info(f"Content unchanged for {output_path}, skipping save")
            return
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    logging.info(f"Saved to: {output_path}")

def process_sitemap(sitemap_url):
    """Process the sitemap and download all pages."""
    try:
        logging.info(f"Processing sitemap: {sitemap_url}")
        response = requests.get(sitemap_url)
        response.raise_for_status()
        
        # Parse XML
        root = ET.fromstring(response.content)
        
        # Define namespace
        ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        
        # Create posts directories
        create_posts_directory()
        
        # Process each URL in the sitemap
        for url in root.findall('.//ns:url/ns:loc', ns):
            page_url = url.text
            logging.info(f"Processing: {page_url}")
            
            # Download page
            html_content = download_page(page_url)
            if html_content:
                # Extract metadata
                metadata = extract_json_ld_metadata(html_content)
                
                # Extract main content
                main_content = extract_main_content(html_content)
                
                # Generate filename
                filename = get_filename_from_url(page_url)
                
                # Save both versions with metadata
                try:
                    markdown_content_html2text = convert_to_markdown_html2text(main_content)
                    save_markdown(markdown_content_html2text, 'posts', filename, metadata)
                except Exception as e:
                    logging.error(f"Error saving HTML2Text markdown: {e}", exc_info=True)
                try:
                    markdown_content_markitdown = convert_to_markdown_markitdown(main_content)
                    save_markdown(markdown_content_markitdown, 'posts_markitdown', filename, metadata)
                except Exception as e:
                    logging.error(f"Error saving MarkItDown markdown: {e}", exc_info=True)
                
    except Exception as e:
        logging.error(f"Error processing sitemap: {e}", exc_info=True)

def main():
    sitemap_url = "https://www.d365stuff.co/sitemap-posts.xml"
    logging.info("Starting download process...")
    process_sitemap(sitemap_url)
    logging.info("Download process completed!")

if __name__ == "__main__":
    main()


    
    
    
    
    
