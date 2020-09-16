'''
Criando Aspas no PRINT
Usando o ISUPPER
'''


Frase = 'Academia Knowledge'

print(Frase,' Original')
print('É Maiuscula? :',Frase.isupper()) #Ele esta fazendo Uma Pergunta-> Se a Var Frase é Maiuscula
#Ira retornar FALSE
print('É Maiuscula? :',Frase.islower())
print('A frase Original é:', Frase)
print('Usando \"Aspas\" No Print')
print('Convertida em \"UPPER\" e depois questionada se é \"UPPER\"=',Frase.upper().isupper())
print('A Frase Tem:', len(Frase), 'Letras')
print('A segunda letra da Frase é: ',Frase[1].upper())
print('Retorna a Posição da letra na Frase \"K\" = ',Frase.index("Kno"))
print(Frase.replace('Knowledge', '\"Unknown\"'),'replace-> Substitui Frase na Variavel')
