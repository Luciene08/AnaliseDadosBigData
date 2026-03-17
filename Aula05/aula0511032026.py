#LAÇOS DE REPETIÇÃO:

# intervalo1=range(10)
# print(intervalo1)

# print("***")

# for numero in range(1,10,2):
#     print('contando')
#     print('numero:')
#     print(numero)

# for i in range(5):
#     try:
#         #i representa o número ateaul da repetição
#         print(f"Número{i + 1} de 5")
#         num = float(input( "Digite um número: "))

#         dobro = num * 2
#         triplo = num * 3
#         quádruplo = num * 4

#         print(f" Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quádruplo}\n")
#     except ValueError:
#         print("Entrada inválida. Tente novamente.")

# WHILE versão 1

# loolap=float(input('Qual o valor do evento (inteira)? ')) # loop infinito no input
# # CTRL + C + C QUBRA CODIGO INFINITO

# while loolap > 300:
#     print('mas não vou mesmo!!!')

# print( 'Estarei lá!')

# loolap=float(input('Qual o valor do evento (inteira)? ')) # loop infinito no input
# CTRL + C + C QUBRA CODIGO INFINITO

#versão 2

# while loolap > 300:
#     print('mas não vou mesmo!!!')

# print( 'Estarei lá!')

# #versão 3

# loolap=0

# while loolap > 300:
#     loolap=float(input('Qual o valor do evento (inteira)?')) #Dependnedo do input, cai num loop infinito
#     print('Mas não vou mesmo!!!')

# print('Estarei lá!')
# ##

# loolap=300

# while loolap >= 300:
#     loolap=float(input('Qual o valor do evento (inteira)?')) #Dependnedo do input, cai num loop infinito
#     print('Mas não vou mesmo!!!')

try:
 
    numero_codigo = int(input("Digite um numero de 1 a 11: "))

    match numero_codigo:
        case 1:
            print("Sul")
        case 2:
            print("Norte")
        case 3:
            print("Leste") 
        case 4:
            print("Oeste")
        case 5:
            print("Nordeste")
        case 6:
            print("Nordeste")
        case 7:
            print("Sudeste")
        case 8:
            print("Sudeste")
        case 9:
            print("Sudeste")
        case 10:
            print("Centro-Oeste")
        case 11:
            print("Noroeste")
        case _ :
            print("importado")
except ValueError:
    print("Importado")



