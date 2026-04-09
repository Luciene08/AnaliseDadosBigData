import mysql.connector

conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
 password="",
 database="vendas_online"
)

cursor = conexao.cursor()

query = "SELECT * FROM clientes"

cursor.execute(query)

resultados = cursor.fetchall()

for linha in resultados:
    print(linha)



cursor = conexao.cursor()

query = "SELECT * FROM Pedidos"

cursor.execute(query)

resultados = cursor.fetchall()

for linha in resultados:
    print(linha)

