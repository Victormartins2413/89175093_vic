import streamlit as st

# Configuração da página
st.set_page_config(page_title="Aurora's Realm: The Enchanted Adventure", layout="wide")

# Estilo CSS personalizado para o vídeo de fundo e a aparência geral
st.markdown(
    """
    <style>
    .stApp {
        background-color: black;  /* Fundo preto para contraste com o vídeo */
        color: white;
    }

    /* Estilo dos botões de navegação horizontais */
    .menu-container {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-bottom: 30px;
    }

    .menu-btn {
        background-color: #1E90FF;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        text-decoration: none;
        transition: background-color 0.3s;
    }

    .menu-btn:hover {
        background-color: #00BFFF;
    }

    /* Estilo para o vídeo */
    .video-bg {
        position: fixed;
        top: 0;
        left: 0;
        min-width: 100%;
        min-height: 100%;
        z-index: -1;
        opacity: 0.6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Adicionando o vídeo de fundo no loop
st.markdown(
    """
    <video autoplay loop muted playsinline class="video-bg">
        <source src="Vídeo_de_entrada.mp4" type="video/mp4">
    </video>
    """,
    unsafe_allow_html=True
)

# Barra de navegação em linha (menu horizontal)
st.markdown("<div class='menu-container'>", unsafe_allow_html=True)

# Botões de navegação
btn1 = st.button("Home")
btn2 = st.button("Quem somos")
btn3 = st.button("Downloads")
btn4 = st.button("Novidades")
btn5 = st.button("Eventos")
btn6 = st.button("Lançamento")

st.markdown("</div>", unsafe_allow_html=True)

# Exibindo o conteúdo com base no botão clicado
if btn1:
    st.title("Bem-vindo ao Aurora's Realm: The Enchanted Adventure")
    st.write("""
    Aurora's Realm é um mundo mágico onde heróis exploram terras encantadas e enfrentam desafios épicos. 
    Fique atento para atualizações diárias sobre o desenvolvimento e novas funcionalidades.
    """)

elif btn2:
    st.title("Quem somos?")
    st.write("""
    Nós somos uma equipe de desenvolvedores apaixonados por criar experiências imersivas. 
    Nosso objetivo é proporcionar um jogo que inspire, desafie e entretenha jogadores de todas as idades.
    """)

elif btn3:
    st.title("Downloads do Jogo")
    st.write("""
    O lançamento do jogo ocorrerá em **junho de 2025**. Fique de olho nas novidades e, em breve, 
    o download estará disponível!
    """)

elif btn4:
    st.title("Novidades do Jogo")
    st.write("""
    Últimas notícias sobre o desenvolvimento de Aurora's Realm:  
    - Novos recursos e mecânicas implementadas.
    - Testes beta fechados em andamento.
    """)

elif btn5:
    st.title("Eventos")
    st.write("""
    Participe de eventos únicos dentro do jogo! Desafie seus amigos e conquiste prêmios incríveis. 
    Confira nossa agenda de eventos nas redes sociais.
    """)

elif btn6:
    st.title("Data de Lançamento")
    st.write("""
    **Aurora's Realm: The Enchanted Adventure** será lançado oficialmente em **junho de 2025**.
    Prepare-se para uma aventura incrível!
    """)

# Barra lateral de login/cadastro
with st.sidebar:
    st.header("Entrar ou Cadastrar")
    login = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    
    if st.button("Entrar"):
        st.success("Login realizado com sucesso!")
    if st.button("Cadastrar"):
        st.success("Cadastro realizado com sucesso!")

# Rodapé
st.markdown("---")
st.markdown("© 2024 Aurora's Realm. Todos os direitos reservados.")
