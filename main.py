import dotenv
import streamlit as st
import os 
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
from groq import Groq
load_dotenv()

def get_model(user_input):
    GROQ_KEY = os.getenv("GROQ_KEY")
    model = Groq(api_key=GROQ_KEY)
    
    chat_test = model.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. Answer based on my CV data."
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )
    

    
    
    st.info(chat_test.choices[0].message.content)
    # print(chat_test)

def main():
    
    with st.sidebar:
        st.page_link("pages/projects.py", label="Projects")
        st.text("Projects")
        st.text("Companies")
        
    st.text("Testing 1")
    
    with st.form("testing_form"):
        text = st.text_area("Input your question here") 
        submitted = st.form_submit_button("Submit")
        
        if submitted and text:
            get_model(text)
    
    st.info("This profile is still in development.")

if __name__ == "__main__":
    main()