from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/produtos')
def produtos():
    return render_template('produtos.html')

@app.route('/SAC')
def contato():
    return render_template('sac.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/sobre')
def sobre():
    return render_template('aboutus.html')

@app.route('/politicaprivacidade')
def politica():
    return render_template('polpriv.html')

@app.route('/termos')
def termos():
    return render_template('termos.html')

@app.route('/cards')
def carrossel():
    return render_template('carrossel.html')

if __name__ == '__main__':
    app.run(debug=True)