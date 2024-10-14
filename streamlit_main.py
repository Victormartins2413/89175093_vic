import streamlit as st
from PIL import Image

# Importando as funções de login e cadastro
from Login import main as login_main
from Cadastro import main as register_main

# Configuração da página
st.set_page_config(page_title="Aurora's Realm", page_icon="✨")

# Carregar a imagem de fundo
image = Image.open("Cidade_de_Aurora.png")

# Exibir a imagem de fundo
st.image(image, use_column_width=True)

# Usar um contêiner para sobrepor os botões na imagem
with st.container():
    # Criar um espaço para os botões
    st.markdown("<div style='position: relative; top: -600px;'>", unsafe_allow_html=True)
    
    # Botão "Start"
    if st.button("Start"):
        # Oferecer opções de login ou cadastro
        option = st.selectbox("Escolha uma opção:", ["Login", "Cadastro"])

        if option == "Login":
            login_main()  # Chamar a função principal do login
        elif option == "Cadastro":
            register_main()  # Chamar a função principal do cadastro

    st.markdown("</div>", unsafe_allow_html=True)  # Fechar o div

# Se precisar de mais espaço na página, você pode adicionar
st.write("<br><br><br>", unsafe_allow_html=True)  # Mais espaços em branco
