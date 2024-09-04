from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate

from rag_agent.base.openai import llm

system = """You are a grader assessing relevance of a retrieved document to a user question.
If the document contains keywords related to the user question,
grade it as 'relevant'. Otherwise, grade it as 'irrelevant'.
Provide the binary score as a JSON with a single key 'score' and no preamble or explanation."""

prompt = ChatPromptTemplate.from_messages(
    [
         ("system", system),
         ("human", "question: {question}\n\n document: {document} ")
    ]
)

relevance_grader = prompt | llm | JsonOutputParser()
