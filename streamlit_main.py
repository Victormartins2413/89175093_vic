import streamlit as st
from datetime import datetime

# Definindo o título da página
st.set_page_config(page_title="Aurora's Realm: The Enchanted Adventure", layout="wide")

# Definindo o CSS para estilizar a página
st.markdown(
    """
    <style>
    /* Estilo da página */
    .stApp {
        background-image: url("https://via.placeholder.com/1600x900");  /* Substitua pela URL da imagem do seu jogo */
        background-size: cover;
        background-position: center;
        color: white;
        padding: 20px;
    }

    /* Estilizando os cabeçalhos */
    h1, h2 {
        font-family: 'Arial', sans-serif;
        text-align: center;
        margin-bottom: 20px;
    }

    /* Estilizando o botão */
    .button {
        display: block;
        width: 100%;
        padding: 10px;
        margin: 10px 0;
        background-color: #1E90FF;  /* Cor do botão */
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }

    .button:hover {
        background-color: #00BFFF;  /* Cor do botão ao passar o mouse */
    }

    /* Estilo da barra lateral */
    .sidebar .sidebar-content {
        background-color: rgba(0, 0, 0, 0.5);
        padding: 20px;
        border-radius: 10px;
    }

    /* Estilo do vídeo */
    .video-container {
        text-align: center;
        margin-bottom: 20px;
    }
    
    /* Estilo do contador */
    .counter {
        font-size: 24px;
        text-align: center;
        margin-top: 20px;
        color: #FFD700; /* Cor dourada */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Criando uma barra lateral para login e cadastro
with st.sidebar:
    st.header("Entrar ou Cadastrar")
    login = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    
    if st.button("Entrar", key='login_button'):
        st.success("Login realizado com sucesso!")  # Lógica de autenticação pode ser adicionada
    if st.button("Cadastrar", key='register_button'):
        st.success("Cadastro realizado com sucesso!")  # Lógica de cadastro pode ser adicionada

# Adicionando o vídeo em loop
st.markdown(
    """
    <div class='video-container'>
        <video autoplay loop muted playsinline style="width: 100%; height: auto;">
            <source src="Vídeo_de_entrada.mp4" type="video/mp4">  <!-- Certifique-se de que o vídeo esteja no mesmo diretório que seu script -->
            Seu navegador não suporta o vídeo.
        </video>
    </div>
    """,
    unsafe_allow_html=True
)

# Adicionando informações sobre o jogo
st.title("Aurora's Realm: The Enchanted Adventure")
st.markdown("""
**Quem somos?**  
Nós somos uma equipe de desenvolvedores dedicados a criar experiências de jogo emocionantes. 
Nosso objetivo é proporcionar aos jogadores um ambiente imersivo e divertido.

---

**Downloads do Jogo**  
Faça o download do nosso jogo [aqui](https://exemplo.com/download) e junte-se à aventura!

---

**Novidades do Jogo**  
Estamos empolgados para anunciar que **Aurora's Realm: The Enchanted Adventure** será lançado em **junho de 2025**! 
Fique atento às atualizações para mais informações.

---

**Contagem Regressiva até o Lançamento**  
""")

# Contador regressivo
launch_date = datetime(2025, 6, 30)  # Data de lançamento
today = datetime.now()  # Data atual
time_remaining = launch_date - today  # Cálculo do tempo restante

# Exibir tempo restante
st.markdown(f"<div class='counter'>Faltam {time_remaining.days} dias até o lançamento!</div>", unsafe_allow_html=True)

# Eventos
st.markdown("""
**Eventos**  
Participe dos nossos eventos mensais e ganhe prêmios incríveis! Fique atento às nossas redes sociais para atualizações.
""")

# Rodapé
st.markdown("---")
st.markdown("© 2024 Aurora's Realm. Todos os direitos reservados.")
