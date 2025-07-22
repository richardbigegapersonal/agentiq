# agentiq/api/inference_server.py

from fastapi import FastAPI
from pydantic import BaseModel
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key (do not hardcode!)
openai_key = os.getenv("OPENAI_API_KEY")
if not openai_key:
    raise ValueError("OPENAI_API_KEY not set in environment.")

app = FastAPI()

# Initialize LangChain LLM
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7, openai_api_key=openai_key)

# Simple prompt chain
prompt = PromptTemplate(
    input_variables=["question"],
    template="Answer the question: {question}"
)
chain = LLMChain(llm=llm, prompt=prompt)

class Query(BaseModel):
    question: str

@traceable(name="AgentIQ Query Trace")
@app.post("/query")
async def ask_question(query: Query):
    response = chain.run(query.question)
    return {"answer": response}
