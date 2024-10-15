import streamlit as st

# Configuração da página
st.set_page_config(page_title="Aurora's Realm: The Enchanted Adventure", layout="wide")

# Estilo CSS personalizado para a imagem de fundo e a aparência geral
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://via.placeholder.com/1600x900");  /* Substitua pela URL da sua imagem de fundo */
        background-size: cover;
        background-position: center;
        color: white;
        height: 100vh;
    }

    /* Estilo dos botões de navegação */
    .navigation-buttons {
        display: flex;
        justify-content: center;
        margin-bottom: 30px;
    }

    .nav-btn {
        background-color: #1E90FF;
        color: white;
        padding: 10px 20px;
        margin: 5px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        text-decoration: none;
    }

    .nav-btn:hover {
        background-color: #00BFFF;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Barra lateral de login/cadastro
with st.sidebar:
    st.header("Entrar ou Cadastrar")
    login = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    
    if st.button("Entrar"):
        st.success("Login realizado com sucesso!")
    if st.button("Cadastrar"):
        st.success("Cadastro realizado com sucesso!")

# Definindo navegação com opções de diferentes seções
st.markdown("<div class='navigation-buttons'>", unsafe_allow_html=True)
section = st.radio("Navegação", ["Home", "Quem somos", "Downloads", "Novidades", "Eventos", "Data de Lançamento", "Entrar"])
st.markdown("</div>", unsafe_allow_html=True)

# Conteúdo das páginas
if section == "Home":
    st.title("Bem-vindo ao Aurora's Realm: The Enchanted Adventure")
    st.write("""
    Aurora's Realm é um mundo mágico onde heróis exploram terras encantadas e enfrentam desafios épicos. 
    Fique atento para atualizações diárias sobre o desenvolvimento e novas funcionalidades.
    """)

elif section == "Quem somos":
    st.title("Quem somos?")
    st.write("""
    Nós somos uma equipe de desenvolvedores apaixonados por criar experiências imersivas. 
    Nosso objetivo é proporcionar um jogo que inspire, desafie e entretenha jogadores de todas as idades.
    """)

elif section == "Downloads":
    st.title("Downloads do Jogo")
    st.write("""
    O lançamento do jogo ocorrerá em **junho de 2025**. Fique de olho nas novidades e, em breve, 
    o download estará disponível!
    """)

elif section == "Novidades":
    st.title("Novidades do Jogo")
    st.write("""
    Últimas notícias sobre o desenvolvimento de Aurora's Realm:  
    - Novos recursos e mecânicas implementadas.
    - Testes beta fechados em andamento.
    """)

elif section == "Eventos":
    st.title("Eventos")
    st.write("""
    Participe de eventos únicos dentro do jogo! Desafie seus amigos e conquiste prêmios incríveis. 
    Confira nossa agenda de eventos nas redes sociais.
    """)

elif section == "Data de Lançamento":
    st.title("Data de Lançamento")
    st.write("""
    **Aurora's Realm: The Enchanted Adventure** será lançado oficialmente em **junho de 2025**.
    Prepare-se para uma aventura incrível!
    """)

elif section == "Entrar":
    st.title("Entrar")
    st.write("Faça login ou registre-se para acessar conteúdos exclusivos do site e do jogo.")

# Rodapé
st.markdown("---")
st.markdown("© 2024 Aurora's Realm. Todos os direitos reservados.")
