# # # ##### Revisão e Praticas aplicandos a logística e e-commerce ########
# # #Condicionais:
# # """""
# #     Exercício 1: Cálculo de Desconto Progressivo (Setor de Vendas) Um e-commerce
# # aplica descontos automáticos no carrinho. Crie um programa que receba o valor total da
# # compra e aplique a seguinte lógica:
# # ● Compras a partir de R$ 500,00: 15% de desconto.
# # ● Compras a partir de R$ 200,00 (e menos de 500): 10% de desconto.
# # ● Compras abaixo de R$ 200,00: Sem desconto. O programa deve exibir o valor do
# # desconto e o valor final a pagar, formatados em R$.
# # """
# # # valor_da_compra=float(input("Valor da compra: "))

# # # if valor_da_compra>500:
# # #     desconto=valor_da_compra*(15/100)
# # #     print(f'Desconto de 15%: R${desconto:.2f} \nValor final: R${valor_da_compra-desconto:.2f}')
# # # elif valor_da_compra>=200 and valor_da_compra<500:
# # #     desconto=valor_da_compra*(10/100)
# # #     print(f'Desconto de 10%: R${desconto:.2f} \nValor final: R${valor_da_compra-desconto:.2f}')
# # # else:
# # #     print("Sem desconto")

# # """"
# # ----------------------Crie um programa que:--------------------------

# #     Pergunte ao usuário o peso da carga (em kg).

# # Aplique as seguintes regras de frete:
# # Até 10 kg → taxa fixa de R$ 50
# # Entre 10 kg e 50 kg → taxa de R$ 100 + 5% do valor da carga
# # Acima de 50 kg → taxa de R$ 200 + 10% do valor da carga
# # Mostre no final um recibo formatado, com cada informação em uma linha:
# # *Peso da carga
# # *Valor da carga (o usuário também digita esse valor)
# # *Taxa de frete calculada
# # *Valor total (carga + frete)
# # *Mensagem final: "Obrigado por utilizar nosso serviço de logística!"
# # """


# # # peso_da_carga=float(input("Peso da Carga : "))
# # # valor_carga=float(input("Qual o valor da carga? "))

# # # if peso_da_carga<=10:
# # #     taxa=50
# # #     frete=taxa
# # #     valor_total=frete
# # #     print(f'Taxa de frete: {frete} \nValor Total: {valor_total}')
# # #     print("Obrigado por utilizar nosso serviço de logística!")

# # # elif peso_da_carga>10 and peso_da_carga<=50:
# # #     taxa=100
# # #     frete= valor_carga*(5/100) + taxa
# # #     valor_total=frete+valor_carga
# # #     print(f'Taxa de frete: {frete} \nValor Total: {valor_total}')
# # #     print("Obrigado por utilizar nosso serviço de logística!")
# # # else:
# # #     taxa=200
# # #     frete=(valor_carga*(10/100)) + taxa
# # #     valor_total= frete+valor_carga
# # #     print(f'Taxa de frete: {frete} \nValor Total: {valor_total}')
# # #     print("Obrigado por utilizar nosso serviço de logística!")

# # """
# # Desafio: Prazo de Entrega
# # Monte um programa que:

# # Pergunte ao usuário:
# # peso da carga (kg)
# # valor da carga (R$)
# # distância da entrega (km)
# # Calcule o frete usando as mesmas regras que você já fez:
# # Até 10 kg → frete = 50
# # Entre 10 e 50 kg → frete = 100 + 5% do valor da carga
# # Acima de 50 kg → frete = 200 + 10% do valor da carga
# # Calcule o prazo de entrega:
# # Até 100 km → 2 dias
# # Entre 101 e 500 km → 5 dias
# # Acima de 500 km → 10 dias
# # Mostre um recibo completo com:
# # Peso da carga
# # Valor da carga
# # Distância da entrega
# # Frete calculado
# # Valor total (carga + frete)
# # Prazo de entrega
# # Mensagem final: "Obrigado por utilizar nosso serviço de logística!"

# # """
# # peso_carga=float(input("Peso da Carga: "))
# # valor_carga=float(input("Qual o valor da carga? "))
# # distancia=float(input("Qual a distância? "))

# # if peso_carga<=10:
# #     frete=50
# #     valor_total=frete + valor_carga
# #     print(f'Frete: {frete:.2f}\nValor Total {valor_total:.2f}')

# # elif peso_carga>10 and peso_carga<50:
# #     frete=100 + (valor_carga*(5/100))
# #     valor_total = frete + valor_carga
# #     print(f'Frete: {frete:.2f}\nValor Total {valor_total:.2f}')

# # else:
# #     frete=200 + (valor_carga*(10/100))
# #     valor_total=frete+valor_carga
# #     print(f'Frete: {frete:.2f}\nValor Total {valor_total:.2f}')

# # if distancia<100:
# #     print("Prazo de Entrega: Em  até 2 dias !!")

# # elif distancia>=101 and distancia<=500:
# #     print("Prazo de Entrega: Em  até 5 dias!! ")

# # else:
# #     print("Prazo de Entrega em até 10 dias")
# # print("Obrigado por utilizar nosso serviço de logística!")

# """
# Monte um programa que pergunte ao usuário o tipo de veículo: 
# (1 = moto, 2 = carro, 3 = caminhão)
# mostre uma mensagem com o valor da taxa de pedágio correspondente.

# """


# numero=int(input("Qual o seu tipo de veículo?\nDigite o numero correspondente (1 = moto, 2 = carro, 3 = caminhão): "))

# match numero:
#     case 1:
#         print("Taxa de pedágio:R$ 100")
#     case 2:
#         print("Taxa de pedágio:R$150")
#     case 3:
#         print("Taxa de pedágio:R$200")
#     case _:
#         print("invalido")
""" 
Monte um programa que pergunte o peso e valor da carga de 5 clientes diferentes e 
mostre o recibo de cada um usando laço de repetição.

"""

# for i in range(5):
#     peso=float(input("Peso da Carga: "))
#     valor_carga=float(input("Valor da Carga: "))
    
#     if peso<10:
#         frete=50
#         valor_total= frete + valor_carga
#         print(f'Frete caulculado: R${frete:.2f}\nValor Total: R${valor_total:.2f}')

#     elif peso>=10 and peso<=50:
#         frete=100 + (valor_carga*(5/100))
#         valor_total= frete + valor_carga
#         print(f'Frete caulculado: R${frete:.2f}\nValor Total: R${valor_total:.2f}')

#     else:
#         frete=200 + (valor_carga*(10/100))
#         valor_total= frete + valor_carga
#         print(f'Frete caulculado: R${frete:.2f}\nValor Total: R${valor_total:.2f}')

# while True:

#     parada=input("digite 0 para parar:" )
#     if parada=="0":
#          print("Encerrado")
#          break
                   
  

#     peso=float(input("Peso da Carga: "))

#     valor_carga=float(input("Valor da Carga: "))
    
#     if peso<10:
#         frete=50
#         valor_total= frete + valor_carga
#         print(f'Frete caulculado: R${frete:.2f}\nValor Total: R${valor_total:.2f}')

#     elif peso>=10 and peso<=50:
#         frete=100 + (valor_carga*(5/100))
#         valor_total= frete + valor_carga
#         print(f'Frete caulculado: R${frete:.2f}\nValor Total: R${valor_total:.2f}')

#     else:
#         frete=200 + (valor_carga*(10/100))
#         valor_total= frete + valor_carga
#         print(f'Frete caulculado: R${frete:.2f}\nValor Total: R${valor_total:.2f}')

"""

 -------Equação do Custo de carregamento (CC)------

Cc = CA + i x P

Cc = Custo de carregamento

CA = Soma de todos os custos diretamente proporcionais

i = taxa de juros corrente

P = Preço pago ao fornecedor
"""

# CA=float(input("Valor custos diretos: "))
# i=float(input("Taxa de juros: "))
# P=float(input("Preço pago ao fornecedor: "))

# Cc=CA + (i*P)

# print(f"O custo com carregamento é: R${Cc:.2f} unidade.ano")

"""
-------Equação do custo inversamente proporcional------
     Cp x número de pedidos 
      Onde: Cp = Custo de preparação + Custo do transporte    	
      Cp = Custo de preparação (obtenção, aquisição, custo do pedido de compras)

Custo do transporte = O valor que será pago para a transportadora entregar o produto

Número de pedidos = Quantas vezes a empresa pretende comprar por ano.

*A relação do número de pedidos com a demanda da empresa,
 informará a quantidade recebida por lote, representado por Q.

**O estoque médio (EM) é representado então por Q/2.
"""

# demanda =float(input("Demanda prevista: "))
# n_pedidos = int(input("Numero de pedidos por ano: "))
# q_lote = demanda/n_pedidos
# custo_preparacao= float(input("Custo de preparação do produto: "))
# valor_frete=float(input("Valor do frete: "))
# custo_total=custo_preparacao + valor_frete
# Cp=custo_total*n_pedidos
# print(f'Quantidade de produtos por lote: {q_lote:.2f}\nCusto Toatal de preparação(Cp): {Cp:.2f}')

   


"""
------Indicador de desempenho: Nível de serviço-----
numero de produtos entregues/numero de pedidos totais

Excente acima de 95
Bom entre 90 e 95
Ruim abaixo de 90

"""
# try:
#     for i in range(2):
#         n_pedido_mes=int(input("Numero de pedidos do mes: "))
#         n_pedido_atendidos=int(input("Numero de pedidos entregues: "))
#         nivel_de_servico=(n_pedido_atendidos/n_pedido_mes)*100

#         if nivel_de_servico>95:
#             print(f"Porcentagem de {nivel_de_servico:.2f}\nDesmpenho EXCELENTE!!!")  
#         elif nivel_de_servico>=90 and nivel_de_servico<=95:
#             print(f'Porcentagem de {nivel_de_servico:.2f}\nDesempenho BOM!!!') 
#         else:
#             print(f'Porcentagem de {nivel_de_servico:.2f}\nDesempenho RUIM!!!') 
# except ValueError:
#     print("Entrada inválida!! Utilize apenas números inteiros!!")
