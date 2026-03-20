# Análise e Previsão de Ações - Ibovespa

Projeto de análise de dados e machine learning utilizando dados históricos do Ibovespa (B3), com foco na construção de um pipeline completo de dados, incluindo ETL, engenharia de features, modelagem preditiva e visualização.

---

## Objetivo

Desenvolver um fluxo completo de dados que permita:

* Processar dados históricos do mercado financeiro
* Criar variáveis relevantes (feature engineering)
* Treinar modelos de machine learning
* Avaliar o desempenho dos modelos
* Gerar dados estruturados para visualização em BI

---

## Tecnologias Utilizadas

* Python
* Pandas
* Scikit-learn
* Matplotlib
* Power BI

---

## Estrutura do Projeto

```bash
ibovespa-ml-analysis/
│
├── data/
│   ├── COTAHIST_AAAA.TXT  # dados brutos da B3
│   └── all_ibovespa.csv   # gerado pelo ETL
│
├── notebooks/
│   └── analise_exploratoria.ipynb
│
├── src/
│   ├── etl_ibovespa.py
│   └── previsao_acoes.py
│
├── resultado_modelo.csv   # gerado pelo modelo
└── README.md
```

---

## Pipeline do Projeto

### 1. ETL

* Leitura dos arquivos COTAHIST da B3
* Extração de colunas por posição fixa
* Conversão de datas e valores
* Consolidação dos dados em um único dataset

Saída: `data/all_ibovespa.csv`

---

### 2. Feature Engineering

Criação de variáveis para melhorar a capacidade preditiva dos modelos:

* Lags (valores de dias anteriores)
* Média móvel de 5 dias
* Média móvel de 21 dias

---

### 3. Modelagem

Foram utilizados dois modelos:

* Regressão Linear
* Rede Neural (MLP - Multi-Layer Perceptron)

---

### 4. Avaliação

Métricas utilizadas:

* R² (coeficiente de determinação)
* MAE (erro médio absoluto)

Resultados obtidos (exemplo):

* Regressão Linear: ~80% de explicação dos dados
* Rede Neural: ~81%

---

### 5. Output

Geração de arquivo CSV contendo:

* Data
* Preço real
* Previsões dos modelos

Saída: `resultado_modelo.csv`

Este arquivo pode ser utilizado no Power BI para visualização.

---

## Visualização

Os dados foram preparados para uso em ferramentas de BI, permitindo:

* Comparação entre valores reais e previstos
* Análise de erro
* Visualização temporal

---

## Como Executar

### 1. Clone o repositório

git clone https://github.com/seu-usuario/ibovespa-ml-analysis.git

cd ibovespa-ml-analysis

---

### 2. Instale as dependências

pip install pandas scikit-learn matplotlib

---

### 3. Baixe os dados

Acesse o site da B3 e baixe os arquivos COTAHIST (anos desejados):

https://www.b3.com.br

Coloque os arquivos dentro da pasta:

data/

---

### 4. Execute o ETL

Este passo irá processar os dados brutos e gerar um dataset consolidado:

python src/etl_ibovespa.py

Arquivo gerado:

data/all_ibovespa.csv

---

### 5. Execute a Modelagem

Agora execute o script de previsão:

python src/previsao_acoes.py

---

### 6. Resultado

Será gerado o arquivo:

resultado_modelo.csv

Esse arquivo pode ser utilizado no Power BI para visualização.

---

## Dados

Os arquivos originais da B3 não estão incluídos no repositório devido ao tamanho.

* Os arquivos `.TXT` devem ser baixados manualmente
* O arquivo `all_ibovespa.csv` é gerado automaticamente pelo ETL

---

## Observações

* O modelo tem finalidade educacional e não deve ser utilizado para decisões financeiras reais
* O mercado financeiro é influenciado por fatores externos não consid
