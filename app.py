from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World! Teste de Servidor Web em aplicações Flask!! '

if __name__ == '__main__':
    app.run()