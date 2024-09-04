from rag_agent.base import GraphState, relevance_grader


def check_relevance(state: GraphState) -> GraphState:
    """
    Check relevance of answer.

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): New key added to state, relevance, that contains binary decision for relevance
    """

    print("---CHECK RELEVANCE---")
    question = state["question"]
    documents = state["documents"]
    scores = [
        relevance_grader.invoke({"question": question, "document": document})["score"]
        for document in documents
    ]
    print(scores)
    relevance = any(score == "relevant" or score == 1 for score in scores)

    return {"documents": documents, "question": question, "relevance": relevance}
