import os
import sys
from pathlib import Path
import zipfile
import logging
import requests


from langchain.schema.runnable.config import RunnableConfig
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()
from lets_talk.config import VECTOR_STORAGE_PATH

VECTOR_STORE_DOWNLOAD_URL = os.getenv("VECTOR_STORE_DOWNLOAD_URL")

def download_from_dropbox(direct_download_url):
    """Download a file from Dropbox with proper handling of the download link."""
    try:
                    

        
        logger.info("Downloading vector store from %s...", direct_download_url)
        response = requests.get(direct_download_url, stream=True)
        response.raise_for_status()
        
        # Save to temp file
        with open("/tmp/vector_store.zip", "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        
        logger.info("Download completed successfully")
        return True
    except Exception as e:
        logger.error("Failed to download from Dropbox: %s", str(e))
        return False
if Path(VECTOR_STORAGE_PATH).exists():
    logger.info("Vector store already exists at %s", VECTOR_STORAGE_PATH)
elif VECTOR_STORE_DOWNLOAD_URL:
    logger.info("Starting vector store download process")
    if download_from_dropbox(VECTOR_STORE_DOWNLOAD_URL):
        try:
            # Verify the zip file
            with zipfile.ZipFile("/tmp/vector_store.zip", "r") as zip_ref:
                logger.info("Extracting vector store files...")
                zip_ref.extractall(VECTOR_STORAGE_PATH)
                logger.info("Vector store extraction completed")
        except zipfile.BadZipFile:
            logger.error("Downloaded file is not a valid zip file")
            sys.exit(1)
        except Exception as e:
            logger.error("Failed to extract vector store: %s", str(e))
            sys.exit(1)
    else:
        logger.error("Failed to download vector store")
        sys.exit(1)
else:
    # Check if the vector store exists
    logger.info("Checking vector store...")
    if not Path(VECTOR_STORAGE_PATH).exists():
        logger.error("Vector store not found at %s. Please create it first.", VECTOR_STORAGE_PATH)
        sys.exit(1)

import chainlit as cl


from prompt import prompt
from lets_talk.agent_v2 import create_agent
d365stuff_agent = create_agent(prompt=prompt)
  
@cl.on_chat_start
async def setup_chain():
   
    # Store the chain in user session
    cl.user_session.set("agent", d365stuff_agent)
    

    # Set a loading message
    welcome_message = "Welcome to [D365 Stuff](https://www.d365stuff.co) Chat! How can I help you today?"
    msg = cl.Message(content=welcome_message, author="System")
    await msg.send()


    

@cl.on_message
async def on_message(message: cl.Message):
    """
    Handler for user messages. Processes the query through the research agent
    and streams the response back to the user.
    
    Args:
        message: The user's message
    """
    agent_executor = cl.user_session.get("agent")
    
    # Check if agent_executor exists
    if not agent_executor:
        await cl.Message(content="Agent not initialized properly. Please refresh the page.").send()
        return
        
    # Create Chainlit message for streaming
    # msg = cl.Message(content="")

    final_answer = cl.Message(content="")
    configurable = {"thread_id": cl.context.session.id}
    cb = cl.LangchainCallbackHandler()
    runnable_config= RunnableConfig(callbacks=[cb], configurable=configurable)

    async for response_msg, metadata in agent_executor.astream({"messages": [HumanMessage(content=message.content)]}, stream_mode="messages", config=runnable_config):
        if (
            response_msg.content
            and not isinstance(response_msg, HumanMessage)
            and metadata["langgraph_node"] == "agent"
        ):
            await final_answer.stream_token(response_msg.content)

    await final_answer.send()
    
   
  