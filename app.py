
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# Configuração
st.set_page_config(
    page_title="Despachante Jumbo - Sistema Inteligente",
    page_icon="🚗",
    layout="wide"
)

BASE = Path(__file__).resolve().parent

st.title("🚗 Sistema Inteligente de Controle de Processos")
st.caption("Despachante Jumbo | Práticas Extensionistas IV - Sprint 6")

# Carregar dados
@st.cache_data
def carregar_dados():
    caminho = BASE / "dados" / "tratados" / "dataset_final_treinamento.csv"
    return pd.read_csv(caminho)

try:
    df = carregar_dados()
except Exception as erro:
    st.error(f"Não foi possível carregar os dados: {erro}")
    st.stop()

# Indicadores
st.header("📊 Painel Gerencial")

total = len(df)
concluidos = (df["status"] == "concluido").sum()
pendentes = total - concluidos

col1, col2, col3 = st.columns(3)
col1.metric("Total de processos", total)
col2.metric("Concluídos", concluidos)
col3.metric("Não concluídos", pendentes)

col4, col5 = st.columns(2)

with col4:
    st.subheader("Atendimentos por serviço")
    st.bar_chart(df["tipo_servico"].value_counts())

with col5:
    st.subheader("Atendimentos por veículo")
    st.bar_chart(df["tipo_veiculo"].value_counts())

if "dias_conclusao" in df.columns:
    media = pd.to_numeric(
        df.loc[df["status"] == "concluido", "dias_conclusao"],
        errors="coerce"
    ).mean()
    if pd.notna(media):
        st.metric("Tempo médio de conclusão", f"{media:.2f} dias")

if "valor_servico" in df.columns:
    valores = pd.to_numeric(df["valor_servico"], errors="coerce")
    st.metric("Valor total registrado", f"R$ {valores.sum():,.2f}")

st.divider()

# Integração com modelo preditivo
st.header("🤖 Previsão experimental com Inteligência Artificial")

st.warning(
    "Modelo demonstrativo treinado com uma amostra muito pequena. "
    "As estimativas não devem ser usadas como prazos oficiais."
)

@st.cache_resource
def carregar_modelo():
    return joblib.load(BASE / "modelo_preditivo.joblib")

try:
    modelo = carregar_modelo()
except Exception as erro:
    st.error(f"Não foi possível carregar o modelo: {erro}")
    st.stop()

servico = st.selectbox(
    "Tipo de serviço",
    sorted(df["tipo_servico"].dropna().unique())
)

veiculo = st.selectbox(
    "Tipo de veículo",
    sorted(df["tipo_veiculo"].dropna().unique())
)

origem = st.selectbox(
    "Origem do atendimento",
    sorted(df["origem_atendimento"].dropna().unique())
)

if st.button("Calcular previsão", type="primary"):
    entrada = pd.DataFrame([{
        "tipo_servico": servico,
        "tipo_veiculo": veiculo,
        "origem_atendimento": origem
    }])

    try:
        previsao = float(modelo.predict(entrada)[0])
        previsao = max(0, previsao)

        st.success(
            f"Tempo estimado experimental: {previsao:.2f} dia(s)"
        )
        st.info(
            "Resultado apenas demonstrativo. "
            "É necessária validação com novos atendimentos."
        )
    except Exception as erro:
        st.error(f"Erro ao realizar previsão: {erro}")

st.divider()
st.caption("Projeto acadêmico - UNOESC | Práticas Extensionistas IV")

