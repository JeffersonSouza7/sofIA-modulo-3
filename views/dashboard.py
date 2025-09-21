import streamlit as st
import plotly.express as px
import pandas as pd
from controllers.estudante_controller import listar_estudantes

def show():
    st.title("📊 Dashboard Escolar")
    st.write("Relatórios e estatísticas dos alunos aqui...")

    estudantes = listar_estudantes()

    if not estudantes:
        st.warning("Nenhum estudante cadastrado.")
        return

    # Criando DataFrame
    data = pd.DataFrame([{
        "Nome": i.nome,
        "Nota 1": i.nota1,
        "Nota 2": i.nota2,
        "Média": i.media
    } for i in estudantes])

    # Exibiindo tabela
    st.subheader("Lista de Estudantes")
    st.table(data.style.format({"Nota 1": "{:.2f}", "Nota 2": "{:.2f}", "Média": "{:.2f}"}))

    # Média geral escolar
    media_geral = data["Média"].mean()
    st.subheader("Média Geral da Escola")
    st.metric(label="Média Geral", value=f"{media_geral:.2f}")

    # Filtros
    st.subheader("Filtros")
    faixa_media = st.slider("Filtrar por faixa de média:", 0.0, 10.0, (0.0, 10.0), step=0.1)
    nomes_disponiveis = data["Nome"].unique()
    nomes_selecionados = st.multiselect("Selecionar estudantes:", options=nomes_disponiveis, default=nomes_disponiveis)

    # Aplicar filtros
    data_filtrada = data[
        (data["Média"] >= faixa_media[0]) &
        (data["Média"] <= faixa_media[1]) &
        (data["Nome"].isin(nomes_selecionados))
    ]

    # Gráfico de barras (filtrado)
    st.subheader("Gráfico de Médias Individuais")
    if not data_filtrada.empty:
        fig_bar = px.bar(
            data_filtrada,
            x="Nome",
            y="Média",
            title="Média Individual dos Estudantes (Filtrada)",
            labels={"Média": "Média", "Nome": "Estudante"},
            text="Média",
            range_y=[0, 10]
        )
        fig_bar.update_traces(texttemplate='%{text:.2f}', textposition='outside')
        st.plotly_chart(fig_bar, use_container_width=True)
    else:
        st.info("Nenhum estudante corresponde aos filtros selecionados.")

    # Gráfico de pizza com dados filtrados
    st.subheader("Distribuição de Categorias de Média")

    categorias = {
        "Abaixo de 5": 0,
        "Entre 5 e 7": 0,
        "Acima de 7": 0
    }
    for _, row in data_filtrada.iterrows():
        media = row["Média"]
        if media < 5:
            categorias["Abaixo de 5"] += 1
        elif media <= 7:
            categorias["Entre 5 e 7"] += 1
        else:
            categorias["Acima de 7"] += 1

    if sum(categorias.values()) > 0:
        fig_pie = px.pie(
            names=list(categorias.keys()),
            values=list(categorias.values()),
            title="Distribuição das Médias dos Estudantes (Filtrada)",
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(fig_pie, use_container_width=True)
    else:
        st.info("Não há dados para gerar o gráfico de pizza com os filtros aplicados.")