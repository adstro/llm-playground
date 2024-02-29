import streamlit as st

from model import Role

import logging

from llms import openai_chat_model
from langchain_core.output_parsers import StrOutputParser

logging.basicConfig(level=logging.DEBUG)

st.title("LLM Playground")

st.sidebar.selectbox("Select a Role",
                     (Role.USER, Role.SYSTEM),
                     key="role",
                     on_change=lambda: logging.debug(f"role changed to {st.session_state.role}"))

st.sidebar.button("Clear Chat",
                  on_click=lambda: st.session_state.messages.clear())

st.session_state.chain = openai_chat_model | StrOutputParser()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input(st.session_state.role):
    role: Role = st.session_state.role

    with st.chat_message(name=role):
        st.markdown(prompt)

    st.session_state.messages.append({"role": role, "content": prompt})

    with st.chat_message(name=Role.ASSISTANT):
        response = st.write(st.session_state.chain.invoke(prompt))

    st.session_state.messages.append({"role": Role.ASSISTANT, "content": response})
