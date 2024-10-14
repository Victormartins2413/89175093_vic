import sqlite3

# Caminho completo para o arquivo do banco de dados
caminho_banco_de_dados = r'C:\Users\Victor\Videos\Test-jogo\cadastro.db'

# Função para criar o banco de dados e a tabela de cadastro
def criar_banco_de_dados():
    # Conectar ao banco de dados (se não existir, ele será criado)
    conn = sqlite3.connect(caminho_banco_de_dados)

    # Criar um cursor
    cursor = conn.cursor()

    # Executar um comando SQL para criar uma tabela de cadastro
    cursor.execute('''CREATE TABLE IF NOT EXISTS cadastro (
                        id INTEGER PRIMARY KEY,
                        nome TEXT NOT NULL,
                        idade INTEGER,
                        altura REAL,
                        peso REAL,
                        senha TEXT NOT NULL,
                        email TEXT NOT NULL
                    )''')

    # Commitar as alterações e fechar a conexão
    conn.commit()
    conn.close()

# Chamar a função para criar o banco de dados e a tabela
criar_banco_de_dados()
