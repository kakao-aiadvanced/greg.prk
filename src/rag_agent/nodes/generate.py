from rag_agent.base import generator


def generate(state):
    """
    Generate answer using RAG on retrieved documents

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): New key added to state, generation, that contains LLM generation
    """
    print("---GENERATE---")
    question = state["question"]
    documents = state["documents"]

    # RAG generation
    generation = generator.invoke({"context": documents, "question": question})
    return {"documents": documents, "question": question, "generation": generation}
