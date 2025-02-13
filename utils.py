from langchain_community.utilities import SQLDatabase
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_experimental.sql.base import SQLDatabaseChain
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.utilities import SQLDatabase
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

import configparser
import os

def read_properties_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError("Config file '{file_path}' not found.")
    config = configparser.ConfigParser()
    config.read(file_path)
    
    db_path = config['DEFAULT']['db_path']
    gemini_api_key = config['DEFAULT']['gemini_api_key']
    
    return db_path, gemini_api_key

def get_property():
    file_path = 'config.properties'
    try:
        db_path, gemini_api_key = read_properties_file(file_path)
        print("Database path:", db_path)
        print("Gemini API Key", gemini_api_key)
        return db_path, gemini_api_key
    except FileNotFoundError as e:
        print(e)
        raise e
    
def get_llm(gemini_api_key):
    llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=gemini_api_key,convert_system_message_to_human=True, temperature=0.0)
    return llm

def db_connection(db_path):
    db = SQLDatabase.from_uri(f"sqlite:///{db_path}")
    print(db.dialect)
    print(db.get_usable_table_names())
    resp = db.run("SELECT * FROM Employee LIMIT 10;")
    print(resp)
    return db

def create_conversational_chain():
    try:
        db, gemini_api_key = get_property()
        llm = get_llm(gemini_api_key)
        db = db_connection(db)

        sql_prompt_template = """
        Only use the following tables:
        {table_info}
        Question: {input}

        Given an input question, first create a syntactically correct
        {dialect} query to run.
        
        Relevant pieces of previous conversation:
        {history}

        (You do not need to use these pieces of information if not relevant)
        Dont include ```, ```sql and \n in the output.
        """
        
        prompt = PromptTemplate(
                input_variables=["input", "table_info", "dialect", "history"],
                template=sql_prompt_template,
            )
        memory = ConversationBufferMemory(memory_key="history")
        db_chain = SQLDatabaseChain.from_llm(
                llm, db, memory=memory, prompt=prompt, return_direct=True,  verbose=True
            )

        output_parser = StrOutputParser()
        chain = llm | output_parser
    except Exception as e:
        raise e
    return  db_chain, chain