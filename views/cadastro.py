import streamlit as st
from controllers.estudante_controller import adicionar_estudante

def show():
    st.title("📚 Cadastro de Estudantes")
    
    with st.form("cadastro_form"):
        nome = st.text_input("Nome")
        idade = st.text_input("Idade")
        nota1 = st.text_input("1º Nota")
        nota2 = st.text_input("2º Nota")
        submitted = st.form_submit_button("Cadastrar")
        

        if submitted:
            adicionar_estudante(nome, idade, nota1, nota2)
            st.success("✅ Estudante cadastrado com sucesso!")
