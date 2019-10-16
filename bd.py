from flask import Flask, render_template

nome_pagina = 'MusicBox'

app = Flask(__name__)

@app.route('/')
def layout():
    return render_template('index.html')

@app.route('/inicio')
def logo_inicio():
    return render_template('index.html')

@app.route('/o_projeto')
def o_projeto():
    return render_template('o_projeto.html') 

@app.route('/planos')  
def planos():
    return render_template('planos.html')     

@app.route('/Cadastro_itens')  
def cadastro_itens():
    return render_template('itens_cadastro.html')  

@app.route('/juntese')
def junte_se():
    return render_template('junte-se_.html', nome_pagina=nome_pagina)    

@app.route('/associados')
def associados():
    return render_template('listar.html', nome_pagina=nome_pagina)    




app.run()    