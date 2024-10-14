import streamlit as st
from PIL import Image

# Funções de login e cadastro
def login():
    st.write("Login page")
    # Aqui você pode adicionar o código para a página de login.

def register():
    st.write("Register page")
    # Aqui você pode adicionar o código para a página de cadastro.

# Configuração da página
st.set_page_config(page_title="Aurora's Realm: The Enchanted Adventure", layout="wide")

# Carregar a imagem de fundo
background_image = Image.open("Cidade_de_Aurora.png")

# Exibir a imagem de fundo
st.image(background_image, use_column_width=True)

# Adicionar um título sobre a imagem
st.markdown(
    """
    <h1 style='text-align: center; color: white;'>Aurora's Realm: The Enchanted Adventure</h1>
    """, unsafe_allow_html=True
)

# Botões para Login e Cadastro
col1, col2 = st.columns(2)

with col1:
    if st.button("Login"):
        login()  # Chamar a função de login

with col2:
    if st.button("Cadastro"):
        register()  # Chamar a função de cadastro

# Adicionar espaço extra para os botões estarem centralizados verticalmente
st.write("<br>" * 10, unsafe_allow_html=True)
