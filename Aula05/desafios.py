
##desafio 4
''''
. Código de Origem do Produto:
Escreva um programa que leia o código de origem de um produto e imprima na tela a região
de sua procedência, conforme a tabela abaixo:
Observação: caso o código não seja nenhum dos especificados, o produto deve ser
encarado como “Importado”.

'''
# try:
 
#     numero_codigo = int(input("Digite um numero de 1 a 11: "))

#     match numero_codigo:
#         case 1:
#             print("Sul")
#         case 2:
#             print("Norte")
#         case 3:
#             print("Leste") 
#         case 4:
#             print("Oeste")
#         case 5:
#             print("Nordeste")
#         case 6:
#             print("Nordeste")
#         case 7:
#             print("Sudeste")
#         case 8:
#             print("Sudeste")
#         case 9:
#             print("Sudeste")
#         case 10:
#             print("Centro-Oeste")
#         case 11:
#             print("Noroeste")
#         case _ :
#             print("importado")
# except ValueError:
#     print("Importado")

#### desafio 2##################
''''
Quantidade de Caixas de Azulejos:
Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento,
largura e altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em
todas as suas paredes (considere que não será descontada a área ocupada por portas e
janelas). Cada caixa de azulejos possui 1,5 m²


'''

# largura= float(input("largura em metros: "))
# comprimento= float(input("comprimenro em metros: "))
# altura= float(input("altura em metros: "))
# print()#coloquei esse print pra pular uma linha no terminal
# dimensao_cozinha = largura * comprimento * altura
# print("Dimensão da cozinha:",dimensao_cozinha)
# dimensao_parede=largura*altura
# print("dimensao da parede:",dimensao_parede)

# caixa_azulejo=1.5
# quantidade_caixas= dimensao_parede / caixa_azulejo
# print("Quantidade de caixas:",quantidade_caixas)

# ######desafio 3#################################
''''
Rendimento do Taxista:
Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o
preço do combustível é de R$ 6,15, escreva um programa para ler: a marcação do
odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros de
combustível gasto e o valor total (R$) recebido dos passageiros. Calcular e escrever: a
média do consumo em km/L e o lucro (líquido) do dia.

'''
# #Odometro
# odometro_inicial=float(input("odometro inicial: "))
# km_dia=float(input("km rodado: "))
# odometro_final=odometro_inicial+km_dia
# print("odometro", odometro_final)

# #combustível

# combustivel_inicial= float(input("combustivel inicial em litros: "))
# combustivel_final= float(input("combustivel fim do dia em litros: "))
# gasto_combustivel=combustivel_inicial-combustivel_final
# print("gasto total de combustivel: ",gasto_combustivel)
# valor_combustivel=6.15
# valor_gasto= gasto_combustivel*valor_combustivel
# print("valor gasto com combustivel: ",valor_gasto)
# print()##espassamento
# media_de_consumo=km_dia/gasto_combustivel
# print("media de consumo de combustivel gasto: ",media_de_consumo)
# print()##espassamento
# valor_recebido_corrida=float(input("valor recebido no fim do dia: "))
# lucro=valor_recebido_corrida-valor_gasto
# print("lucro do dia: ",lucro)



# #### desafio 6####
'''
Positivo ou Negativo:
Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o
valor zero como positivo
'''
# numero = int(input(" Digite um numero inteiro: "))
# if numero >=0:
#  print("positivo")
# else:
#  print("negativo")


''''
Média do Aluno com Optativa:
Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação
optativa dos estudantes de uma turma. Caso o estudante não tenha feito a optativa, deve
ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa
substitui a nota mais baixa entre as duas primeiras avaliações. Escrever a média e
mensagens que indiquem se o estudante foi aprovado, reprovado ou se está em
recuperação, de acordo com as informações abaixo:
Aprovado: média >= 6.0
Reprovado: média < 3.0
Recuperação: média >= 3.0 e < 6.0
'''

#abs = falor absoluto, não aceita numeros negativos
# =! é o mesmo que sinal de diferente<> poreém se usa =!

# nota01=(float(input("primeira nota: ")))
# nota02=(float(input("segunda nota: ")))
# optativa= (float(input("Tem nota optativa?")))

# if optativa == -1:
#     media=(nota01+nota02)/2
# else:
#     if optativa > nota01:
#         media=(optativa+nota02)/2
#     else:
#         media=(optativa+nota01)/2

# if media>= 6.0:
#     resultado ="APROVADO"
# elif media>= 3.0:
#     resultado= "RECUPERAÇÃO"
# else:
#     resultado="REPROVADO"

# print(f"Média final: {media}; Resultado: {resultado}")

''''
Cálculo de Lâmpadas:
Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para
iluminar um determinado cômodo de uma residência. Dados de entrada: a potência da
lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do
cômodo. Considere que a potência necessária é de 3 watts por metro quadrado e a cada
3m² existe um bocal para uma lâmpada.
'''
POTENCIA=3 #quando a "variável" é uma constante (não muda no codigo, fixa) pode ser escrita com letras maiusculas.
lmapadas=0
largura= float(input('largura: '))
comprimento=float(input('Comprimento: '))

area=largura*comprimento

lampadas= area/POTENCIA

print(f'São necessárias {round(lampadas)} para iluminar um cômodo de {area}m²') #round é usado para arredondar dizimas 
# .round() é utilizado para definir quantas casas serão arredondadas, por exemplo raund(2) arredonda 2 casas apos a virgula.

      

##Listas##
nomes=['Mateus','Alice','Caio','Larissa','Miguel','Rafael']

nome1= nomes[0]

print(nomes[-1])
print(nomes[-2])
print(nomes[-4])
print(nomes[-3])
print(nome1)

primeira_parte=nomes[0:3]
print(primeira_parte)
segunda_parte=[3:6]
print(segunda_parte)

print(len(nomes))

#TUPLAS###
nomes_tupla=tuple(nomes)
print(nomes_tupla)

#SET###
nomes_set=set(nomes)
print(nomes_set)

###DICIONARIOS:

nomes_dici={'nome1':'Matheus',
            'nome2':'Alice',
            'nome3':'Caio',
            'nome4':'Larissa'}
'Mateus','Alice','Caio','Larissa',
















