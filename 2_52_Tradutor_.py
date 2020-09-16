def tradutor(frase):
    traduc = ""
    for carta in frase:
        if carta.lower() in "aeiou": #O LOWER Eliminou a Necessidade de precisar de letras Maiusculas E Minusculas a frente do IN
            if carta.isupper():
                traduc = traduc + "G"
        else:
            traduc = traduc + "g" #Com esta modificação é possivel manter a Peimeira Letra MAIUSCULA (Vai ser Substituida por "G"
            #traduc = traduc + carta
    return traduc

print(tradutor(input("Digite a Palavra: "))) #PRINT Devido á FUnção NÃO ter PRINT, Tradutor=> Nome Da Função...
#...Embutimos um INPUT na função para Introduzir as informações\Palavra dentro da Função Como Parametro.



#Continua em 3H 00:18Seg  Comments
