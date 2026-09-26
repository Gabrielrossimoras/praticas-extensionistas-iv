# Requisitos do Projeto

## 1. Revisão dos Requisitos

Os requisitos do Sistema Inteligente de Controle e Análise de Processos para Despachante foram definidos a partir da revisão do projeto desenvolvido em Práticas Extensionistas III.

As funcionalidades relacionadas ao controle dos processos foram mantidas e aperfeiçoadas. Também foram adicionados novos requisitos relacionados ao tratamento, análise e visualização dos dados.

Para a priorização foi utilizada a seguinte classificação:

- Alta: essencial para o funcionamento da solução;
- Média: importante, mas pode ser implementado após as funcionalidades principais;
- Baixa: melhoria que poderá ser implementada futuramente.

---

## 2. Requisitos Funcionais

### RF01 - Cadastro e controle de processos

**Descrição:** O sistema deverá permitir registrar e acompanhar os processos realizados pelo despachante.

**Origem:** Práticas Extensionistas III  
**Situação:** Mantido  
**Prioridade:** Alta

**Critério de aceitação:** O usuário deverá conseguir registrar um processo contendo as informações necessárias e posteriormente consultá-lo.

---

### RF02 - Controle de documentos e pendências

**Descrição:** O sistema deverá permitir registrar os documentos relacionados aos processos e identificar documentos pendentes.

**Origem:** Práticas Extensionistas III  
**Situação:** Mantido  
**Prioridade:** Alta

**Critério de aceitação:** O sistema deverá permitir identificar quais documentos estão relacionados ao processo e quais ainda estão pendentes.

---

### RF03 - Controle de prazos e status

**Descrição:** O sistema deverá armazenar o prazo e o status atual de cada processo.

**Origem:** Práticas Extensionistas III  
**Situação:** Mantido e aperfeiçoado  
**Prioridade:** Alta

**Critério de aceitação:** O usuário deverá conseguir consultar a situação atual do processo e verificar seu prazo.

---

### RF04 - Registro da conclusão do processo

**Descrição:** O sistema deverá permitir registrar a data em que o processo foi concluído.

**Origem:** Práticas Extensionistas IV  
**Situação:** Novo  
**Prioridade:** Alta

**Critério de aceitação:** Processos finalizados deverão possuir uma data de conclusão válida, permitindo calcular o tempo utilizado para sua realização.

---

### RF05 - Pipeline de tratamento de dados

**Descrição:** A solução deverá importar os dados brutos dos processos, realizar tratamento e gerar um dataset organizado para análise.

**Origem:** Práticas Extensionistas IV  
**Situação:** Novo  
**Prioridade:** Alta

**Critério de aceitação:** O pipeline deverá receber um arquivo de dados brutos e gerar um novo arquivo contendo os dados tratados.

---

### RF06 - Identificação de processos atrasados

**Descrição:** A solução deverá identificar os processos que ultrapassaram o prazo previsto.

**Origem:** Práticas Extensionistas IV  
**Situação:** Novo  
**Prioridade:** Alta

**Critério de aceitação:** A base tratada deverá possuir uma informação que permita distinguir processos dentro do prazo e processos atrasados.

---

### RF07 - Geração de indicadores

**Descrição:** A solução deverá calcular indicadores relacionados aos processos e atendimentos.

**Origem:** Práticas Extensionistas IV  
**Situação:** Novo  
**Prioridade:** Média

**Indicadores previstos:**

- Quantidade total de processos;
- Quantidade por tipo de serviço;
- Quantidade por status;
- Processos atrasados;
- Tempo médio de conclusão;
- Origem dos atendimentos.

**Critério de aceitação:** Os indicadores deverão ser calculados utilizando os dados existentes no dataset tratado.

---

### RF08 - Visualização dos dados

**Descrição:** A solução deverá apresentar os principais indicadores por meio de gráficos e visualizações.

**Origem:** Práticas Extensionistas IV  
**Situação:** Novo  
**Prioridade:** Média

**Critério de aceitação:** O usuário deverá conseguir visualizar graficamente pelo menos os principais indicadores dos processos.

---

## 3. Requisitos Não Funcionais

### RNF01 - Usabilidade

**Descrição:** A solução deverá possuir uma interface simples e de fácil compreensão para o usuário.

**Prioridade:** Alta

**Critério de aceitação:** O usuário deverá conseguir identificar os principais indicadores e informações sem necessidade de conhecimento técnico em programação.

---

### RNF02 - Privacidade dos dados

**Descrição:** Dados pessoais de clientes deverão ser protegidos e não poderão ser disponibilizados publicamente no dataset utilizado para análise.

**Prioridade:** Alta

**Critério de aceitação:** Os arquivos publicados no GitHub não deverão conter informações como CPF, telefone ou outros dados pessoais identificáveis.

---

### RNF03 - Desempenho

**Descrição:** O tratamento e a consulta dos dados deverão ocorrer em tempo adequado para utilização na rotina do escritório.

**Prioridade:** Média

**Critério de aceitação:** O pipeline deverá processar a base utilizada no projeto sem apresentar travamentos ou tempo excessivo de execução.

---

### RNF04 - Manutenibilidade

**Descrição:** O código deverá ser organizado e documentado para permitir futuras alterações e melhorias.

**Prioridade:** Média

**Critério de aceitação:** O projeto deverá possuir código organizado, documentação e controle de versões utilizando Git e GitHub.

---

### RNF05 - Reprodutibilidade

**Descrição:** O processo de tratamento e análise deverá poder ser executado novamente utilizando os arquivos e instruções disponibilizados no projeto.

**Prioridade:** Média

**Critério de aceitação:** A execução do notebook ou pipeline com a base de entrada deverá gerar novamente o dataset tratado e os resultados da análise.

---

## 4. Priorização

Para a primeira versão da evolução da solução foram considerados essenciais os requisitos relacionados ao controle dos processos e ao pipeline de dados.

### Prioridade Alta

- RF01 - Cadastro e controle de processos
- RF02 - Controle de documentos e pendências
- RF03 - Controle de prazos e status
- RF04 - Registro da conclusão do processo
- RF05 - Pipeline de tratamento de dados
- RF06 - Identificação de processos atrasados
- RNF01 - Usabilidade
- RNF02 - Privacidade dos dados

### Prioridade Média

- RF07 - Geração de indicadores
- RF08 - Visualização dos dados
- RNF03 - Desempenho
- RNF04 - Manutenibilidade
- RNF05 - Reprodutibilidade

---

## 5. Relação com a evolução da solução

Os requisitos RF01, RF02 e RF03 representam funcionalidades que já faziam parte da proposta desenvolvida em Práticas Extensionistas III.

O RF04 foi acrescentado para melhorar o acompanhamento dos processos e permitir o cálculo do tempo de conclusão.

Os requisitos RF05 até RF08 representam a principal evolução para Práticas Extensionistas IV, pois acrescentam ao sistema recursos relacionados à Engenharia e Ciência de Dados.

Com esses novos requisitos, os dados deixam de ser utilizados somente para registro e passam também a ser tratados, analisados e utilizados para geração de indicadores.
