#  rotinas python anywhere

#  lista = ListKros('/home/felipedacs/mysite/static', 'krosmaster')
#  app.run(debug=True)

from flask import Flask, render_template, request, flash
import random

from listakros import ListKros
from times import TimePadrao, EternalPadrao, EternalUm, EternalDois, EternalTres, TimeSeason

lista = ListKros('static', 'krosmaster')
backgrounds = ['pattern1', 'pattern2', 'pattern3', 'pattern4', 'pattern5', 'pattern6', 'pattern7', 'pattern8', 'pattern9', 'pattern10', 'pattern11']


def escrever_auditoria(msg, auditoria):
    print(msg)
    auditoria.append(msg)
    return auditoria


def converte_auditoria_class(auditorias, auditoria):
    for a in auditorias:
        auditoria.append(a)
    return auditoria


def retorna_kros(procurado):
    for linha in lista.contents:
        if procurado == linha['nome_class']:
            linha['nivel'] = int(linha['nivel'])
            linha['qtd'] = int(linha['qtd'])
            return linha
        else:
            pass


def retorna_csv_kros(lista_krosmasters):
    contador = 0
    for escolhido in lista_krosmasters:
        lista_krosmasters[contador] = retorna_kros(escolhido)
        contador += 1
    return lista_krosmasters


app = Flask(__name__)
app.secret_key = 'kros'


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
    classificacao = request.form['classificacao']
    qtd_times = int(request.form['qtd_times'])
    auditoria = []

    max_tentativas = 33

    for e in range(max_tentativas):
        lista_krosmasters = codigo.split(',')
        times = []
        total_times_completos = 0

        auditoria = escrever_auditoria('✍ TENTATIVA DE RANDOMIZAR: {} ✍'.format(e + 1), auditoria)
        random.shuffle(lista_krosmasters)
        auditoria = escrever_auditoria('🔀 Resultado da desordenação: {}'.format(lista_krosmasters), auditoria)

        lista_krosmasters = retorna_csv_kros(lista_krosmasters)

        for t in range(qtd_times):
            auditoria = escrever_auditoria('_______ TIME NUMERO {} ______'.format(t+1), auditoria)
            if classificacao == 'um':
                time = EternalUm(lista_krosmasters)
            elif classificacao == 'dois':
                time = EternalDois(lista_krosmasters)
            elif classificacao == 'tres':
                time = EternalTres(lista_krosmasters)
            elif classificacao == 'season':
                time = TimeSeason(lista_krosmasters)
            times.append(time)
            lista_krosmasters = time.fonte_dos_times
            auditoria = converte_auditoria_class(time.msg_auditoria, auditoria)

            if time.time_completo:
                auditoria = escrever_auditoria('✨ SUCESSO! Time completo ✨', auditoria)
                total_times_completos += 1

        if qtd_times == total_times_completos:
            max_tentativas = False
            break

    auditoria = escrever_auditoria(
        '▄▀▄▀▄▀ TENTATIVAS: {} ▄▀▄▀▄▀'.format(e + 1), auditoria)

    if e >= 32:
        flash('O algoritmo tentou identificar {} vezes a randomização do time e infelizmente não foi possível.'.format(
            e + 1))

    total_times_completos = 0

    time = []

    random.shuffle(backgrounds)

    return render_template(
        'equipe.html',
        codigo=codigo,
        times=times,
        auditoria=auditoria,
        background=backgrounds[0]
    )


app.run(debug=True)

#  app.run(port=8080)
