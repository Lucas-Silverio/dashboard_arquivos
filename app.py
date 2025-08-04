import streamlit as st
import pandas as pd
from analisar_arquivos import coletar_dados_dir
from utils import selecionar_pasta

st.set_page_config(page_title="Analisador de arquivos", layout="wide")

st.title("📊 Dashboard de Arquivos Locais")

if 'pasta_selecionada' not in st.session_state:
    st.session_state['pasta_selecionada'] = ""

if st.button("📁 Selecionar pasta"):
    st.session_state['pasta_selecionada'] = selecionar_pasta()

#pasta = st.text_input("📁 Caminho da pasta a ser analisada: ", value=".")
if st.session_state['pasta_selecionada']:
    st.success(f'Pasta selecionada: {st.session_state["pasta_selecionada"]}')
    if st.button("🔍 Analisar"):
        with st.spinner("Coletando dados..."):
            dados = coletar_dados_dir(st.session_state['pasta_selecionada'])

            if not dados:
                st.warning("Nenhum arquivo encontrado.")
            else:
                df = pd.DataFrame(dados)

                st.success(f"{len(df)} arquivos encontrados!")

                st.subheader("🔝 Top 10 arquivos maiores")
                st.dataframe(df.sort_values(by="tamanho_MB", ascending=False).head(10))

                st.subheader("📦 Total de arquivos por extensão")
                extensoes = df['extensao'].value_counts().reset_index()
                extensoes.columns = ['Extensão', 'Quantidade']
                st.bar_chart(extensoes.set_index('Extensão'))

                st.subheader("💾 Tamanho total por extensão (MB)")
                tamanho_por_extensao = df.groupby('extensao')['tamanho_MB'].sum().sort_values(ascending=False)
                st.bar_chart(tamanho_por_extensao)

                st.subheader("📜 Arquivos mais antigos")
                st.dataframe(df.sort_values(by='criado_em').head(5))

                st.subheader("📤 Exportar dados")
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button("⬇️ Baixar CSV", csv, "dados_arquivos.csv", "text/csv")
else:
    st.info("Selecione uma pasta para iniciar a análise.")