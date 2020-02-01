import pandas as pd
import numpy as np

# no momento em que executamos a busca por gabaritos diferentes 
# usamos o arquivo completo com mais de 5 milhões de participantes
file_name = 'data.csv'
dados = pd.read_csv(file_name, sep=';', encoding="ISO-8859-1")

# Estamos aqui separando somente a prova de Ciências da Natureza e suas Tecnologias‎
heads = ['TX_GABARITO_CN', 'CO_PROVA_CN']
dados = dados[heads]

# Pegando os gabaritos únicos
gabaritos = dados.groupby(['TX_GABARITO_CN'])

# Resultado dos gabaritos unicos 
# ACEDEAEAEBECAADABBDBCEDEDDCDDABCCACBCACEBDEBB   450
# BCACEEBBBDACEDECAADDDABDBCCACDCBCEDEDABEBEAEA   448
# BCCDABBDBEBAACEBDDAEECAADEEDDBEDCACEDCEECCACB   490
# BDDEDBCACEBCCACDCDDAECAADBDBCEEAEAABEBEBBACED   447
# CACBEDCADBCEECCEDEDAACEBDDAADEEECAEBBDBCDABBC   487
# CDABBCCEECBDBEBAACEADEEECABDDAEDDBCACBCEDEDCA   489
# EBBEBACEDDEDDCBCCACBDDDAECAADBCEABEAEABDBCACE   449
# EDCADBBCCACBCDABADEBDDAAACEEECAEBEDCEECBDBCED   488