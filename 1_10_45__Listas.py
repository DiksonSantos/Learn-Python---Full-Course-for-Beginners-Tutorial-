

'''
amigos = ['Ana', 'Karen', 'Jimmy', 'Gun', 'Triger', 'Boson','Thompson']
#print(amigos)
amigos[1] = 'D_Santos'   #Substituiu o Segundo Item da Lista (Ou Indice 1)
Mais = 'Eu mesmo'
amigos.append(Mais)
print(amigos)
'''

'''
#Funções de Listas:
Numeros_Da_Sorte = [ 2, 5, 6, 8, 0, 10, 3, 42]
Guarda_Nums = Numeros_Da_Sorte.sort()
amigos = ['Ana', 'Karen', 'Jimmy', 'Gun', 'Triger', 'Boson','Thompson', 'Boson']

amigos.extend(Numeros_Da_Sorte) #!!!
amigos.append('Dikson')
amigos.insert(1, 'Gow')  #ESTE NÃO SUBSTITUI, MAS EMPURRA OS PROXIMOS p\ direita
#amigos.remove('Gun')
#amigos.clear()  #LIMPA A LISTA

print(amigos)
try:
    Consulta = str(input('Procure na Lista: '))
    print(amigos.count(Consulta), 'Elemento(s) Com este Valor Consta(m) Na Lista')
    print('Elemento(s) Na Posição: ', amigos.index(Consulta))

    print('Numeros Na Ordem', Guarda_Nums)
except ValueError:
    print('Valor Não Encontrado')


'''
#De outra Forma Não Funiona
Numeros_Da_Sorte = [ 2, 5, 6, 8, 0, 10, 3, 42]
Numeros_Da_Sorte.sort()  #Coloca do Menor para o Maior
print(Numeros_Da_Sorte)
Numeros_Da_Sorte.reverse() #Do Maior Para o Menor
print(Numeros_Da_Sorte)

amigos = ['Ana', 'Karen', 'Jimmy', 'Gun', 'Triger', 'Boson','Thompson', 'Boson']
Amigos_2 = amigos.copy()
print(Amigos_2) #Copia de Amigos Em Amigos_2

#CONTINUA EM 1:18:57 TUPLAS
#   https://www.youtube.com/watch?v=rfscVS0vtbw&feature=youtu.be

