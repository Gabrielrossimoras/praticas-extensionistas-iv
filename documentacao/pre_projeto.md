# Pré-Projeto

## Sistema Inteligente de Controle e Análise de Processos para Despachante

### 1. Assunto

Ciência de Dados aplicada à gestão de processos e serviços de despachante documentalista.

### 2. Tema

Utilização da análise de dados para auxiliar no controle de processos, documentos, prazos e serviços realizados por um despachante documentalista.

### 3. Título

Sistema Inteligente de Controle e Análise de Processos para Despachante

### 4. Delimitação / Escopo

O projeto será desenvolvido com foco na evolução do Sistema de Controle de Documentos para Despachante desenvolvido anteriormente em Práticas Extensionistas III. A nova etapa terá como objetivo utilizar os dados dos processos e atendimentos para gerar informações que possam auxiliar na organização e na gestão dos serviços realizados pelo despachante.

A solução deverá trabalhar com informações relacionadas aos processos, como tipo de serviço, origem do atendimento, data de início, prazo, status, documentos pendentes e data de conclusão. Esses dados serão organizados e tratados para permitir a realização de análises e a criação de indicadores.

O projeto ficará limitado à gestão interna dos processos e à análise dos dados gerados pelos atendimentos. Nesta etapa, não será realizada integração direta com sistemas externos, como DETRAN, SENATRAN ou outros órgãos públicos.

### 5. Problema

Na rotina de um despachante documentalista são realizados diferentes tipos de serviços relacionados a veículos, envolvendo clientes, documentos, prazos e diversas etapas até a conclusão de cada processo. Quando essas informações não estão organizadas em um único ambiente, podem ocorrer dificuldades no acompanhamento dos serviços, documentos pendentes e prazos.

No projeto anterior foi proposta a centralização das informações de clientes, veículos e processos para reduzir atrasos e facilitar o acompanhamento dos atendimentos.

Porém, além de organizar essas informações, também é possível utilizar os dados gerados pelos próprios atendimentos para compreender melhor a rotina do despachante. Informações como quantidade de processos realizados, serviços mais procurados, processos atrasados, tempo de conclusão e origem dos atendimentos podem auxiliar na identificação de problemas e na melhoria da gestão.

Dessa forma, o problema deste projeto está relacionado à dificuldade de transformar os dados dos processos e atendimentos em informações úteis para auxiliar no controle e na tomada de decisão do despachante.

### 6. Questão de Pesquisa

Como a análise dos dados dos processos e atendimentos pode contribuir para melhorar o controle de documentos, prazos e serviços realizados por um despachante documentalista?

### 7. Hipóteses

A principal hipótese do projeto é que a organização e análise dos dados dos processos poderá facilitar a identificação de atrasos, documentos pendentes e padrões nos serviços realizados pelo despachante.

Também se considera que a utilização de indicadores e visualizações poderá tornar mais simples o acompanhamento dos processos, permitindo identificar quais serviços possuem maior demanda, quais apresentam maior tempo de conclusão e quais situações geram mais pendências.

Por fim, acredita-se que a centralização das informações e a utilização de técnicas de Ciência de Dados poderão contribuir para uma gestão mais organizada e para a redução de falhas no acompanhamento dos processos.

### 8. Justificativa

O desenvolvimento deste projeto se justifica pela necessidade de melhorar a organização e o acompanhamento dos processos realizados por despachantes documentalistas. A rotina desse profissional envolve diferentes serviços, documentos e prazos, sendo necessário acompanhar cada processo desde o atendimento inicial até sua conclusão.

No projeto desenvolvido anteriormente foi proposta uma solução para centralizar essas informações. Nesta nova etapa, pretende-se evoluir essa solução utilizando conceitos de Ciência de Dados.

Os dados registrados poderão ser tratados e analisados para gerar indicadores sobre os atendimentos e auxiliar na identificação de situações que precisam de maior atenção.

Além de contribuir para a organização da rotina do despachante, o projeto permite aplicar na prática conhecimentos relacionados a banco de dados, programação, tratamento de dados, análise exploratória e visualização de informações.

### 9. Relevância Regional e Sustentabilidade

Os serviços prestados por despachantes documentalistas fazem parte da rotina de pessoas e empresas que possuem veículos e necessitam realizar procedimentos relacionados à documentação veicular.

No Oeste Catarinense, a solução poderá auxiliar pequenos escritórios de despachante a utilizar melhor os dados gerados em seus próprios atendimentos, transformando registros operacionais em informações que contribuam para a gestão do negócio.

A digitalização e organização dos dados também pode diminuir a dependência de controles realizados exclusivamente em papel, reduzir retrabalho e melhorar o acompanhamento dos processos.

Caso apresente resultados positivos, a solução também possui potencial para futuramente ser adaptada para utilização por outros escritórios de despachantes.

### 10. Objetivo Geral

Desenvolver a evolução de um sistema de controle de processos para despachante documentalista, utilizando técnicas de Ciência de Dados para organizar, tratar e analisar os dados dos atendimentos, gerando informações que auxiliem no controle de documentos, prazos e serviços.

### 11. Objetivos Específicos

- Revisar e aprimorar a estrutura desenvolvida em Práticas Extensionistas III.
- Organizar os dados relacionados aos processos e atendimentos realizados pelo despachante.
- Desenvolver um processo de extração, tratamento e transformação dos dados (ETL).
- Realizar uma análise exploratória dos dados para identificar padrões e informações relevantes.
- Criar indicadores relacionados aos serviços, prazos, status e pendências.
- Desenvolver posteriormente uma interface ou dashboard para visualização das informações.
- Avaliar a possibilidade de utilização de técnicas de Machine Learning conforme a quantidade e a qualidade dos dados disponíveis.

### 12. Estudo de Viabilidade

#### Viabilidade Técnica

O projeto apresenta viabilidade técnica, pois poderá ser desenvolvido utilizando tecnologias acessíveis como Python, Pandas, banco de dados, Google Colab e ferramentas para criação de gráficos e dashboards.

#### Viabilidade Operacional

A solução será desenvolvida considerando uma utilização simples e voltada à rotina de um escritório de despachante.

#### Viabilidade de Tempo

O desenvolvimento será realizado de forma incremental durante a disciplina, iniciando pela modelagem e preparação dos dados e avançando para análise, desenvolvimento, testes e validação.

#### Viabilidade de Manutenção

O código e a documentação serão organizados utilizando Git e GitHub, permitindo o controle das versões e facilitando futuras alterações no projeto.

### 13. Implantação

Inicialmente, o tratamento e a análise dos dados serão desenvolvidos em Python utilizando o Google Colab.

Posteriormente, os dados tratados poderão ser utilizados em uma interface de visualização ou dashboard. O código e a documentação serão armazenados no GitHub para controle das versões.

Na etapa final será avaliada a possibilidade de disponibilização da solução em ambiente web ou nuvem.

### 14. Plano Inicial de Validação

A validação será realizada a partir dos requisitos e critérios de aceitação definidos durante a etapa de modelagem.

Inicialmente, serão realizados testes para verificar se o pipeline consegue importar, tratar e gerar corretamente a base utilizada nas análises.

Também será verificado se os indicadores correspondem aos dados existentes e se as visualizações apresentam as informações de forma clara.

Posteriormente, a solução será avaliada quanto à facilidade de utilização e à utilidade das informações para a rotina do despachante.

### 15. Cronograma

| Período | Atividade |
|---|---|
| Agosto | Revisão do projeto anterior, definição do problema e pré-projeto |
| Agosto/Setembro | Revisão dos requisitos e atualização da modelagem |
| Setembro | Preparação da base de dados e desenvolvimento do ETL inicial |
| Setembro | Análise exploratória inicial dos dados |
| Outubro | Tratamento final dos dados e aprofundamento da EDA |
| Outubro/Novembro | Avaliação de técnicas analíticas e Machine Learning |
| Novembro | Desenvolvimento do dashboard e integração da solução |
| Novembro | Testes e validação |
| Dezembro | Ajustes, documentação e entrega final |
