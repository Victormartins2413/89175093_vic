import streamlit as st

# Configuração da página
st.set_page_config(page_title="Aurora's Realm: The Enchanted Adventure", layout="wide")

# Incorporando o HTML dentro do Streamlit usando st.components.v1.html
st.components.v1.html("""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aurora's Realm: The Enchanted Adventure</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: black;
            color: white;
            margin: 0;
            padding: 0;
            overflow-x: hidden;
        }
        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: rgba(0, 0, 0, 0.8);
            padding: 20px;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 999;
        }
        header a {
            color: white;
            text-decoration: none;
            margin: 0 15px;
            font-size: 18px;
            padding: 10px;
            border-radius: 5px;
        }
        header a:hover {
            background-color: #1E90FF;
        }
        .container {
            margin-top: 100px;
            text-align: center;
            padding: 20px;
        }
        .btn {
            background-color: #1E90FF;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .btn:hover {
            background-color: #00BFFF;
        }
        video {
            position: fixed;
            top: 0;
            left: 0;
            min-width: 100%;
            min-height: 100%;
            z-index: -1;
            opacity: 0.5;
        }
    </style>
</head>
<body>
    <header>
        <nav>
            <a href="#home">Home</a>
            <a href="#quem-somos">Quem Somos</a>
            <a href="#downloads">Downloads</a>
            <a href="#novidades">Novidades</a>
            <a href="#eventos">Eventos</a>
            <a href="#lancamento">Lançamento</a>
        </nav>
        <div>
            <button class="btn">Entrar</button>
            <button class="btn">Cadastrar</button>
        </div>
    </header>

    <video autoplay loop muted playsinline>
        <source src="Vídeo_de_entrada.mp4" type="video/mp4">
    </video>

    <div class="container" id="home">
        <h1>Bem-vindo ao Aurora's Realm: The Enchanted Adventure</h1>
        <p>Fique por dentro de todas as atualizações sobre o nosso jogo incrível que será lançado em junho de 2025.</p>
    </div>

    <div class="container" id="quem-somos">
        <h2>Quem Somos?</h2>
        <p>Nós somos uma equipe dedicada a criar um jogo único e emocionante, trazendo aventuras épicas e uma jogabilidade imersiva.</p>
    </div>

    <div class="container" id="downloads">
        <h2>Downloads</h2>
        <p>O jogo estará disponível para download em junho de 2025.</p>
    </div>

    <div class="container" id="novidades">
        <h2>Novidades</h2>
        <p>Últimas atualizações sobre o desenvolvimento do jogo: novos recursos, mecânicas e mais!</p>
    </div>

    <div class="container" id="eventos">
        <h2>Eventos</h2>
        <p>Participe de eventos e ganhe recompensas exclusivas dentro do Aurora's Realm!</p>
    </div>

    <div class="container" id="lancamento">
        <h2>Data de Lançamento</h2>
        <p>Aurora's Realm será lançado oficialmente em junho de 2025.</p>
    </div>

</body>
</html>
""", height=1000, scrolling=True)
