import streamlit as st

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
Fique por dentro das últimas atualizações e recursos que estamos implementando. Confira o nosso blog para mais informações.

---

**Eventos**  
Participe dos nossos eventos mensais e ganhe prêmios incríveis! Fique atento às nossas redes sociais para atualizações.

---

**Data do Lançamento do Jogo**  
**Aurora's Realm: The Enchanted Adventure** será lançado no dia **01 de janeiro de 2025**. Prepare-se para a aventura!
""")

# Rodapé
st.markdown("---")
st.markdown("© 2024 Aurora's Realm. Todos os direitos reservados.")
