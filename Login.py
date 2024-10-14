import streamlit as st
import sqlite3

# Caminho completo para o arquivo do banco de dados (ajuste conforme necessário)
caminho_banco_de_dados = r'cadastro.db'

# Função para processar o login
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
    st.title("Login")

    # Carregar a imagem (assumindo que a imagem está no mesmo diretório que o script)
    st.image("Aurora-1.png", width=300)  # Caminho relativo para a imagem

    # Entradas para o nome de usuário e senha
    username = st.text_input("Nome de Usuário")
    password = st.text_input("Senha", type="password")

    # Botão de login
    if st.button("Login"):
        if login(username, password):
            st.success("Login bem-sucedido!")
            st.write("Bem-vindo, ", username)
            # A função Jogo.main() seria chamada aqui, substitua pela lógica do jogo
        else:
            st.error("Nome de usuário ou senha incorretos.")

    # Botão de voltar
    if st.button("Voltar"):
        st.write("Retornando à página principal...")
        # Aqui você pode redirecionar para outra página, se necessário

# Executa a função principal
if __name__ == "__main__":
    main()
