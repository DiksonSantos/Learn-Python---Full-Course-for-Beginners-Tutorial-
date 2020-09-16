'''
Conversor_De_Mes = {1: "Janeiro",
                    2: "Fevereiro",
                    3: "Março",
                    "Abr": "Abril",
}

print(Conversor_De_Mes[3]) #imprime Março
'''

'''
#2:14:16 LOOP WHILE:
Y = 1   #FLAG
print("Verdade",Y)
while Y <=9:   #CONDIÇÃO

    Y += 1   #CONTADOR
    print("Verdade", Y)  #RESULTADOS
print("Loop Terminado!")  #FORA DO LOOP
'''

# 2:20:02 CONSTRUINDO JOGO DA ADVINHAÇÃO:
print("Tente Descobrir a Palavra secreta -> Dica: 'Pescoçuda'")

Palavra_Secreta = "girafas"  #Para o LOWER  funcionar você tem que digitar aqui tudo em Minusculo
Advinhe = ""
Contador = 0
Limite_Tentativas = 3
Findou = False

while Advinhe != Palavra_Secreta and not(Findou): #... e Findou Não for Verdadeiro...
    if Contador < Limite_Tentativas:
        Advinhe = str.lower(input("Sugestão: "))
        Contador += 1
    else: #Se o contador for maior que 3:
        Findou = True #A condição muda
if Findou: #E, ..Se Findou se tornar verdade
    print("Acabaram as Chances, Fim De Jogo")
else: #Essa alguma coisa diferente No Caso é -> Se você acertar a Palavra secreta.
    print("Você Venceu!")
print("Numero de Tentativas: " ,Contador)


# Continua em 2:32:46H Fol Loop
