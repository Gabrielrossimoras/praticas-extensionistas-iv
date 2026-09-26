# Diagrama Entidade-Relacionamento (DER)

O Diagrama Entidade-Relacionamento representa a estrutura dos principais dados utilizados pelo Sistema Inteligente de Controle e Análise de Processos para Despachante.

O modelo mantém a estrutura desenvolvida em Práticas Extensionistas III e acrescenta informações necessárias para a evolução da solução em Práticas Extensionistas IV.

```mermaid
erDiagram

    CLIENTE ||--o{ VEICULO : possui
    VEICULO ||--o{ PROCESSO : possui
    SERVICO ||--o{ PROCESSO : classifica
    STATUS ||--o{ PROCESSO : define
    ORIGEM ||--o{ PROCESSO : identifica
    PROCESSO ||--o{ DOCUMENTO : possui

    CLIENTE {
        int id_cliente PK
        string nome
        string cpf_cnpj
        string telefone
        string email
    }

    VEICULO {
        int id_veiculo PK
        int id_cliente FK
        string placa
        string marca
        string modelo
        int ano
    }

    PROCESSO {
        int id_processo PK
        int id_veiculo FK
        int id_servico FK
        int id_status FK
        int id_origem FK
        date data_abertura
        date prazo
        date data_conclusao
        string observacao
    }

    SERVICO {
        int id_servico PK
        string descricao
    }

    STATUS {
        int id_status PK
        string descricao
    }

    ORIGEM {
        int id_origem PK
        string descricao
    }

    DOCUMENTO {
        int id_documento PK
        int id_processo FK
        string descricao
        string situacao
    }
```

## Principais relacionamentos

- Um cliente pode possuir vários veículos;
- Um veículo pode possuir vários processos;
- Cada processo está relacionado a um tipo de serviço;
- Cada processo possui um status;
- Cada processo possui uma origem de atendimento;
- Um processo pode possuir vários documentos.

## Evolução do modelo

A principal alteração em relação ao projeto anterior é a inclusão da informação `data_conclusao` na entidade PROCESSO.

Essa informação permitirá comparar a data de abertura, o prazo previsto e a data efetiva de conclusão do processo.

Com isso será possível calcular indicadores como:

- Tempo médio de conclusão dos processos;
- Quantidade de processos concluídos;
- Quantidade de processos atrasados;
- Tempo utilizado por tipo de serviço;
- Comparação entre prazo previsto e conclusão.

## Privacidade dos dados

Embora o modelo possua informações pessoais necessárias para a operação do sistema, como nome, CPF/CNPJ, telefone e e-mail, esses dados não serão disponibilizados nos datasets públicos utilizados para análise.

Para as etapas de Ciência de Dados serão utilizados somente os dados necessários para geração dos indicadores, respeitando a privacidade das informações dos clientes.
