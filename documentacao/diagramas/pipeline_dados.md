# Diagrama do Pipeline de Dados

O pipeline de dados representa o fluxo das informações desde o registro dos processos realizados pelo despachante até a geração de indicadores e visualizações.

```mermaid
flowchart LR
    A[Dados dos Clientes e Veículos] --> B[Dados dos Processos]
    B --> C[Extração dos Dados]
    C --> D[Limpeza dos Dados]
    D --> E[Padronização e Tratamento]
    E --> F[Dataset Tratado]
    F --> G[Análise Exploratória - EDA]
    G --> H[Cálculo de Indicadores]
    H --> I[Gráficos]
    H --> J[Dashboard]
    I --> K[Análise dos Resultados]
    J --> K
```

## Etapas do Pipeline

### 1. Dados dos clientes, veículos e processos
Os dados são gerados durante os atendimentos realizados pelo despachante e ficam armazenados no sistema.

### 2. Extração dos dados
Os dados necessários para a análise são extraídos da base utilizada pelo sistema.

### 3. Limpeza dos dados
Nesta etapa serão identificados dados ausentes, duplicados ou inconsistentes que possam prejudicar as análises.

### 4. Padronização e tratamento
Os dados serão organizados e padronizados utilizando principalmente Python e a biblioteca Pandas.

### 5. Dataset tratado
Após o tratamento será gerado um conjunto de dados organizado e adequado para realização das análises.

### 6. Análise Exploratória de Dados
Será realizada a análise exploratória para compreender as características dos dados e identificar padrões relacionados aos processos e serviços.

### 7. Cálculo de indicadores
Serão calculados indicadores como quantidade de processos, situação dos serviços, prazos, atrasos e tempo de conclusão.

### 8. Visualização dos resultados
Os resultados serão apresentados por meio de gráficos e dashboard, facilitando a interpretação das informações.

## Objetivo

O objetivo do pipeline é transformar os dados gerados no dia a dia do despachante em informações organizadas que possam auxiliar no acompanhamento dos processos e na tomada de decisão.
