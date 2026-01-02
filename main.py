import streamlit as st
import os
from openai import OpenAI


# CONFIGURAÇÃO DA API

# A chave deve estar na variável de ambiente OPENAI_API_KEY
cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# INTERFACE

st.title("💬 ChatBot com IA")


# MEMÓRIA DO CHAT (SESSION STATE)

if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []


# EXIBIR HISTÓRICO

for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)


# INPUT DO USUÁRIO

mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")

if mensagem_usuario:
    # adiciona mensagem do usuário
    st.chat_message("user").write(mensagem_usuario)
    st.session_state["lista_mensagens"].append({
        "role": "user",
        "content": mensagem_usuario
    })


    # RESPOSTA DA IA
   
    resposta = cliente.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state["lista_mensagens"]
    )

    resposta_ia = resposta.choices[0].message.content

    # exibe resposta da IA
    st.chat_message("assistant").write(resposta_ia)
    st.session_state["lista_mensagens"].append({
        "role": "assistant",
        "content": resposta_ia
    })
