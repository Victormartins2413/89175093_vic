import streamlit as st
from PIL import Image

# Carregar a imagem de fundo
image = Image.open("Cidade_de_Aurora.png")

# Configurar o layout do Streamlit
st.set_page_config(page_title="Aurora's Realm: The Enchanted Adventure", layout="wide")

# Exibir a imagem de fundo
st.image(image, use_column_width=True)

# Criar um contêiner para sobrepor os botões
with st.container():
    st.markdown("<h1 style='text-align: center; color: white;'>Bem-vindo ao Reino de Aurora</h1>", unsafe_allow_html=True)

    # Criar uma linha com três colunas
    col1, col2, col3 = st.columns(3)

    # Adicionar botões nas colunas
    with col1:
        if st.button("Login"):
            st.write("Você clicou em 'Login'!")

    with col2:
        if st.button("Start"):
            st.write("Você clicou em 'Start'!")

    with col3:
        if st.button("Cadastro"):
            st.write("Você clicou em 'Cadastro'!")
