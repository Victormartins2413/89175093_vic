import streamlit as st
from PIL import Image

# Ligação dos outros arquivos
from Login import main as login_main
from Cadastro import main as register_main

# Função principal
def main():
    # Configurações da página
    st.set_page_config(page_title="Aurora's Realm: The Enchanted Adventure", page_icon="🧙‍♀️", layout="centered")

    # Carregar a imagem de fundo
    image = Image.open("Cidade_de_Aurora.png")
    st.image(image, use_column_width=True, caption="")  # Imagem de fundo

    # Adicionar um espaço entre a imagem e o texto
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Mensagem de boas-vindas centralizada
    st.markdown("<h1 style='text-align: center; color: white;'>Bem-vindo ao Aurora's Realm: The Enchanted Adventure!</h1>", unsafe_allow_html=True)

    # Botão "Start" centralizado
    if st.button("Start", key="start_button"):
        offer_options()

# Função para oferecer as opções de Login e Cadastro
def offer_options():
    st.markdown("<h2 style='text-align: center; color: white;'>Escolha uma opção:</h2>", unsafe_allow_html=True)

    # Botões para Login e Cadastro em colunas
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Login"):
            login_main()  # Chamar a função principal do login

    with col2:
        if st.button("Cadastro"):
            register_main()  # Chamar a função principal do cadastro

# Executar a função principal se este arquivo for executado
if __name__ == "__main__":
    main()
