import streamlit as st
import pandas as pd
import sqlite3
import time
import plotly.express as px
import base64

st.set_page_config(page_title="Painel de Velocidade", layout="wide")


DB_PATH = "velocidades.db"

# Função para carregar dados do banco
def carregar_dados():
    conn = sqlite3.connect(DB_PATH)
    query = """
    SELECT
        id,
        velocidade,
        datetime(data_captura, 'localtime') AS data_captura,
        CASE
            WHEN velocidade >= 120 THEN 'Vel. Extrema'
            WHEN velocidade >= 100 THEN 'Alta Vel.'
            WHEN velocidade >= 60 THEN 'Vel. Normal'
            ELSE 'Baixa Vel.'
        END AS categoria_velocidade
    FROM velocidades;
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Layout do painel
st.title("🚗 Painel de Monitoramento de Velocidades")
st.markdown("Atualização automática a cada 5 segundos")

# Loop de atualização
while True:
    df = carregar_dados()

    if not df.empty:
        # COLUNAS
        col2, col3, col1 = st.columns([1.2, 1.2, 1.2])  # controla proporções das colunas

       

        # GRÁFICO 1: Categorias de velocidade
        with col2:
            contagem = df["categoria_velocidade"].value_counts().reset_index()
            contagem.columns = ["Categoria", "Quantidade"]
            contagem = contagem.sort_values(by="Quantidade", ascending=False)

            fig_barras = px.bar(
                contagem,
                x="Quantidade",
                y="Categoria",
                orientation="h",
                title="Distribuição por Faixa de Velocidade",
                text="Quantidade",
                color="Categoria",
                color_discrete_sequence=px.colors.sequential.Redor,
            )
            fig_barras.update_traces(textposition="outside")
            fig_barras.update_layout(
                yaxis_title="",
                xaxis_title="Qtd. de Condutores",
                yaxis=dict(categoryorder="total ascending"),
                template="plotly_dark",
                height=400
            )
            st.plotly_chart(fig_barras, use_container_width=True)

        # GRÁFICO 2: Velocidade x Tempo
        with col3:
            df_sorted = df.sort_values(by="data_captura")
            fig_linha = px.line(
                df_sorted,
                x="data_captura",
                y="velocidade",
                title="Evolução das Velocidades no Tempo",
                markers=True,
                line_shape="spline",
            )
            fig_linha.update_layout(
                xaxis_title="Horário da Captura",
                yaxis_title="Velocidade (km/h)",
                template="plotly_dark",
                height=400
            )
            st.plotly_chart(fig_linha, use_container_width=True)

         # CARD: Velocidade Máxima 
        with col1:
            velocidade_max = df["velocidade"].max()
            velocidade_min = df["velocidade"].min()
            velocidade_media = df["velocidade"].mean()
            Qtd_total_condutores= df["id"].count()
            st.metric(
                label="💨 Velocidade Máxima (km/h)",
                value=f"{velocidade_max:.2f}",
                help="Velocidade mais alta registrada até agora.",
            )
            st.metric(
                label="💨 Velocidade Mínima (km/h)",
                value=f"{velocidade_min:.2f}",
                help="Velocidade mais baixas registrada até agora."
            )
            st.metric(
                label="🚗 Velocidade Média (km/h)",
                value=f"{velocidade_media:.2f}",
                help="Velocidade média registrada até agora."
            )
            st.metric(
                label="🚶‍♀️‍➡️ Total de condutores",
                value=f"{Qtd_total_condutores}",
                help="Total de condutores registrados até agora."
            )

    else:
        st.warning("Ainda não há dados registrados no banco de dados.")

    time.sleep(7)
    st.rerun()
