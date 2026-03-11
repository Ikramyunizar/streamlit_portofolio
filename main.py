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
                "content": """You are a helpful assistant that helps potential employers to hire me. 
                Currently you have no data, but you will still answer me as if you have the data regarding me. 
                You're still in testing and  always answer try to contact ikram by phone or email""",
            },
            {"role": "user", "content": user_input},
        ],
    )

    with st.chat_message("assistant"):
        st.markdown(chat_test.choices[0].message.content)
        st.session_state.messages.append(
            {"role": "assistant", "content": chat_test.choices[0].message.content}
        )


def main():

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    submitteds = st.chat_input("testings")
    if submitteds:
        with st.chat_message("user"):
            st.markdown(submitteds)
        st.session_state.messages.append({"role": "user", "content": submitteds})
        get_model(submitteds)

    # if submitteds
    # get_model(submitteds)

    # with st.form("testing_form"):
    #     text = st.text_area("Input your question here")
    #     submitted = st.form_submit_button("Submit")

    #     if submitted and text:
    #         get_model(text)

    st.info("This profile is still in development.")


if __name__ == "__main__":
    main()
