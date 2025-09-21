import streamlit as st
from controllers.usuarios_controller import criar_usuario


#FORMULARIO DE CRIAÇÃO DE NOVO USUARIO

def show():

    st.title("Criar novo usuário")
    novo_usuario = st.text_input("Novo nome de usuário")
    nova_senha = st.text_input("Nova senha", type="password")

    if st.button("Criar usuário"):
            if criar_usuario(novo_usuario, nova_senha):
                    st.success(f"Usuário '{novo_usuario}' criado com sucesso!")
            else:
                    st.error("Erro: nome de usuário já existe.")
