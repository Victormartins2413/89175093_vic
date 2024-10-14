import streamlit as st
from PIL import Image

# Carregar a imagem de fundo
image = Image.open("Cidade_de_Aurora.png")

# Configurar o layout do Streamlit
st.set_page_config(page_title="Aurora's Realm: The Enchanted Adventure", layout="centered")

# Criar uma seção de estilo para o CSS
st.markdown(
    """
    <style>
        .image-container {
            position: relative;
            text-align: center;
        }
        .overlay {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
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

# Criar um contêiner para a imagem
with st.container():
    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    st.image(image, use_column_width=True)

    # Criar uma variável de sessão para controlar a visibilidade dos botões
    if 'show_buttons' not in st.session_state:
        st.session_state.show_buttons = False

    # Adicionar o botão "Start" em cima da imagem
    st.markdown('<div class="overlay">', unsafe_allow_html=True)
    if st.button("Start", key="start", help="Clique para começar"):
        st.session_state.show_buttons = True
        st.write("Você clicou em 'Start'!")

    st.markdown('</div>', unsafe_allow_html=True)

    # Exibir os botões "Login" e "Cadastro" apenas se "Start" for clicado
    if st.session_state.show_buttons:
        st.markdown('<div class="overlay">', unsafe_allow_html=True)
        if st.button("Login", key="login", help="Clique para fazer login"):
            st.write("Você clicou em 'Login'!")

        if st.button("Cadastro", key="cadastro", help="Clique para se cadastrar"):
            st.write("Você clicou em 'Cadastro'!")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
