'''
Band = True

while True:
    try:
        num = int(input("Number: "))
        print(num)
    except ValueError:
        print("Digite Apenas Numeros")
        Band = False
    if Band == False:
        break
#Uhuu !!

'''
#CONTINUA EM 3:10:03
#    https://www.youtube.com/watch?v=rfscVS0vtbw&feature=youtu.be

try:
    #value = 10 / 0
    num = float(input("Numero: "))
    NUM = float(input("Outro Numero: "))
    Mat = num / NUM
    print(Mat)
except ZeroDivisionError as err: #ERR vai dar uma mensagem nativa do sistema para este tipo de erro.
    print("Dividido Por ZERO ??!!")
    print(err)
except ValueError:
    print("Entrada Invalida")
