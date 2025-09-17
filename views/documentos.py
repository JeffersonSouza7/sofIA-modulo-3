import streamlit as st
from utils.file_loader import load_pdf, load_excel, load_txt, load_csv
from utils.qa_chain_groq import create_qa_chain_groq
from utils.limpar_resposta import limpar_resposta

def show():
    st.title("📊 Analise seus documentos com RAG")
    st.write("Analises e estatísticas...")

    st.title(" Converse com seus documentos (PDF, Excel ou TXT)")
    api_key = st.text_input("Digite sua chave da Groq", type="password")

    # Escolha do modelo
    modelo = st.selectbox(
        "Escolha o modelo",
        ["deepseek-r1-distill-llama-70b"]
    )

    #Upload de arquivos pdf
    uploaded_file = st.file_uploader(
            "Faça upload de um PDF ou Excel", type=["pdf", "xlsx", "xls", "csv", "txt"]
        )
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "qa_chain" not in st.session_state:
        st.session_state.qa_chain = None

    if uploaded_file:
        file_type = uploaded_file.name.split(".")[-1]

        with st.spinner("Lendo arquivo..."):
            if file_type == "pdf":
                docs = load_pdf(uploaded_file)
                if not docs:
                    st.error("O arquivo PDF está vazio ou não pôde ser lido corretamente.")
                    return

            elif file_type in ["xlsx", "xls"]:
                docs = load_excel(uploaded_file)

            elif file_type == "txt":
                docs = load_txt(uploaded_file)
                if not docs:
                    st.error("O arquivo TXT está vazio ou não pôde ser lido corretamente.")
                    return

            elif file_type == "csv":
                docs = load_csv(uploaded_file)
                if not docs:
                    st.error("O arquivo CSV está vazio ou não pôde ser lido corretamente.")
                    return
                
            else:
                st.error("Tipo de arquivo não suportado")
                st.stop()

            st.session_state.qa_chain = create_qa_chain_groq(docs,api_key)
            st.success("Arquivo carregado com sucesso!")

    
    if st.session_state.qa_chain:
        user_input = st.chat_input("Digite sua pergunta...")
        if user_input:
            with st.spinner("Pensando..."):
                response = st.session_state.qa_chain.run(user_input)
                response = limpar_resposta(response)
                st.session_state.chat_history.append(("Usuário", user_input))
                st.session_state.chat_history.append(("Bot", response))

    # Exibindo o histórico
        for speaker, msg in st.session_state.chat_history:
            with st.chat_message(speaker):
                st.markdown(msg)