import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import(
    AIMessage,
    HumanMessage,
    SystemMessage
)

# App UI
st.set_page_config(page_title="ChatModelApp ", page_icon = ":robot:")
st.header("Hey , I am your Assistnat")

if "sessionMessages" not in st.session_state:
    st.session_state.sessionMessages=[
        SystemMessage(content="You are helpful assistant.")
        
    ]

def load_answer(question):
    st.session_state.sessionMessages.append(HumanMessage(content=question))
    assistant_answer = chat(st.session_state.sessionMessages)
    st.session_state.sessionMessages.append(AIMessage(content=assistant_answer.content))
    return assistant_answer.content


def get_text():
    input_text = st.text_input("you", key=input)
    return input_text

chat = ChatOpenAI(temperature=0)

user_input = get_text()

submit = st.button('Generate')
if submit:
    response = load_answer(user_input)
    st.subheader("Answer : ")
    st.write(response,key=1)

    