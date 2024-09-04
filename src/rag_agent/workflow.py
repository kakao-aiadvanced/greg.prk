from langgraph.graph import END, StateGraph

from rag_agent.base import GraphState
from rag_agent.edges import *
from rag_agent.nodes import *

workflow = StateGraph(GraphState)

# Define the nodes
workflow.add_node("websearch", web_search)  # web search
workflow.add_node("retrieve", retrieve)  # retrieve
workflow.add_node("check_hallucination", check_hallucination)
workflow.add_node("check_relevance", check_relevance)
workflow.add_node("generate", generate)  # generatae

workflow.set_entry_point("retrieve")
workflow.add_edge("retrieve", "check_relevance")
workflow.add_conditional_edges(
    "check_relevance",
    decide_to_generate,
    {
        "web_search": "websearch",
        "generate": "generate",
    },
)
workflow.add_edge("websearch", "check_relevance")
workflow.add_edge("generate", "check_hallucination")
workflow.add_conditional_edges(
    "check_hallucination",
    decide_to_answer,
    {
        "yes": END,
        "no": "generate"
    },
)
