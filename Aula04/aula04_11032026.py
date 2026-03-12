
# carro= True
# combustivel=True

#  ao invés de colocar "carro ==false" pode colocar "not" na frente da variável caso ela comece falsa 
#  not false é o mesmo que não ser falso, então se não é false é verdadeiro


# if not carro and not combustivel:
#     print("Meu carro liga")
# elif carro==False or combustivel==False:
#     print("Não sobrou nada pro fusquinha")
# else:
#     print('Erro de execução')

# if not carro and not combustivel:
#     print("Meu carro liga")
# else:
#     print("Não sobrou nada pro fusquinha")

"""
semana = int(input("informe o dia da semana:"))
if semana == 1:
 print("Domingo")
elif semana == 2:
 print("Segunda-feira")
elif semana == 3:
 print("Terça-feira")
elif semana == 4:
 print("Quarta-feira")
elif semana == 5:
 print("Quinta-feira")
elif semana == 6:
 print("Sexta-feira")
elif semana == 7:
 print("Sábado")
else: # O 'else' funciona como o 'default'
 print("Dia inválido")

"""

# SEM TRATAMENTO

# mes = int(input("Digite o mes"))

# match mes:
#  case 1:# antes do "case" tem 1 espaço( se não tever esse espaço vai dar erro)
#     print("Janeiro")
#  case 2:
#     print("Fevereiro")
#  case 3:
#     print("Março")
#  case 4:
#     print("Abril")
#  case 5:
#     print("Maio")
#  case 6:
#       print("Junho")
#  case 7:
#       print("julho")
#  case 8:
#       print("Agosto")
#  case 9:
#       print("Setembro")
#  case 10:
#       print("Outubro")
#  case 11:
#       print("Novembro")
#  case 12:
#       print("Dezembro")
      

#  case _: # O underline ( _ ) funciona como o 'default' ou 'else'
#     print("Mês inválido")

####COM TRATAMENTO####
try:
 
    numero_mes = int(input("Digite um mes de 1 a 12"))

    match numero_mes:
        case 1:# antes do "case" tem 1 espaço( se não tever esse espaço vai dar erro)
            print("Janeiro")
        case 2:
            print("Fevereiro")#observar as identações, cada tratamento tem uma indentação diferente( como se fosse uma dentro da outra) 

        case 3:
            print("Março") #### o except tem que estar no mesmo nível de indentação do try
        case 4:
            print("Abril") ### selecionar + TAB (indenta tudo selecionado)
        case 5:
            print("Maio")
        case 6:
            print("Junho")
        case 7:
            print("julho")
        case 8:
            print("Agosto")
        case 9:
            print("Setembro")
        case 10:
            print("Outubro")
        case 11:
            print("Novembro")
        case 12:
            print("Dezembro")
except ValueError:
    print('Erro desconhecido')
      
 
 