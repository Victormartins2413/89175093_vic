import streamlit as st

# Definindo o título da página
st.set_page_config(page_title="Aurora's Realm: The Enchanted Adventure", layout="wide")

# Definindo a imagem de fundo
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://via.placeholder.com/1600x900");  /* Insira a URL da sua imagem de fundo */
        background-size: cover;
        background-position: center;
        height: 100vh;
        color: white;
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
    
    if st.button("Entrar"):
        st.success("Login realizado com sucesso!")  # Aqui você pode adicionar a lógica de autenticação
    if st.button("Cadastrar"):
        st.success("Cadastro realizado com sucesso!")  # Aqui você pode adicionar a lógica de cadastro

# Adicionando informações sobre o jogo
st.title("Bem-vindo ao Aurora's Realm: The Enchanted Adventure")
st.write("""
Nós somos uma equipe de desenvolvedores dedicados a criar experiências de jogo emocionantes. 
Nosso objetivo é proporcionar aos jogadores um ambiente imersivo e divertido.
""")

st.title("Downloads do Jogo")
st.write("""
Faça o download do nosso jogo **Aurora's Realm** [aqui](https://exemplo.com/download) e junte-se à aventura!
""")

st.title("Novidades do Jogo")
st.write("""
Fique por dentro das últimas atualizações e recursos que estamos implementando.
Confira o nosso blog para mais informações.
""")

st.title("Eventos")
st.write("""
Participe dos nossos eventos mensais e ganhe prêmios incríveis! 
Fique atento às nossas redes sociais para atualizações.
""")

st.title("Data do Lançamento do Jogo")
st.write("""
**Aurora's Realm: The Enchanted Adventure** será lançado no dia **01 de janeiro de 2025**. 
Prepare-se para a aventura!
""")

# Rodapé
st.markdown("---")
st.markdown("© 2024 Aurora's Realm. Todos os direitos reservados.")
