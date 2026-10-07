"""Sprint 4 - ETL dos atendimentos anonimizados do Despachante Jumbo.
Executar na raiz do repositorio: python src/etl.py
Dependencias: pandas, openpyxl
"""
from pathlib import Path
import unicodedata
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
ENTRADA = ROOT / 'dados' / 'brutos' / 'atendimentos_reais_anonimizados.xlsx'
SAIDA = ROOT / 'dados' / 'tratados' / 'dataset_final_treinamento.csv'
COLUNAS = ['id_processo','data_abertura','tipo_servico','origem_atendimento',
           'tipo_veiculo','status','data_conclusao','prazo_previsto',
           'documentacao_pendente','valor_servico']

def normalizar(valor):
    if pd.isna(valor):
        return ''
    texto = str(valor).strip().lower()
    return ''.join(c for c in unicodedata.normalize('NFKD', texto)
                   if not unicodedata.combining(c))

def executar():
    if not ENTRADA.exists():
        raise FileNotFoundError(f'Planilha nao encontrada: {ENTRADA}')
    df = pd.read_excel(ENTRADA, dtype={'id_processo': str})
    faltantes = set(COLUNAS) - set(df.columns)
    if faltantes:
        raise ValueError(f'Colunas ausentes: {sorted(faltantes)}')
    df = df[COLUNAS].copy()
    if df['id_processo'].isna().any() or df['id_processo'].duplicated().any():
        raise ValueError('IDs vazios ou duplicados encontrados.')

    for coluna in ['tipo_servico','origem_atendimento','tipo_veiculo','status','documentacao_pendente']:
        df[coluna] = df[coluna].map(normalizar)
    for coluna in ['data_abertura','data_conclusao','prazo_previsto']:
        # Normaliza para data: descarta o horario existente no Excel.
        df[coluna] = pd.to_datetime(df[coluna], errors='coerce', dayfirst=True).dt.normalize()
    df['valor_servico'] = pd.to_numeric(df['valor_servico'], errors='coerce')

    df['dias_conclusao'] = (df['data_conclusao'] - df['data_abertura']).dt.days
    df['prazo_dias'] = (df['prazo_previsto'] - df['data_abertura']).dt.days
    df['mes_abertura'] = df['data_abertura'].dt.month
    df['dia_semana_abertura'] = df['data_abertura'].dt.dayofweek
    df['concluido'] = df['status'].eq('concluido').astype(int)
    # Atraso so e conhecido quando ha data de conclusao.
    df['atrasou'] = pd.NA
    concluidos = df['concluido'].eq(1) & df['data_conclusao'].notna() & df['prazo_previsto'].notna()
    df.loc[concluidos, 'atrasou'] = (df.loc[concluidos, 'data_conclusao'] > df.loc[concluidos, 'prazo_previsto']).astype(int)

    inconsistentes = df.loc[(df['dias_conclusao'] < 0) | (df['prazo_dias'] < 0)]
    if not inconsistentes.empty:
        raise ValueError(f'Datas inconsistentes nos IDs: {inconsistentes.id_processo.tolist()}')
    for coluna in ['data_abertura','data_conclusao','prazo_previsto']:
        df[coluna] = df[coluna].dt.strftime('%Y-%m-%d')
    SAIDA.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(SAIDA, index=False, encoding='utf-8-sig')
    print(f'ETL concluido: {len(df)} atendimentos; {df.concluido.sum()} concluidos; {(df.concluido == 0).sum()} nao concluidos.')
    print(f'Arquivo gerado: {SAIDA}')
    print('ATENCAO: esta base pequena serve para demonstracao, nao para validar modelo preditivo.')

if __name__ == '__main__':
    executar()
