from pymongo import MongoClient
import streamlit as st

def get_database():
    #CONNECTION_STRING = 'mongodb+srv://elmetwalleyhammad:uy5ZxY0sFvm6lZ78@cluster0.zupkc.mongodb.net/'
    CONNECTION_STRING = st.secrets[MONGODB][MONGODB_CONNECTION_STRING]
    
    if not CONNECTION_STRING:
        raise ValueError("No MongoDB connection string found in environment variables.")
    
    client = MongoClient(CONNECTION_STRING)
    db = client['legalDocsDB']

    return db

def fetch_documents():
    db = get_database()
    collection = db['legal_pdfs']
    docs = list(collection.find({}, {"pdf_text": 1, "sub_link": 1, "title": 1, "sub_title": 1}))
    
    return docs
