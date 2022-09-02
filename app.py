# Como colocar código Python no HTML5
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    nome = 'Bernardo'
    idade = 4
    return render_template('index.html', nome=nome, idade=idade)

if __name__ == '__main__':
    app.run(debug=True)