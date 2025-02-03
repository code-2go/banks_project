# Banks Project - ETL & Data Pipeline

Este projeto implementa um pipeline de Extração, Transformação e Carga (ETL) para processar e armazenar dados sobre as maiores instituições financeiras do mundo. Ele faz a coleta dos dados de um site da web, converte os valores para diferentes moedas e armazena os dados em um banco de dados SQLite.

## Fonte de dados: 
Os dados utilizados neste projeto foram extraídos do [Wikipedia - Largest Banks](https://en.wikipedia.org/wiki/List_of_largest_banks) e de um conjunto de taxas de câmbio disponível neste repositório.

## Objetivo do Projeto
- Extrair dados das maiores instituições financeiras do mundo.
- Aplicar transformações, como conversão de valores para diferentes moedas.
- Armazenar os dados em arquivos **CSV** e um banco de dados **SQLite**.
- Implementar **testes automatizados** para garantir a robustez do pipeline.

## Tecnologias Utilizadas
**Web Scraping:** Requests, BeautifulSoup  
**Manipulação de Dados**: Pandas  
**Armazenamento:** SQLite3  
**Testes:** Unittest, Mock, Tempfile  

## Arquitetura do Projeto

```
banks_project/
├── data/
│   ├── raw/                 - Dados brutos extraídos
│   │   ├── banks_data_raw.csv
│   │   ├── exchange_rate.csv
│   ├── final/               - Dados transformados
│   │   ├── largest_banks.csv
├── db/
│   ├── Banks.db             - Banco de dados SQLite
├── src/                     - Código-fonte do projeto
│   ├── controller/          - Orquestração do pipeline
│   │   ├── main_process.py
│   ├── extract/             - Módulo de extração de dados (web scraping e download de arquivos)
│   ├── load/                - Módulo de carga 
│   ├── tests/               - Testes unitários e mocks
│   ├── transform/           - Módulo de transformação
│   ├── utils/               - Funções auxiliares e log
│   ├── config.py            - Configurações globais
├── README.md
├── requirements.txt         - Dependências do projeto
└── .gitignore               - Arquivos ignorados pelo Git
```

##  Como Executar o Projeto
1. **Clone o repositório**:
   ```bash
   git clone https://github.com/code-2go/banks_project.git
   cd banks_project
   ```
2. **Crie um ambiente virtual e instale as dependências**:
   ```bash
   python -m venv venv
   source venv/bin/activate  - Linux/macOS
   venv\Scripts\activate     - Windows
   pip install -r requirements.txt
   ```
3. **Execute o pipeline ETL**:
   ```bash
   python -m src.controller.main_process
   ```

##  Testes Automatizados
Para garantir a confiabilidade do pipeline, testes unitários foram implementados usando `unittest` , `mock` e `tempfile`. 

Para rodar os testes, utilize:
```bash
python -m unittest discover -s src/tests
```

Os testes cobrem:
- **Extração** de dados (`extract.py`)
- **Download de arquivos CSV** (`download_file`)
- **Transformação** dos dados (`currency_converter`)
- **Carga no banco de dados** (`load_to_database`)

##  Possíveis Melhorias
- Implementar logging estruturado ao invés de `print()`.
- Melhorar a orquestração com alguma ferramenta especifica, como Apache Airflow.
- Adicionar suporte para mais fontes de dados (API, JSON, etc.).

##  Contato e Conexão
Caso tenha alguma sugestão ou feedback, fique à vontade para me chamar no [LinkedIn](https://www.linkedin.com/in/bruno-gurgel-2131362b1/)!
