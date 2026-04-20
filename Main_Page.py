import dotenv
import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq
import json

load_dotenv()


def get_model(user_input):
    GROQ_KEY = os.getenv("GROQ_KEY")
    model = Groq(api_key=GROQ_KEY)
    with open('knowledge/cv_data.json') as f:
        cv_data = json.load(f)

    chat_test = model.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": f"""You are an CV profile assistant. 
                Your primary role is to answer user questions  using the information provided in cv_data. 
                If the user's question is not directly related to this topic or cannot be answered using the provided information, 
                politely add that your info might not complete, no need to inform you have the profile in the backend
                if there are no info about it, guide them to contact me through my profile
                data is as follows {cv_data}""",
                
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


    github = 'https://github.com/Ikramyunizar'
    with st.sidebar:
        st.subheader(":small[Contacts :]")
        st.markdown(":small[✉️ ikramyunizar@gmail.com]")
        st.markdown(":small[[My Github](%s)]" % github )



    st.header("Chat with my Ikram AI!")
    

    if "messages" not in st.session_state:
        st.session_state.messages = [{"role" : "assistant", "content" : "Ask Me Anything about Ikram!"}]

    for message in st.session_state.messages:
        
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
     

        # st.session_state.messages.append(
        #     {"role": "assistant", "content": "}
        # )
    
    submitteds = st.chat_input("Ask me about Ikram!")
    
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



if __name__ == "__main__":
    main()
