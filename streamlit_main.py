import streamlit as st
from PIL import Image
import sys

# Ligação dos outros arquivos:
from Login import main as login_main
from Cadastro import main as register_main

# Definição da função principal
def main():
    st.set_page_config(page_title="Aurora's Realm: The Enchanted Adventure", page_icon="🧙‍♀️", layout="centered")

    # Exibir a imagem da tela de entrada
    image = Image.open("Cidade_de_Aurora.png")
    st.image(image, caption="Aurora's Realm: The Enchanted Adventure", use_column_width=True)

    st.markdown("## Bem-vindo ao Aurora's Realm: The Enchanted Adventure!")

    # Botão Start
    start_button = st.button("Start")

    # Quando o botão "Start" for clicado
    if start_button:
        offer_options()

# Função para oferecer as opções de Login e Cadastro
def offer_options():
    st.markdown("### Escolha uma opção:")

    # Botões para Login e Cadastro
    col1, col2 = st.columns(2)

    with col1:
        login_button = st.button("Login")

    with col2:
        register_button = st.button("Cadastro")

    # Verificar qual botão foi clicado
    if login_button:
        st.write("Redirecionando para Login...")
        login_main()  # Chamar a função principal do login

    if register_button:
        st.write("Redirecionando para Cadastro...")
        register_main()  # Chamar a função principal do cadastro

# Executar a função principal se este arquivo for executado
if __name__ == "__main__":
    main()
