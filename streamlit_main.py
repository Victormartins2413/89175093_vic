import streamlit as st
from PIL import Image

# Carregar a imagem de fundo
image = Image.open("Cidade_de_Aurora.png")

# Configurar o layout do Streamlit
st.set_page_config(page_title="Aurora's Realm: The Enchanted Adventure", layout="wide")

# Exibir a imagem de fundo
st.image(image, use_column_width=True)

# Centralizar os botões em cima da imagem
col1, col2, col3 = st.columns([1, 2, 1])  # Colunas para centralizar os botões

with col1:
    st.write("")  # espaço vazio

with col2:
    if st.button("Start"):
        st.write("Você clicou em 'Start'!")
        
with col3:
    st.write("")  # espaço vazio

# Adicionar mais botões (Login e Cadastro)
with col1:
    if st.button("Login"):
        st.write("Você clicou em 'Login'!")
        
with col3:
    if st.button("Cadastro"):
        st.write("Você clicou em 'Cadastro'!")
