import sqlite3
import streamlit as st

# Função para inserir os dados no banco de dados
def inserir_dados(nome, idade, altura, peso, senha, email):
    conn = sqlite3.connect('cadastro.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO cadastro (nome, idade, altura, peso, senha, email) VALUES (?, ?, ?, ?, ?, ?)''',
                   (nome, idade, altura, peso, senha, email))
    conn.commit()
    conn.close()

# Função de cadastro no Streamlit
def main():
    st.title("Cadastro de Usuário")
    
    # Campos do formulário
    nome = st.text_input("Nome")
    idade = st.number_input("Idade", min_value=0, max_value=120, step=1)
    altura = st.number_input("Altura (cm)", min_value=0.0, step=0.1)
    peso = st.number_input("Peso (kg)", min_value=0.0, step=0.1)
    senha = st.text_input("Senha", type="password")
    email = st.text_input("Gmail ou E-mail")
    
    # Botão de cadastro
    if st.button("Cadastrar"):
        if nome and idade and altura and peso and senha and email:
            inserir_dados(nome, idade, altura, peso, senha, email)
            st.success("Cadastro realizado com sucesso!")
        else:
            st.error("Preencha todos os campos.")

if __name__ == "__main__":
    main()
