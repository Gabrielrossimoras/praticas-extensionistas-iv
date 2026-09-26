import pandas as pd
from pathlib import Path

# --------------------------------------------------
# 1. Definição dos caminhos
# --------------------------------------------------

PASTA_PROJETO = Path(__file__).resolve().parent.parent

arquivo_entrada = PASTA_PROJETO / "dados" / "dados_processos.csv"
arquivo_saida = PASTA_PROJETO / "dados" / "dados_processos_tratados.csv"


# --------------------------------------------------
# 2. EXTRAÇÃO
# --------------------------------------------------

print("Iniciando o pipeline ETL...")

df = pd.read_csv(arquivo_entrada)

print(f"Dados carregados com sucesso: {len(df)} registros.")


# --------------------------------------------------
# 3. TRANSFORMAÇÃO
# --------------------------------------------------

# Remover possíveis registros duplicados
df = df.drop_duplicates()

# Converter as colunas de data
df["data_entrada"] = pd.to_datetime(
    df["data_entrada"],
    errors="coerce"
)

df["data_conclusao"] = pd.to_datetime(
    df["data_conclusao"],
    errors="coerce"
)

# Padronizar campos de texto
df["tipo_servico"] = df["tipo_servico"].str.strip().str.title()
df["status"] = df["status"].str.strip().str.title()
df["origem_atendimento"] = df["origem_atendimento"].str.strip().str.title()
df["tipo_veiculo"] = df["tipo_veiculo"].str.strip().str.title()

# Garantir que o valor do serviço seja numérico
df["valor_servico"] = pd.to_numeric(
    df["valor_servico"],
    errors="coerce"
)

# Identificar se o processo foi concluído
df["processo_concluido"] = df["data_conclusao"].notna()

# Calcular o tempo de conclusão dos processos
df["tempo_conclusao_dias"] = (
    df["data_conclusao"] - df["data_entrada"]
).dt.days

# Criar informações de mês e ano para futuras análises
df["ano_entrada"] = df["data_entrada"].dt.year
df["mes_entrada"] = df["data_entrada"].dt.month


# --------------------------------------------------
# 4. CARGA
# --------------------------------------------------

df.to_csv(
    arquivo_saida,
    index=False,
    encoding="utf-8-sig"
)

print("Tratamento dos dados concluído.")
print(f"Dataset tratado salvo em: {arquivo_saida}")
print("Pipeline ETL finalizado com sucesso.")
