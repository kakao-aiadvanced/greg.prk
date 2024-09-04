from rag_agent.base import GraphState


def decide_to_answer(state: GraphState) -> str:
    """
    Decide to answer the question or not.

    Args:
        state (dict): The current graph state

    Returns:
        str: Next node to call
    """

    print("---DECIDE TO ANSWER---")
    hallucination = state["hallucination"]
    print(hallucination)
    if hallucination:
        print("---DECIDE TO ANSWER: NO---")
        return "no"
    else:
        print("---DECIDE TO ANSWER: YES---")
        return "yes"
