import streamlit as st
import sqlite3
from PIL import Image

# Caminho completo para o arquivo do banco de dados
caminho_banco_de_dados = r'cadastro.db'

# Função para verificar login no banco de dados
def login(username, password):
    conn = sqlite3.connect(caminho_banco_de_dados)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cadastro WHERE nome=? AND senha=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    if user:
        return True
    else:
        return False

# Função principal
def main():
    st.set_page_config(page_title="Login Aurora's Realm", page_icon="🧙‍♀️")

    # Exibir imagem
    image = Image.open("Imagens/Aurora-1.png")
    st.image(image, caption="Aurora's Realm: The Enchanted Adventure", use_column_width=True)

    st.title("Login")

    # Campos para nome de usuário e senha
    username = st.text_input("Nome de usuário:")
    password = st.text_input("Senha:", type="password")

    # Botões de Login e Voltar
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Login"):
            if login(username, password):
                st.success("Login bem-sucedido!")
                # Aqui você pode redirecionar ou carregar a página do jogo
                st.write("Carregando o jogo...")
                # Jogo.main()  # Como não podemos carregar o jogo do Pygame, você poderia redirecionar para outra página no Streamlit.
            else:
                st.error("Dados inválidos.")

    with col2:
        if st.button("Voltar"):
            st.write("Redirecionando para a página principal...")
            # Aqui você pode redirecionar para outra página ou funcionalidade principal.
            # Exemplo: os.system("python main.py")

# Chamar a função principal
if __name__ == "__main__":
    main()
