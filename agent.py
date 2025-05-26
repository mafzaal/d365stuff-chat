import os
from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool
from langchain_community.tools.requests.tool import RequestsGetTool
from langchain_community.utilities.requests import TextRequestsWrapper
from langchain.chat_models import init_chat_model
import lets_talk.rag as rag
from lets_talk.utils import format_docs
from lets_talk.tools import RSSFeedTool,get_current_datetime
from lets_talk.config import LLM_MODEL,LLM_TEMPERATURE

@tool 
def retrive_documents(query: str) -> str:
    """Retrieve relevant documents from the knowledge base to answer user questions.
    
    Use this tool when you need to search for specific information, facts, or content
    that may be in the document collection. Provide a clear search query related to
    what information you need to find.
    
    Args:
        query: The search query to find relevant documents
        
    Returns:
        Formatted text containing the retrieved document content
    """
    docs = rag.retriever.invoke(query) # type: ignore
    return format_docs(docs)



requests_tool = RequestsGetTool(
    requests_wrapper=TextRequestsWrapper(headers={}),
    allow_dangerous_requests=True,
    description="Use this tool to make HTTP GET requests to retrieve information from the web. Provide a valid URL to fetch data.",
)

from promp import prompt
RSS_URL = os.getenv("RSS_URL")

tools =[RSSFeedTool(rss_url=RSS_URL), get_current_datetime,retrive_documents,requests_tool]

model_name = LLM_MODEL
temperature = LLM_TEMPERATURE
model = init_chat_model(model_name, temperature=temperature)

agent = create_react_agent(
    model=model,
    tools=tools,
    prompt=prompt,
    version="v2",
)
