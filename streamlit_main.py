import streamlit as st

# Configuração da página
st.set_page_config(page_title="Aurora's Realm: The Enchanted Adventure", layout="wide")

# Estilo CSS personalizado para o vídeo de fundo, botões no topo e aparência geral
st.markdown(
    """
    <style>
    .stApp {
        background-color: black;  /* Fundo preto para contraste com o vídeo */
        color: white;
    }

    /* Estilo para o vídeo de fundo */
    .video-bg {
        position: fixed;
        top: 0;
        left: 0;
        min-width: 100%;
        min-height: 100%;
        z-index: -1;
        opacity: 0.6;
    }

    /* Estilo da barra de navegação */
    .nav-bar {
        display: flex;
        justify-content: space-evenly;
        position: fixed;
        top: 0;
        width: 100%;
        background-color: rgba(0, 0, 0, 0.7);
        padding: 10px 0;
        z-index: 999;
    }

    .nav-btn {
        background-color: #1E90FF;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        text-decoration: none;
        transition: background-color 0.3s;
    }

    .nav-btn:hover {
        background-color: #00BFFF;
    }

    /* Adiciona um padding no topo da página para que o conteúdo não fique atrás da barra */
    .content {
        padding-top: 70px;
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

# Barra de navegação no topo
st.markdown("""
<div class="nav-bar">
    <a href="#home" class="nav-btn">Home</a>
    <a href="#quem-somos" class="nav-btn">Quem somos</a>
    <a href="#downloads" class="nav-btn">Downloads</a>
    <a href="#novidades" class="nav-btn">Novidades</a>
    <a href="#eventos" class="nav-btn">Eventos</a>
    <a href="#lancamento" class="nav-btn">Lançamento</a>
</div>
""", unsafe_allow_html=True)

# Conteúdo do site
st.markdown('<div class="content">', unsafe_allow_html=True)

# Home
st.markdown('<a id="home"></a>', unsafe_allow_html=True)
st.title("Bem-vindo ao Aurora's Realm: The Enchanted Adventure")
st.write("""
Aurora's Realm é um mundo mágico onde heróis exploram terras encantadas e enfrentam desafios épicos. 
Fique atento para atualizações diárias sobre o desenvolvimento e novas funcionalidades.
""")

# Quem somos
st.markdown('<a id="quem-somos"></a>', unsafe_allow_html=True)
st.title("Quem somos?")
st.write("""
Nós somos uma equipe de desenvolvedores apaixonados por criar experiências imersivas. 
Nosso objetivo é proporcionar um jogo que inspire, desafie e entretenha jogadores de todas as idades.
""")

# Downloads
st.markdown('<a id="downloads"></a>', unsafe_allow_html=True)
st.title("Downloads do Jogo")
st.write("""
O lançamento do jogo ocorrerá em **junho de 2025**. Fique de olho nas novidades e, em breve, 
o download estará disponível!
""")

# Novidades
st.markdown('<a id="novidades"></a>', unsafe_allow_html=True)
st.title("Novidades do Jogo")
st.write("""
Últimas notícias sobre o desenvolvimento de Aurora's Realm:  
- Novos recursos e mecânicas implementadas.
- Testes beta fechados em andamento.
""")

# Eventos
st.markdown('<a id="eventos"></a>', unsafe_allow_html=True)
st.title("Eventos")
st.write("""
Participe de eventos únicos dentro do jogo! Desafie seus amigos e conquiste prêmios incríveis. 
Confira nossa agenda de eventos nas redes sociais.
""")

# Lançamento
st.markdown('<a id="lancamento"></a>', unsafe_allow_html=True)
st.title("Data de Lançamento")
st.write("""
**Aurora's Realm: The Enchanted Adventure** será lançado oficialmente em **junho de 2025**.
Prepare-se para uma aventura incrível!
""")

st.markdown('</div>', unsafe_allow_html=True)

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
