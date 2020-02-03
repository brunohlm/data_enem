import pandas as pd

# no momento em que executamos a busca por gabaritos diferentes 
# usamos o arquivo completo com mais de 5 milhões de participantes
file_name = 'data.csv'
dados = pd.read_csv(file_name, sep=';', encoding="ISO-8859-1")

# Estamos aqui separando somente a prova de Ciências da Natureza e suas Tecnologias‎
print(dados.TX_GABARITO_CN.unique())

# Resultado dos gabaritos unicos 
# ACEDEAEAEBECAADABBDBCEDEDDCDDABCCACBCACEBDEBB   450
# BCACEEBBBDACEDECAADDDABDBCCACDCBCEDEDABEBEAEA   448
# BCCDABBDBEBAACEBDDAEECAADEEDDBEDCACEDCEECCACB   490
# BDDEDBCACEBCCACDCDDAECAADBDBCEEAEAABEBEBBACED   447
# CACBEDCADBCEECCEDEDAACEBDDAADEEECAEBBDBCDABBC   487
# CDABBCCEECBDBEBAACEADEEECABDDAEDDBCACBCEDEDCA   489
# EBBEBACEDDEDDCBCCACBDDDAECAADBCEABEAEABDBCACE   449
# EDCADBBCCACBCDABADEBDDAAACEEECAEBEDCEECBDBCED   488
