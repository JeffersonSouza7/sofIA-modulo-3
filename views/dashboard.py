import streamlit as st
import plotly.express as px
from controllers.estudante_controller import listar_estudantes


def show():
    st.title("📊 Dashboard Escolar")
    st.write("Relatórios e estatísticas dos alunos aqui...")

    estudantes = listar_estudantes()

    # Se não tiver nenhum estudante cadastrado
    if not estudantes:
        st.warning("Nenhum estudante cadastrado.")
        return
    
    # Caso tenha
    data = []
    for i in estudantes:
        data.append({
            "Nome": i.nome,
            "Nota 1": f"{i.nota1:.2f}",
            "Nota 2": f"{i.nota2:.2f}",
            "Média": f"{i.media:.2f}"
        })

    # Exibir tabela
    st.subheader("Lista de Estudantes")
    st.table(data)

     # Calculando a média geral da escola
    soma_medias = sum(i.media for i in estudantes)
    media_geral = soma_medias / len(estudantes)

    st.subheader("Média Geral da Escola")
    st.metric(label="Média Geral", value=f"{media_geral:.2f}")

    # Gráfico de barras: médias por estudante
    fig_bar = px.bar(
        data,
        x="Nome",
        y="Média",
        title="Média Individual dos Estudantes",
        labels={"Média": "Média", "Nome": "Estudante"},
        text="Média",
        range_y=[0, 10]  # As notas variam de 0 a 10
    )
    fig_bar.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    st.plotly_chart(fig_bar, use_container_width=True)

    # Categorizando estudantes por média para gráfico de pizza
    categorias = {
        "Abaixo de 5": 0,
        "Entre 5 e 7": 0,
        "Acima de 7": 0
    }
    for e in estudantes:
        if e.media < 5:
            categorias["Abaixo de 5"] += 1
        elif e.media <= 7:
            categorias["Entre 5 e 7"] += 1
        else:
            categorias["Acima de 7"] += 1

    fig_pie = px.pie(
        names=list(categorias.keys()),
        values=list(categorias.values()),
        title="Distribuição das Médias dos Estudantes",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(fig_pie, use_container_width=True)