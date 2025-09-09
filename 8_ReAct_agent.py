from typing import Annotated, Sequence, TypedDict
from dotenv import load_dotenv
from langchain_core.messages import BaseMessage # The foundational class for all message types in LangGraph
from langchain_core.messages import ToolMessage # 
from langchain_core.messages import SystemMessage
from langchain_openai import tools
from langgraph.graph.message import add_messages
from langgraph.graph.message import StateGraph
from langgraph.prebuilt import ToolNode

load_dotenv()

# Annotated - provides additional context without affecting the type itself
# email = Annotated[str, "THis is to be valid email id"]
# print('email:', email.__metadata__)

# Sequence - To automatically handle the state updates for sequences such as by adding new messages a chat history

