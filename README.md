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

## Autor

**Gabriel Rossi Moras**

Curso de Ciência de Dados e Inteligência Artificial
