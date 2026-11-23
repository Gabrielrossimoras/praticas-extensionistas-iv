# Práticas Extensionistas IV

## Sistema Inteligente de Controle e Análise de Processos para Despachante

Projeto desenvolvido na disciplina de Práticas Extensionistas IV do curso de Ciência de Dados e Inteligência Artificial.

## Sobre o projeto

Este projeto é uma evolução do Sistema de Controle de Documentos para Despachante desenvolvido anteriormente em Práticas Extensionistas III.

A proposta é aplicar técnicas de Ciência de Dados em uma situação relacionada à rotina de um despachante documentalista, utilizando dados de processos e atendimentos para gerar informações úteis para a gestão.

O projeto realiza o tratamento dos dados, análise dos processos, geração de indicadores e identificação de processos que necessitam de maior atenção.

## Objetivo

Desenvolver uma solução capaz de organizar, tratar e analisar dados relacionados aos processos de um despachante documentalista, auxiliando no acompanhamento dos serviços, prazos e processos pendentes.

## Funcionalidades desenvolvidas

- Organização dos dados dos processos;
- Pipeline de tratamento de dados (ETL);
- Limpeza e padronização dos dados;
- Geração de dataset tratado;
- Análise Exploratória de Dados (EDA);
- Cálculo de indicadores gerenciais;
- Análise da quantidade de processos por serviço;
- Análise do tempo médio de conclusão;
- Identificação de processos pendentes ou em andamento;
- Cálculo dos dias em aberto;
- Classificação de prioridade dos processos;
- Geração de alertas para processos de prioridade alta;
- Geração de resumo gerencial.

## Indicadores analisados

Entre as informações geradas pelo projeto estão:

- Total de processos;
- Quantidade de processos concluídos;
- Quantidade de processos em aberto;
- Tempo médio de conclusão;
- Valor total dos serviços;
- Serviço mais realizado;
- Tipo de veículo mais atendido;
- Principal origem dos atendimentos;
- Quantidade de processos com prioridade alta.

## Tecnologias utilizadas

- Python
- Pandas
- Matplotlib
- Google Colab
- Git
- GitHub
- CSV

## Estrutura do projeto

- `dados/` - bases de dados utilizadas no projeto e dados tratados;
- `documentacao/` - documentação relacionada ao desenvolvimento;
- `src/` - código-fonte do pipeline ETL;
- `analise_processos.ipynb` - notebook responsável pela análise exploratória, indicadores, gráficos e identificação de processos prioritários;
- `README.md` - documentação principal do projeto.

## Pipeline de dados

O processamento dos dados segue o fluxo:

**Dados brutos → Extração → Limpeza → Transformação → Dados tratados → Análise Exploratória → Indicadores**

O arquivo `src/etl.py` realiza o tratamento inicial dos dados e gera uma nova base preparada para análise.

Posteriormente, o notebook `analise_processos.ipynb` utiliza os dados tratados para realizar as análises e gerar informações gerenciais.

## Resultados obtidos

A análise desenvolvida permite visualizar informações importantes sobre a rotina dos processos, como volume de serviços, tempo médio de conclusão e processos que permanecem em aberto.

Também foi implementada uma classificação de prioridade baseada no tempo em que cada processo permanece aberto, permitindo identificar situações que necessitam de maior atenção.

Dessa forma, o projeto demonstra como técnicas de Ciência de Dados podem ser aplicadas em uma situação real de um despachante documentalista, transformando dados operacionais em informações úteis para apoio à gestão.

## Próximas etapas

- Desenvolvimento de novas visualizações;
- Criação de dashboard para acompanhamento dos indicadores;
- Ampliação da base de dados;
- Avaliação da aplicação de técnicas de Machine Learning;
- Evolução do sistema de apoio à gestão dos processos.

## Evolução do Projeto — Práticas Extensionistas IV

Este projeto dá continuidade ao sistema desenvolvido em Práticas Extensionistas III, com o objetivo de melhorar o controle e a análise dos processos de documentação de veículos em um despachante.

A proposta é utilizar técnicas de Ciência de Dados e Inteligência Artificial para organizar informações, acompanhar indicadores e estudar a possibilidade de estimar o tempo necessário para concluir os atendimentos.

O projeto utiliza como estudo aplicado o **Despachante Jumbo**, com registros anonimizados para preservar as informações dos clientes.

### Sprint 4 — Tratamento e Análise Exploratória dos Dados

**Situação: Concluída**

Nesta etapa, foi desenvolvido e executado um processo de ETL (Extração, Transformação e Carga) utilizando Python e Pandas.

As atividades realizadas foram:

- Organização dos dados brutos e tratados.
- Leitura de registros anonimizados de atendimentos.
- Limpeza e padronização das informações.
- Preparação do dataset para análise e modelagem.
- Análise exploratória dos processos.
- Geração de gráficos e indicadores.
- Elaboração do Relatório de Insights.

A base utilizada contém sete atendimentos, sendo seis concluídos e um pendente.

**Entregáveis:**

- `src/etl.py`
- `dados/tratados/dataset_final_treinamento.csv`
- `EDA_Sprint4_Pratica_Extensionista_IV.ipynb`
- `documentacao/Relatório de Insights.pdf`

### Sprint 5 — Modelagem Preditiva Experimental

**Situação: Concluída como prova de conceito**

Nesta etapa, foi desenvolvido um modelo experimental de aprendizado de máquina para estimar o tempo de conclusão de atendimentos.

Foi utilizado o algoritmo **DecisionTreeRegressor (Árvore de Decisão para Regressão)**, da biblioteca scikit-learn.

As variáveis de entrada foram:

- Tipo de serviço.
- Tipo de veículo.
- Origem do atendimento.

A variável que o modelo procura estimar é `dias_conclusao`.

O treinamento utilizou os seis processos concluídos da base disponível.

**Resultados experimentais:**

| Indicador | Resultado |
|---|---|
| Registros utilizados no treinamento | 6 |
| MAE de treinamento | 0,67 dia |
| RMSE de treinamento | 0,91 dia |
| Algoritmo | Árvore de Decisão para Regressão |
| Validação independente | Não realizada |

Também foi realizada uma simulação de transferência de automóvel, na qual o modelo apresentou uma estimativa experimental de 0,50 dia.

**Limitação importante:** devido à pequena quantidade de registros, os resultados demonstram apenas o funcionamento técnico do modelo. As métricas foram calculadas sobre os próprios dados de treinamento e não comprovam a capacidade de previsão para novos atendimentos.

**Entregáveis:**

- `Sprint5_Modelagem_Preditiva.ipynb`
- `documentacao/Relatorio Tecnico Sprint5.pdf`

### Sprint 6 — Desenvolvimento da Interface e Integração

**Situação: Planejada**

A próxima etapa será o desenvolvimento de uma interface visual para facilitar a consulta e o acompanhamento dos processos.

Está prevista a utilização do Streamlit, integrado ao Python e aos dados tratados.

As funcionalidades planejadas incluem:

- Painel com indicadores de atendimentos.
- Visualização dos processos concluídos e pendentes.
- Gráficos por tipo de serviço e veículo.
- Acompanhamento dos prazos.
- Consulta aos valores registrados.
- Simulação experimental do tempo de conclusão de novos atendimentos.

As estimativas do modelo continuarão identificadas como demonstrativas até que seja possível realizar uma validação com dados independentes.

### Tecnologias Utilizadas

- Python
- Pandas
- Matplotlib
- scikit-learn
- Google Colab
- Git e GitHub
- Streamlit (planejado para a Sprint 6)

### Próximos Passos

Ampliar a base de atendimentos anonimizados, desenvolver a interface visual, integrar os indicadores e o modelo experimental e realizar novos testes para avaliar a evolução do sistema.

O objetivo final é construir uma ferramenta que auxilie na organização dos atendimentos e na tomada de decisões dentro da rotina de um despachante documentalista.

## Autor

**Gabriel Rossi Moras**

Curso de Ciência de Dados e Inteligência Artificial
