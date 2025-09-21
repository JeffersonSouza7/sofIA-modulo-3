import streamlit as st
from controllers.usuarios_controller import listar_usuarios, atualizar_usuario, deletar_usuario

def show():

    st.title("👥 Gerenciar usuários existentes")

    usuarios = listar_usuarios()

    for usuario in usuarios:
                user_id, username = usuario

                if username == "admin":
                    continue  # Evita que admin se exclua ou edite

                with st.expander(f"Usuário: {username}"):
                    novo_username = st.text_input(f"Novo nome de usuário (ID: {user_id})", value=username, key=f"user_{user_id}")
                    nova_senha = st.text_input(f"Nova senha", type="password", key=f"senha_{user_id}")

                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button("💾 Atualizar", key=f"update_{user_id}"):
                            if atualizar_usuario(user_id, novo_username, nova_senha):
                                st.success(f"Usuário '{username}' atualizado.")
                                st.rerun()
                            else:
                                st.error("Erro ao atualizar usuário.")

                    with col2:
                        if st.button("🗑️ Excluir", key=f"delete_{user_id}"):
                            deletar_usuario(user_id)
                            st.warning(f"Usuário '{username}' deletado.")
                            st.rerun()