'''
Gua = open("Funcionarios.txt", "r")
var = Gua.read() #Converteu Para Legivel
print(var)
print("\nO Arquivo é Legivél??: " , Gua.readable()) #Para checar se o arquivo É legivel.
print("\n")
print(Gua.readline())
#print(Gua.readlines())
#Gua.close()



#O Software a baixo le Linha a Linha com espaço entre elas.
empre = open("Funcionarios.txt", "r")

print(empre.readline()) #Lê linha 1
print(empre.readline()) #Lê linha 2
print(empre.readline()) #Lê linha 3
'''

#O Soft a baixo mostra as linhas do texto como se fossem uma Lista Python
empre = open("Funcionarios.txt", "r")

#print(empre.readlines())
#print(empre.readlines()[2]) #Somente a Posição 2 (0,1,"2") dos nomes contidos no .TXT

for empregado in empre.readlines(): #Mostra as linhas com espaçoes entre elas.
    print(empregado)
empre.close()

#leit = empre.read()
#print(leit) # Printa o Arquivo Exatamente como ele é


# Continua em 3:21:26 Escrevendo Arquivos
#   https://www.youtube.com/watch?v=rfscVS0vtbw&feature=youtu.be
