# numero_secreto=42
# tentativa_maxima=5

# try:
#     for n in range(tentativa_maxima,-1,-1):
#         print("Digite um número inteiro e tente descobrir o numero secreto!")

#         print(f'você está na tentativa {n} de {tentativa_maxima} Boa sorte!')
#         numero_escolhido=int(input("digite um numero: "))

#         if numero_escolhido==numero_secreto:
#             print("PARABENS!! VOCÊ É UM AKINATOR DOS NUMEROS")
#             break
        
#         elif numero_escolhido>numero_secreto:
#             print(f"Você escolheu o {numero_escolhido} que é maior que o número secreto")
#         else:
#             print(f"Você escolheu o {numero_escolhido} que é maior que o numero secreto")
# except:ValueError
# print("TENTATIVAS ESGOTADAS")

#######---------#######

# lado_a=int(input("Digite o comprimento A: "))
# lado_b=int(input("Digite o comprimento B: "))
# lado_c=int(input("Digite o comprimento C: "))

# if lado_a + lado_b>lado_c and lado_a+lado_c>lado_b and lado_b+lado_c>lado_a :
#     print("É UM TRIANGULO")
# else:
#     print("QUE RAIOS É ISSO?")

########----------########

# try:
    
#     print("Digite o numero correspondente para cada opção: 1 - Iniciar | 2 - Configurações | 3 - Ajuda | 4 - Sair")
#     opcao=int(input("DIGITE UM MUMERO DE 1 A 4: "))
#     match opcao :
#         case 1:
#             print("INICIAR")
#         case 2:
#             print("CONFIGURAÇÕES")
#         case 3:
#             print("AJUDA")
#         case 4:
#             print("SAIR")
#         case _ :
#             print("OPÇÃO INVALIDA")

# except ValueError:
#     print("OPÇÃO INVALIDA")

###########------------############

# palavra=input("digite uma palavra: ").lower()
# print(palavra)

# contador_vogal=0
# for  letra in palavra:
#     if letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u' :
#         contador_vogal+=1
#         print("QUANTIDADE DE VOGAIS",contador_vogal)

###############----------------##############

# usuario="arroz"
# senha="feijao"
# tentativa_atual=0
# tentativas_max=5

# while tentativa_atual<tentativas_max:

#     usuario1=input("crie um usuario: ")
#     senha1=input("crie uma senha: ")
    
#     if usuario1 == usuario and senha1 == senha:
#         print("senha correta")
#         break
    
#     else:
#         tentativa_atual+=1
#         print(f'tentativa atual {tentativa_atual} faltam {tentativas_max-tentativa_atual}') 

#######################------------------###############   

# primeiro_numero=float(input("digite um numero: "))
# operacoes= input( "digite operação:(+,-,*,/): ")
# segundo_numero=float(input("digite um numero: "))

  
# match operacoes:
#     case "+":
#         print(f"soma: {primeiro_numero+segundo_numero}")
#     case "-":
#         print(f"subtração: {primeiro_numero-segundo_numero}")
#     case "*":
#         print(f"multiplicação: {primeiro_numero*segundo_numero}")
#     case "/":
#         print(f"divisao: {primeiro_numero/segundo_numero}")
#     case _:
#         print("invalido")
    
#############---------------###################

# contador=int(input("digite um numero"))

# while contador >= 1:
#     print(contador)
#     contador=contador-1

###############------------------#############

ano_nascimento=int(input("Em que ano você nasceu: "))
ano_atual=2025
idade=ano_atual-ano_nascimento
print(f"sua idade é: {idade}")



if idade<12:
    print("Criança")

elif 12<idade<17:
    print("Adolescente")

else:
    print("Adulto")
