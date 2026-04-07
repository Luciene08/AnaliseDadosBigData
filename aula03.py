# import numpy as np

# #Dados de exemplo
# dados = np.array([12, 15, 17, 20, 22, 25, 28, 30, 35, 40])
# print(dados)

# #calcular quartis
# q1 = np.percentile(dados, 25) # o 1° quartil representa 25% dos dados
# q2 = np.percentile(dados, 50) # a mediana é o mesmo que o quartil de 50%
# q3 = np.percentile(dados, 75) # p 3° quartil representa 75% dos dados

# # Exibir os resultados
# print(f"Primeiro quartil Q1:{q1}")
# print(f"Segundo quartil Q2:{q2}")
# print(f"Terceiro quartil Q3:{q3}")

import mysql.connector

conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
 password="",
 database="vendas_online"
)

cursor = conexao.cursor()

query = "SELECT * FROM PRODUTOS"

cursor.execute(query)

resultados = cursor.fetchall()

for linha in resultados:
    print(linha)