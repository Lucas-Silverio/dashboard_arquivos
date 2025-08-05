# 📊 Analisador de Arquivos Locais

Este projeto foi desenvolvido com o objetivo de **treinar habilidades em Engenharia de Dados** utilizando Python e Streamlit. A aplicação permite ao usuário **selecionar uma pasta local**, e então realiza uma **análise automatizada dos arquivos contidos nessa pasta**, apresentando estatísticas e visualizações úteis.

---

## 🎯 Objetivo

Criar uma ferramenta simples de análise de arquivos locais como forma de exercitar conceitos fundamentais de Engenharia de Dados, como:

- Coleta de metadados de arquivos
- Manipulação e limpeza de dados com `pandas`
- Uso de bibliotecas nativas como `os`, `pathlib` e `tkinter`
- Geração de visualizações com `Streamlit`
- Exportação de dados para formatos reutilizáveis (CSV)

---

## ✅ Funcionalidades

- 📁 Seleção de pasta via interface gráfica
- 🔎 Leitura recursiva de todos os arquivos na pasta e subpastas
- 📊 Exibição de:
  - Top 10 maiores arquivos
  - Quantidade de arquivos por extensão
  - Tamanho total por extensão
  - Arquivos mais antigos
- 📤 Exportação dos dados analisados em CSV

---

## 🧠 Pontos importantes no código

### 🔹 `tkinter` para seleção de pasta
A função `selecionar_pasta()` utiliza a interface gráfica do sistema para facilitar a escolha de diretórios sem necessidade de digitação.

### 🔹 `pandas` para estruturação dos dados
Os dados coletados são organizados em um `DataFrame`, facilitando análises e visualizações.

### 🔹 `Streamlit` para visualização
Toda a interface interativa é construída com `Streamlit`, possibilitando:
- Interface web local
- Visualização de gráficos de barra
- Tabelas dinâmicas
- Download dos dados analisados

---

## 🚀 Como Executar

### 1. Clone o repositório

```bash

git clone https://github.com/Lucas-Silverio/dashboard_arquivos.git
cd dashboard_arquivos

```
### 2. Instale as dependências
```

pip install -r requirements.txt

```
### 3. Execute o projeto
```

streamlit run app.py

```
