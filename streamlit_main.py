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

# Criar um espaço para os botões sobre a imagem
st.markdown(
    """
    <style>
    .container {
        position: relative;
        top: -700px; /* Ajuste para posicionar acima da imagem */
        text-align: center;
    }
    .button {
        background-color: white;
        color: black;
        border: none;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Container para os botões
with st.container():
    st.markdown("<div class='container'>", unsafe_allow_html=True)

    # Botão "Start"
    if st.button("Start", key="start_button", help="Clique para começar", css_class='button'):
        # Oferecer opções de login ou cadastro
        option = st.selectbox("Escolha uma opção:", ["Login", "Cadastro"])

        if option == "Login":
            login_main()  # Chamar a função principal do login
        elif option == "Cadastro":
            register_main()  # Chamar a função principal do cadastro

    st.markdown("</div>", unsafe_allow_html=True)  # Fechar o div
