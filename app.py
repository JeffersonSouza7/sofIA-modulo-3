import streamlit as st
from utils.db import init_db
from controllers.usuarios_controller import autenticar_usuario
from views import cadastro, conteudo, dashboard, documentos, matriculados, novosUsuarios, gerenciarUsuarios


# Inicializa banco
init_db()

#TELA DE LOGIN

def login():
    st.title("Login")
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if autenticar_usuario(username, password):
            st.session_state["logado"] = True
            st.session_state["usuario"] = username
            st.success("Login bem-sucedido!")
            st.rerun()
        else:
            st.error("Usuário ou senha inválidos.")

# Verifica se o usuário está logado

if "logado" not in st.session_state:    #Verifica se já existe uma variável chamada logado na sessão
    st.session_state["logado"] = False  #Se não existir, define que o usuário não está logado

if not st.session_state["logado"]:      #Se o usuário não está logado
    login()                             #mostra a tela de login
    st.stop()                           #impede o resto do código de rodar até que o login seja feito

# OPÇÕES DO USUARIO ADMIN
if st.session_state["usuario"] == "admin":

        # "FRONT-END" - Sidebar
        st.title("😺 MiIA")
        st.subheader(f"Bem vindo {st.session_state["usuario"]}")

        # Menu
        st.sidebar.title("📌 Menu")
        opcao = st.sidebar.radio("Navegação", ["Matricular Novo Estudante", "Estudantes Matriculados","Gerenciar Contas", "Criar Novo Usuario", "Dashboard", "Conteúdo","Documentos"])

        if opcao == "Matricular Novo Estudante":
            cadastro.show()
        elif opcao == "Estudantes Matriculados":
            matriculados.show()
        elif opcao == "Criar Novo Usuario":
            novosUsuarios.show()
        elif opcao == "Gerenciar Contas":
            gerenciarUsuarios.show()
        elif opcao == "Conteúdo":
            conteudo.show()
        elif opcao == "Dashboard":
            dashboard.show()
        elif opcao == "Documentos":
            documentos.show()

        #BOTÃO LOGOUT
        if st.sidebar.button("Logout"):
            st.session_state['logado'] = False
            st.rerun()

else:

# Apenas ao que o usuario comum tem acesso

# "FRONT-END" - Sidebar

        st.title("😺 MiIA")

        st.subheader(f"Bem-vindo {st.session_state['usuario']}")

        # Menu
        st.sidebar.title("📌 Menu")
        opcao = st.sidebar.radio("Navegação", ["Conteúdo","Documentos", "Dashboard"])


        if opcao == "Conteúdo":
            conteudo.show()
        elif opcao == "Documentos":
            documentos.show()
        elif opcao == "Dashboard":
            dashboard.show()

        #BOTÃO LOGOUT
        if st.sidebar.button("Logout"):
            st.session_state['logado'] = False
            st.rerun()