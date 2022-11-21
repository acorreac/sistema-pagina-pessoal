

from flask import app, Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/curriculo')
def curriculo():
    return render_template('curriculo.html')

@app.route('/portifolio')
def portifolio():
    return render_template('portifolio.html')

@app.route('/hobby')
def hobby():
    return render_template('hobby.html', )

if __name__ == '__main__':
    app.run('0.0.0.0')