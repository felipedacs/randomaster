#  /home/felipedacs/mysite/static

from flask import Flask, render_template

from listakros import ListKros

lista = ListKros('static', 'krosmaster')
lista.cria_list()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/randomaster')
def randomaster_form():
    return render_template(
        'randomaster_form.html',
        titulo='Lista de kros',
        contents=lista.contents,
        datas=len(lista.headers)
    )


@app.route('/lista')
def listagem():
    return render_template(
        'lista.html',
        titulo='Lista de kros',
        headers=lista.headers,
        contents=lista.contents,
        datas=len(lista.headers)
    )


app.run(debug=True)

#  app.run(port=8080)
