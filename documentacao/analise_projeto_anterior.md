# Análise Crítica do Projeto Desenvolvido em Práticas Extensionistas III

## 1. Projeto desenvolvido anteriormente

Em Práticas Extensionistas III foi desenvolvido o projeto denominado Sistema de Controle de Documentos para Despachante.

A proposta surgiu a partir da necessidade de melhorar a organização dos processos realizados por um despachante documentalista, principalmente no controle de clientes, veículos, serviços, documentos, prazos e andamento dos processos.

O sistema foi pensado para centralizar essas informações e facilitar o acompanhamento dos serviços desde o atendimento inicial até a conclusão do processo.

## 2. Solução desenvolvida

A solução desenvolvida em Práticas Extensionistas III foi estruturada para permitir o cadastro e acompanhamento das principais informações utilizadas na rotina do despachante.

A modelagem foi organizada principalmente pelas seguintes entidades:

- Cliente;
- Veículo;
- Processo;
- Serviço;
- Status;
- Documento;
- Origem.

O cliente pode possuir um ou mais veículos e cada veículo pode estar relacionado a diferentes processos. Cada processo possui informações sobre o serviço realizado, situação atual, documentos necessários, prazo e origem do atendimento.

Também foram previstas funcionalidades como:

- Cadastro de clientes;
- Cadastro de veículos;
- Cadastro de serviços;
- Registro de processos;
- Controle de documentos;
- Controle de documentos pendentes;
- Controle de prazos;
- Atualização do status;
- Consulta de processos em andamento;
- Consulta de processos atrasados;
- Consulta de processos finalizados.

Além da estrutura do banco de dados, foram desenvolvidos diagramas para representar o funcionamento do sistema, incluindo Diagrama Entidade-Relacionamento, Diagrama de Classes, Casos de Uso, Diagrama de Atividades e Diagrama de Sequência.

## 3. Pontos satisfatórios

A análise do projeto anterior mostrou que a solução possui uma estrutura adequada para representar as principais informações utilizadas na rotina de um despachante.

Um dos principais pontos positivos foi a centralização das informações. Em vez de manter dados de clientes, veículos, documentos e processos separados, a proposta permite relacionar essas informações dentro de uma mesma estrutura.

Outro ponto positivo foi a definição dos relacionamentos entre as entidades. A ligação entre cliente, veículo e processo representa de maneira simples o fluxo de atendimento realizado pelo despachante.

O controle de status, documentos e prazos também é importante, pois permite acompanhar a situação de cada processo e identificar serviços que ainda precisam de alguma ação.

A modelagem desenvolvida anteriormente também fornece uma boa base para a continuidade do projeto, evitando a necessidade de iniciar uma nova solução do zero.

## 4. Limitações identificadas

Apesar dos pontos positivos, foram identificadas algumas limitações que podem ser melhoradas nesta nova etapa do projeto.

A principal limitação é que a solução desenvolvida anteriormente está concentrada no controle operacional dos processos. O sistema registra e organiza informações, mas ainda não utiliza esses dados para produzir análises sobre os atendimentos realizados.

Também não foram desenvolvidos indicadores que permitam identificar, por exemplo:

- Quantidade de processos realizados;
- Serviços mais procurados;
- Quantidade de processos atrasados;
- Tempo médio para conclusão;
- Principais tipos de pendências;
- Origem dos atendimentos;
- Distribuição dos processos por status.

Outra limitação identificada é a necessidade de acrescentar algumas informações ao conjunto de dados, principalmente a data de conclusão dos processos. Essa informação será importante para calcular o tempo utilizado na realização de cada serviço e verificar o cumprimento dos prazos.

Também será necessário melhorar a estrutura utilizada para análise dos dados, separando os dados utilizados na rotina operacional daqueles preparados para análise.

## 5. Melhorias prioritárias

A partir das limitações identificadas, foram definidas algumas melhorias para a evolução da solução.

As principais melhorias serão:

1. Revisar e atualizar os requisitos do sistema;
2. Revisar a estrutura dos dados utilizados nos processos;
3. Acrescentar informações necessárias para análise, como data de conclusão;
4. Criar uma base de dados adequada para análise;
5. Desenvolver um pipeline ETL para tratamento dos dados;
6. Realizar uma Análise Exploratória de Dados (EDA);
7. Criar indicadores relacionados aos processos e atendimentos;
8. Desenvolver visualizações e um dashboard;
9. Avaliar a possibilidade de utilização de técnicas de Machine Learning;
10. Melhorar a documentação e o controle das versões do projeto utilizando Git e GitHub.

## 6. Evolução proposta para Práticas Extensionistas IV

Em Práticas Extensionistas IV, a proposta é manter a base desenvolvida anteriormente e acrescentar uma camada de análise de dados.

O sistema continuará tendo como finalidade principal auxiliar no controle dos processos realizados pelo despachante, porém os dados registrados também serão utilizados para gerar informações sobre o funcionamento dos atendimentos.

A evolução pode ser representada de forma simplificada pelo seguinte fluxo:

Dados dos processos
↓
Extração dos dados
↓
Tratamento e padronização
↓
Dataset tratado
↓
Análise Exploratória de Dados
↓
Indicadores
↓
Dashboard

Dessa forma, o projeto deixa de ser apenas uma solução de registro e controle e passa também a utilizar os dados para auxiliar na análise e na tomada de decisão.

## 7. Conclusão da análise

A análise do projeto desenvolvido em Práticas Extensionistas III mostrou que a estrutura criada anteriormente continua adequada como base para a evolução da solução.

As principais entidades, relacionamentos e funcionalidades serão mantidos, porém alguns elementos serão revisados e ampliados para permitir a aplicação de técnicas de Ciência de Dados.

A principal evolução será transformar os dados gerados pelos processos em informações que possam auxiliar no acompanhamento dos serviços, identificação de atrasos, análise dos prazos e compreensão da demanda dos atendimentos.

Com isso, o projeto de Práticas Extensionistas IV dará continuidade ao trabalho anterior, acrescentando novos recursos sem perder a proposta original do sistema.
