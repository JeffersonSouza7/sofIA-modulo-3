import streamlit as st
from controllers.estudante_controller import listar_estudantes, atualizar_estudante, deletar_estudante


def show():
    
    st.title("👤 Estudantes matriculados")

    st.subheader("Lista de Estudantes")
    estudantes = listar_estudantes()
    
    for estudante in estudantes:
        matricula = estudante.matricula
        nome = estudante.nome
        idade = estudante.idade
        nota1 = estudante.nota1
        nota2 = estudante.nota2
        media = estudante.media
        

        with st.expander(f"📚 Estudante: {nome} (Matrícula: {matricula})"):
            novo_nome = st.text_input("Nome", value=nome, key=f"nome_{matricula}")
            nova_idade = st.number_input("Idade", value=idade, key=f"idade_{matricula}", min_value=0)
            nova_nota1 = st.number_input("Nota 1", value=nota1, key=f"nota1_{matricula}", min_value=0.0, max_value=10.0)
            nova_nota2 = st.number_input("Nota 2", value=nota2, key=f"nota2_{matricula}", min_value=0.0, max_value=10.0)

            col1, col2 = st.columns(2)

            with col1:
                if st.button("💾 Atualizar", key=f"update_{matricula}"):
                    try:
                        atualizar_estudante(matricula, novo_nome, nova_idade, nova_nota1, nova_nota2)
                        st.success(f"Estudante '{nome}' atualizado com sucesso.")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Erro ao atualizar estudante: {e}")

            with col2:
                if st.button("🗑️ Excluir", key=f"delete_{matricula}"):
                    try:
                        deletar_estudante(matricula)
                        st.warning(f"Estudante '{nome}' deletado.")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Erro ao deletar estudante: {e}")