import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

# Ler o arquivo Excel para um DataFrame
df=pd.read_excel('base_invest.xlsx', sheet_name= 'Transacoes')
df_ativo=pd.read_excel('base_invest.xlsx', sheet_name= 'Ativo')
# Exibir as primeiras 5 linhas do DataFrame
# op_compra=df[df['operacao'] == 'compra'] #tabela df[dentro da tabela df[pegar de operaçoes == 'compra']]
# op_venda=df[df['operacao'] == 'venda']

# max_compra= op_compra['preco'].max()
# min_compra=op_compra['preco'].min()
# max_venda=op_venda['preco'].max()
# min_venda=op_venda['preco'].min()

# print(f" O preço maximo de compra é:{max_compra}")
# print(f" O preço minimo de compra é:{min_compra}")
# print(f" O preço maximo de venda é:{max_venda}")
# print(f" O preço minimo de venda é:{min_venda}")

# max_compra=df.groupby('operacao')['preco'].max()
# print(max_compra)

# df['valor_total']=df['quantidade'] * df['preco']
# print(df['valor_total'])
# valor_por_ativo=df.groupby('id_ativo')['valor_total'].sum()
# print(valor_por_ativo)
# id_ativo_maior_valor= valor_por_ativo.idxmax()
# cnpj_maior_valor=df_ativo[df_ativo['id_ativo']== id_ativo_maior_valor]['cnpj'].iloc[0]
# print(id_ativo_maior_valor)
# print(cnpj_maior_valor)




# Calcule o Q1, Q2 (Mediana) e Q3 para a coluna 'preco'
# q1_preco = df['preco'].quantile(0.25)
# q2_preco = df['preco'].quantile(0.50)
# q3_preco = df['preco'].quantile(0.75)

# print(f"Preço Q1: {q1_preco}")
# print(f"Preço Mediana (Q2): {q2_preco}")
# print(f"Preço Q3: {q3_preco}")


# Selecione a linha com índice 2 (iloc)
# print(df.iloc[0])
# Selecione a linha com id_participante igual a 101 (query)
# print(df.query("id_participante == 101"))
# print(df.loc[df['preco']>32.8])

# Contar a frequência de cada tipo de operação
contagem_operacao = df['operacao'].value_counts()
# Criar um gráfico de barras
contagem_operacao.plot(kind='bar', title='Tipos de Operação')
# Mostrar o gráfico
plt.show()
