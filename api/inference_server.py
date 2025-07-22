from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
from langsmith import traceable
import os
import logging

load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")
if not openai_key:
    raise ValueError("OPENAI_API_KEY not set in environment.")

app = FastAPI()

# Set up static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Chain setup
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7, openai_api_key=openai_key)
prompt = PromptTemplate(input_variables=["question"], template="Answer the question: {question}")
chain = LLMChain(llm=llm, prompt=prompt)

@traceable(name="AgentIQ Query Trace")
@app.post("/", response_class=HTMLResponse)
async def get_answer(request: Request, question: str = Form(...)):
    try:
        response = chain.run(question)
        return templates.TemplateResponse("index.html", {
            "request": request,
            "answer": response
        })
    except Exception as e:
        logging.exception("❌ Error while processing the question")
        return templates.TemplateResponse("index.html", {
            "request": request,
            "answer": f"⚠️ An internal error occurred: {str(e)}"
        })

@app.get("/", response_class=HTMLResponse)
async def form_get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
