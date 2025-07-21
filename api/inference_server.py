# agentiq/api/inference_server.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

app = FastAPI()

# Load your OpenAI key from env
os.environ["OPENAI_API_KEY"] = "sk-..."

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
prompt = PromptTemplate(
            input_variables=["question"],
                template="Answer the question: {question}"
                )
chain = LLMChain(llm=llm, prompt=prompt)

class Query(BaseModel):
        question: str

        @app.post("/query")
        async def ask_question(query: Query):
                response = chain.run(query.question)
                    return {"answer": response}
