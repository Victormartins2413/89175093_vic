import streamlit as st
from PIL import Image

# Importando as funções de login e cadastro
from Login import main as login_main
from Cadastro import main as register_main

# Título da página
st.title("Aurora's Realm: The Enchanted Adventure")

# Carregar e exibir a imagem de fundo
image = Image.open("Cidade_de_Aurora.png")
st.image(image, use_column_width=True)

# Criar um espaço em branco para dar espaço aos botões
st.write("<br>", unsafe_allow_html=True)  # Usando HTML para criar espaço

# Botão "Start"
if st.button("Start"):
    # Oferecer opções de login ou cadastro
    option = st.selectbox("Escolha uma opção:", ["Login", "Cadastro"])

    if option == "Login":
        login_main()  # Chamar a função principal do login
    elif option == "Cadastro":
        register_main()  # Chamar a função principal do cadastro

# Se precisar de mais espaço na página, você pode adicionar
st.write("<br><br><br>", unsafe_allow_html=True)  # Mais espaços em branco
