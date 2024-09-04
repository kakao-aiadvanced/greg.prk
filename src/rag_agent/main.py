import sys
from pprint import pprint

from dotenv import load_dotenv

from rag_agent.workflow import workflow


def main() -> None:
    app = workflow.compile()
    question = sys.argv[1]
    inputs = {"question": question}
    for output in app.stream(inputs):
        for key, value in output.items():
            pprint(f"Finished running: {key}:")
    pprint(value["generation"])

if __name__ == "__main__":
    main(*sys.argv[1:])
