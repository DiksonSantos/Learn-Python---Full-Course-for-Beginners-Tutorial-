from math import sqrt
#print("Digite Help Para Mais Informações")

print("""Digite + Para Adição"
      "Digite - Para Subtração"
      "Digite / Para Divisão"
      "Digite * Para Multiplicação"
      "Digite R para Radiciação (Somente UM Numero)""")

try:
    OP = str.lower(input('Insira Operador: '))
    num1 = float(input('Insira Numero: '))

    num2 = float(input('Insira Segundo Numero: '))

    if OP == "+":
        print(num1 + num2)
    elif OP == '-':
        print(num1 - num2)
    elif OP == '/':
        print(num1 / num2)
    elif OP == '*':
        print(num1 * num2)
    elif OP == 'R'.lower():
        print(sqrt(num1))

    else:
        print('Operador Invalido.')

except ValueError:
    #pass
    print('Caso Não escolha a Opção Raiz Quadrada Você precisa digitar DOIS numeros.')

'''
Poderia colocar Cada Operação matematica dentro de Uma Função DEF e transforma-las em modulos
Assim de acordo com o sinal matematico digitado os IFs chamariam determinada Função. Isso faria o codigo ficar 
Muito Mais enchuto.
'''

#Continua em 2:07:19  -> Dicionarios    (09-03-19)
