
'''
#print(2**3) #2 Elevado a 3 (Potenciação)

def potencia(Base, Pot):
    return Base * Pot

Objeto = potencia(1,2)
print(Objeto)


def Pot_(Num, Expo):
    Bases = Num
    Pote = Expo
    Res = Bases ** Pote
    print(Res)

#Obj = Pot_(2,3) #Dois Elevado a Três

Num_1 = float(input("Numero_Base: "))
Num_2 = float(input("Elevado a: "))

Exemple_ = Pot_(Num_1, Num_2)
'''

def raise_to_power(Base_Num, Pow_Num):
    res = 1 # Aqui é uma variavel Temporaria, ela tem que ter qualquer valor nela, se não não funciona
    for index in range(Pow_Num): #Dependendo do numero que se insere em Segundo ou o Numero da Potencia
        res = res * Base_Num #O Laço FOR vai transformar o 1 de res no numero que for Inserido em Pow_Num, pois...
#... o IN Range vai fazer isso quantas vezes de acordo com o numero inserido em Pow_Num
#.. e Vai fazer isto VEZES o Numero Da Base.
    return res
print(raise_to_power(2,4))
# Complicação desnecessária (a do autor). Somente para usar o FOR.

#Continua em 2:47:14 -> 2D List & Nested Loops
