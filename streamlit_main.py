import streamlit as st
from PIL import Image

# Ligação dos outros arquivos:
from Login import main as login_main
from Cadastro import main as register_main

# Definição da função principal
def main():
    st.set_page_config(page_title="Aurora's Realm: The Enchanted Adventure", page_icon="🧙‍♀️", layout="centered")

    # Carregar e exibir a imagem de fundo
    image = Image.open("Cidade_de_Aurora.png")
    st.image(image, caption="Aurora's Realm: The Enchanted Adventure", use_column_width=True)

    # Adicionar um espaço entre a imagem e o texto
    st.markdown("<br>", unsafe_allow_html=True)

    # Mensagem de boas-vindas
    st.markdown("## Bem-vindo ao Aurora's Realm: The Enchanted Adventure!")

    # Botão "Start"
    if st.button("Start"):
        offer_options()

# Função para oferecer as opções de Login e Cadastro
def offer_options():
    st.markdown("### Escolha uma opção:")

    # Botões para Login e Cadastro
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Login"):
            st.write("Redirecionando para Login...")
            login_main()  # Chamar a função principal do login

    with col2:
        if st.button("Cadastro"):
            st.write("Redirecionando para Cadastro...")
            register_main()  # Chamar a função principal do cadastro

# Executar a função principal se este arquivo for executado
if __name__ == "__main__":
    main()
