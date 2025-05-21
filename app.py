import streamlit as st
from langchain_community.utilities import SQLDatabase
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import langchain, os

from dotenv import load_dotenv
load_dotenv()

langchain.debug=True

# MySQL URI
mysql_uri = os.getenv("MYSQL_URI")


# Creating SQLDatabase instance
db = SQLDatabase.from_uri(mysql_uri)

# Ensure db is an instance of SQLDatabase
if not isinstance(db, SQLDatabase):
    raise TypeError(f"Expected db to be an instance of SQLDatabase, got {type(db)}")

def get_schema(db):
    schema = db.get_table_info()
    return schema

# Template for generating SQL query
template = """Based on the table schema below, write a SQL query that would answer the user's question:
{schema}
Question: {question}
SQL Query:"""
prompt = ChatPromptTemplate.from_template(template)

llm = AzureChatOpenAI(
    deployment_name=os.getenv("AZURE_DEPLOYMENT_NAME"),
    model_name=os.getenv("AZURE_MODEL_NAME"),
    azure_endpoint=os.getenv("AZURE_ENDPOINT"),
    openai_api_version=os.getenv("AZURE_API_VERSION"),
    openai_api_key=os.getenv("AZURE_API_KEY"),
    temperature=0
)

# Runnable for generating SQL query
sql_chain = (
    RunnablePassthrough.assign(schema=lambda _: get_schema(db))
    | prompt
    | llm.bind(stop=["\nSQLResult:"])
    | StrOutputParser()
)

# Template for generating natural language response
response_template = """Based on the table schema below, question, SQL query, and SQL response, write a natural language response:
{schema}
Your response should be concise, relevant, and directly answer the question. Do not include SQL query details or technical metadata.

Question: {question}
SQL Query: {query}
SQL Response: {response}

Your final response should clearly state the answer based on the SQL query results.
"""
prompt_response = ChatPromptTemplate.from_template(response_template)

def run_query(query):
    return db.run(query)

# Runnable for generating natural language response
full_chain = (
    RunnablePassthrough.assign(query=sql_chain).assign(
        schema=lambda _: get_schema(db),
        response=lambda vars: run_query(vars["query"]),
    )
    | prompt_response
    | llm
)

# Streamlit UI
st.title('SQL Chatbot')

user_question = st.text_input('Ask a question about the database')

if st.button('Get Answer'):
    if user_question:
        response = full_chain.invoke({"question": user_question})
        st.write(response.content)  # Displaying the content attribute of AIMessage
    else:
        st.warning('Please enter a question')