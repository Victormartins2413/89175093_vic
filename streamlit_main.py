import streamlit as st
from PIL import Image

# Ligação dos outros arquivos
from Login import main as login_main
from Cadastro import main as register_main

# Definição da função principal
def main():
    st.set_page_config(page_title="Aurora's Realm: The Enchanted Adventure", page_icon="🧙‍♀️", layout="centered")

    # Carregar a imagem da tela de entrada
    image = Image.open("Cidade_de_Aurora.png")

    # Definir um fator de escala
    scale_factor = 1.5
    scaled_width = int(image.width * scale_factor)
    scaled_height = int(image.height * scale_factor)
    image = image.resize((scaled_width, scaled_height))

    # Exibir a imagem como fundo
    st.image(image, caption="Aurora's Realm: The Enchanted Adventure", use_column_width='always')

    # Título
    st.markdown("<h2 style='text-align: center; color: white;'>Bem-vindo ao Aurora's Realm: The Enchanted Adventure!</h2>", unsafe_allow_html=True)

    # Botão Start
    start_button = st.button("Start")

    # Quando o botão "Start" for clicado
    if start_button:
        offer_options()

# Função para oferecer as opções de Login e Cadastro
def offer_options():
    st.markdown("<h3 style='text-align: center; color: white;'>Escolha uma opção:</h3>", unsafe_allow_html=True)

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
