from rag_agent.base import GraphState, hallucination_grader


def check_hallucination(state: GraphState) -> GraphState:
    """
    Check hallucination of answer.

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): New key added to state, hallucination, that contains binary decision for hallucination
    """

    print("---CHECK HALLUCINATION---")
    documents = state["documents"]
    generation = state["generation"]
    hallucination = hallucination_grader.invoke({"documents": documents, "generation": generation})["score"] == "no"

    return {"documents": documents, "question": state["question"], "generation": generation, "hallucination": hallucination}
