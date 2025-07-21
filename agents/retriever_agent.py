
from langchain.chains import RetrievalQA
from agentiq.vectorstore.index_pinecone import vectorstore
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-3.5-turbo")
retriever_chain = RetrievalQA.from_chain_type(
            llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever()
            )

def answer_with_context(query):
        return retriever_chain.run(query)
