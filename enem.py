import pandas as pd
import numpy as np
import math as math

# este subset esta com 99.999 alunos
file_name = 'data.csv'
dados = pd.read_csv(file_name, sep=';', encoding="ISO-8859-1")

# Estamos aqui separando somente a prova de Ciências da Natureza e suas Tecnologias‎
heads = ['TX_RESPOSTAS_CN', 'CO_PROVA_CN']
alunos = dados[heads]

# numero de acertos para verificar melhora
numero_acertos = 19
# acumualador de participantes que melhoraram a quantidade de acerto
count = 0
# acumulador participantes que melhoraram a quantidade de acertos acima do numero_acertos
count_maior = 0
# acumualador de participantes
total = 0

# participantes linha a linha
rowsAlunos = alunos.iterrows()

# este array foi criado usando o gabarito.py
gabaritos = {
    450: 'ACEDEAEAEBECAADABBDBCEDEDDCDDABCCACBCACEBDEBB',
    448: 'BCACEEBBBDACEDECAADDDABDBCCACDCBCEDEDABEBEAEA',
    490: 'BCCDABBDBEBAACEBDDAEECAADEEDDBEDCACEDCEECCACB',
    447: 'BDDEDBCACEBCCACDCDDAECAADBDBCEEAEAABEBEBBACED',
    487: 'CACBEDCADBCEECCEDEDAACEBDDAADEEECAEBBDBCDABBC',
    489: 'CDABBCCEECBDBEBAACEADEEECABDDAEDDBCACBCEDEDCA',
    449: 'EBBEBACEDDEDDCBCCACBDDDAECAADBCEABEAEABDBCACE',
    488: 'EDCADBBCCACBCDABADEBDDAAACEEECAEBEDCEECBDBCED',
}


def quantidade_corretas(gabarito, respostas):
    '''
    Retorna a quantidade de respostas corretas
    '''
    count = 0
    tamanho = len(gabarito)
    if respostas != 'nan':
        for i in range(0, tamanho):
            if gabarito[i] == respostas[i]:
                count += 1
    return count


def verifica_quantidade_corretas(idCorreto, respostas):
    '''
    Verifica gabarito a gabarito a quantidade de corretas
    '''
    todos = []
    for g in gabaritos:
        count = quantidade_corretas(gabaritos[g], respostas)
        todos.append({'c': g == idCorreto, 'q': count})
    return todos


def errado_maior(todosGabaritos):
    '''
    Verifica se algum outro gabarito teve melhora
    '''
    correta = 0
    for g in todosGabaritos:
        if g['c']:
            correta = g['q']

    for g in todosGabaritos:
        atual = int(g['q'])
        if not g['c'] and atual > correta:
            return {'errado_maior': True, 'maior_que': correta > numero_acertos}

    return {'errado_maior': False}


for index, row in rowsAlunos:
    total += 1
    co_prova = row['CO_PROVA_CN']

    if not math.isnan(co_prova):
        co_prova = int(co_prova)
        respostas = str(row['TX_RESPOSTAS_CN'])

        if respostas != 'nan':
            todosGabaritos = verifica_quantidade_corretas(co_prova, respostas)

            resultado = errado_maior(todosGabaritos)
            if resultado['errado_maior']:
                count += 1
            if resultado['errado_maior'] and resultado['maior_que']:
                count_maior += 1


print('o total de alunos é {} o total que melhorou é {} e dos que melhoram acima de {} foram {}'
      .format(total, count, numero_acertos,  count_maior))

# o total de alunos é 5.513.747 o total que melhorou é 2.380.415

# o total de alunos é 99999 o total que melhorou é 43440 e dos que melhoram acima de 5 foram 40862
# o total de alunos é 99999 o total que melhorou é 43440 e dos que melhoram acima de 10 foram 12434
# o total de alunos é 99999 o total que melhorou é 43440 e dos que melhoram acima de 15 foram 111
# o total de alunos é 99999 o total que melhorou é 43440 e dos que melhoram acima de 16 foram 39
# o total de alunos é 99999 o total que melhorou é 43440 e dos que melhoram acima de 17 foram 9
# o total de alunos é 99999 o total que melhorou é 43440 e dos que melhoram acima de 18 foram 3
# o total de alunos é 99999 o total que melhorou é 43440 e dos que melhoram acima de 19 foram 0
