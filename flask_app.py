#  rotinas python anywhere

#  lista = ListKros('/home/felipedacs/mysite/static', 'krosmaster')
#  app.run(debug=True)

from flask import Flask, render_template, request, flash
import random

from listakros import ListKros

lista = ListKros('static', 'krosmaster')
lista.cria_list()
listateste = []


def retorna_kros(procurado, lista_csv):
    for linha in lista_csv:
        if procurado == linha['nome_class']:
            linha['nivel'] = int(linha['nivel'])
            linha['qtd'] = int(linha['qtd'])
            return linha
        else:
            pass
    return 'aaa'


def escrever_auditoria(msg_auditoria, auditoria):
    print(msg_auditoria)
    auditoria.append(msg_auditoria)
    return auditoria


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
    times_krosmaster = []
    qtd_times = int(request.form['qtd_times'])
    #  qtd_times = 1
    auditoria = []

    for t in range(qtd_times):
        times_krosmaster.append('')
        print(t)

    for e in range(33):
        auditoria = escrever_auditoria('***** TENTATIVA DE CRIAR NUMERO: {} *****'.format(e + 1), auditoria)

        lista_krosmasters = codigo.split(',')
        random.shuffle(lista_krosmasters)

        auditoria = escrever_auditoria('Resultado da desordenação: {}'.format(lista_krosmasters), auditoria)

        i = 0
        for escolhido in lista_krosmasters:
            lista_krosmasters[i] = retorna_kros(escolhido, lista.contents)
            if classificacao == 'um' or classificacao == 'dois' or classificacao == 'tres':

                if lista_krosmasters[i]['eternal'] == 'ban':
                    lista_krosmasters.remove(lista_krosmasters[i])
                    auditoria = escrever_auditoria('BAN: {}'.format(lista_krosmasters[i]), auditoria)
                    i += 1
            elif classificacao == 'season':
                if lista_krosmasters[i]['ban_season'] == 'ban':
                    lista_krosmasters.remove(lista_krosmasters[i])
                    auditoria = escrever_auditoria('BAN: {}'.format(lista_krosmasters[i]), auditoria)
                    i -= 1
            i += 1

        try:
            for t in range(qtd_times):
                auditoria = escrever_auditoria('______ FORMANDO TIME {} ______'.format(t + 1), auditoria)
                time_krosmaster = []
                i = 0
                total_gg = 12
                time_com_boss = False
                while total_gg > 0:
                    count = sum(x.get('nome') == lista_krosmasters[i]['nome'] for x in time_krosmaster)
                    if lista_krosmasters[i]['nivel'] <= total_gg and count < lista_krosmasters[i]['qtd']:

                        if classificacao == 'um' or classificacao == 'dois' or classificacao == 'tres':
                            if lista_krosmasters[i]['boss_eternal'] == 'boss' and time_com_boss:
                                pass
                                #  não entra no time
                                auditoria = escrever_auditoria(
                                    '-> NÃO entrou no time por ser BOSS: {}'.format(lista_krosmasters[i]['nome']),
                                    auditoria)
                            else:
                                #  entra no time
                                if lista_krosmasters[i]['boss_eternal'] == 'boss':
                                    time_com_boss = True
                                time_krosmaster.append(lista_krosmasters[i])
                                total_gg -= lista_krosmasters[i]['nivel']
                                auditoria = escrever_auditoria(
                                    '-> ENTROU: {}. Sobram {}gg'.format(lista_krosmasters[i]['nome'], total_gg),
                                    auditoria)
                                lista_krosmasters.remove(lista_krosmasters[i])

                        elif classificacao == 'season':
                            if lista_krosmasters[i]['boss_season'] == 'boss' and time_com_boss:
                                pass
                                #  não entra no time
                                auditoria = escrever_auditoria(
                                    '-> NÃO entrou no time por ser BOSS: {}'.format(lista_krosmasters[i]['nome']),
                                    auditoria)
                            else:
                                #  entra no time
                                if lista_krosmasters[i]['boss_season'] == 'boss':
                                    time_com_boss = True
                                time_krosmaster.append(lista_krosmasters[i])
                                total_gg -= lista_krosmasters[i]['nivel']
                                auditoria = escrever_auditoria(
                                    '-> ENTROU: {}. Sobram {}gg'.format(lista_krosmasters[i]['nome'], total_gg),
                                    auditoria)
                                lista_krosmasters.remove(lista_krosmasters[i])
                    else:
                        auditoria = escrever_auditoria(
                            '-> NÃO entrou no time por falta de gg ou atingiu seu limite: {}. {}gg'.format(lista_krosmasters[i]['nome'],
                                                                                     total_gg), auditoria)
                    i += 1
                time_com_boss = True
                if len(time_krosmaster) < 3 or len(time_krosmaster) > 7:
                    raise IndexError
                times_krosmaster[t] = time_krosmaster
            break
        except IndexError:
            auditoria = escrever_auditoria(
                '☠☠☠ Acabaram as opções da fila de kros ☠☠☠', auditoria)
            pass

    auditoria = escrever_auditoria(
        '§§§ TOTAL DE TENTATIVAS DE CRIAÇÃO DE TIME -> {} §§§'.format(e + 1), auditoria)

    if e >= 32:
        flash('O algoritmo tentou identificar {} vezes a randomização do time e infelizmente não foi possível.'.format(
            e + 1))

    total_gg = 12

    return render_template(
        'equipe.html',
        codigo=codigo,
        lista_krosmasters=lista_krosmasters,
        times_krosmaster=times_krosmaster,
        auditoria=auditoria
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
