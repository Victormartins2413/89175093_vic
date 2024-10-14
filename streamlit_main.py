import streamlit as st
from PIL import Image

# Carregar a imagem de fundo
image = Image.open("Cidade_de_Aurora.png")

# Configurar o layout do Streamlit
st.set_page_config(page_title="Aurora's Realm: The Enchanted Adventure", layout="centered")

# Exibir a imagem de fundo
st.image(image, use_column_width=True)

# Criar uma seção de estilo para o CSS
st.markdown(
    """
    <style>
        .overlay {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
        }
        .btn {
            margin: 10px;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Criar um contêiner para sobrepor os botões
st.markdown('<div class="overlay">', unsafe_allow_html=True)

# Adicionar os botões
if st.button("Login", key="login", help="Clique para fazer login"):
    st.write("Você clicou em 'Login'!")

if st.button("Start", key="start", help="Clique para começar"):
    st.write("Você clicou em 'Start'!")

if st.button("Cadastro", key="cadastro", help="Clique para se cadastrar"):
    st.write("Você clicou em 'Cadastro'!")

st.markdown('</div>', unsafe_allow_html=True)
