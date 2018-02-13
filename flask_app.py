#  rotinas python anywhere

#  lista = ListKros('/home/felipedacs/mysite/static', 'krosmaster')
#  app.run(debug=True)

from flask import Flask, render_template, request
import random

from listakros import ListKros

lista = ListKros('static', 'krosmaster')
lista.cria_list()
listateste = []



app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/randomaster')
def randomaster():
    return render_template(
        'randomaster_form.html',
        titulo='Lista de kros',
        contents=lista.contents,
        datas=len(lista.headers)
    )


@app.route('/equipe', methods=['POST'])
def equipe():
    codigo = request.form['input_codigo']
    #  checar se o codigo está correto!

    lista_krosmasters = codigo.split(',')
    random.shuffle(lista_krosmasters)
    for i in range(1):
        listateste
    return render_template(
        'equipe.html',
        codigo=codigo,
        lista_krosmasters=lista_krosmasters
    )


@app.route('/teste')
def teste():
    random.shuffle(listateste)
    escolhidos = []
    for i in listateste:
        escolhidos.append(i)
    return render_template(
        'teste.html',
        listateste=listateste,
        escolhidos=escolhidos
    )


app.run(debug=True)

#  app.run(port=8080)
