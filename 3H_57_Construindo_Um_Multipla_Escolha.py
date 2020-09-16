from Question import  Question

#Esta lista a baixo tem 3 Itens 0 0,  1, e o 2.
Question_Promts = [
    "Que cor é a Laranja?\n(a) Vermelha/Verde\n(b) Roxa\n(c) Laranja\n\n",
    "Que cor é a banana?\n(a) Azul\n (b) Magenta\n(c) Amarela\n\n",
    "Que cor são os morangos?\n(a) Amarelos\n(b) Vermelhos\n(c) Azuis\n\n",
    "Que cor São os bacates?\n(a)Verdes\n(b) Rosa\n(c) Roxos"
]

#Aqui nessa Lista [QUASTIONS] estão definidas as respostas corretas.
#Os MODULOs\Objetos Question (from Question...) estão dentro desta lista.
#Dentro da Lista QUASTIONS temos a função Question chamada 3 vezes
#Acredito eu que: a Função run_test possa reconhecer que Question_Promts[0] 'É = letra -> "c"
#Aqui a baixo é a Função/Modulo Question.py agindo; Foram passador a ela 2 parametros o Primeiro foi -> Question_Promts[0],
#... e o Segundo foi "c"
quastions = [
    Question(Question_Promts[0], "c"),
    Question(Question_Promts[1], "c"),
    Question(Question_Promts[2], "b"),
    Question(Question_Promts[3], "a")
]

#Esta função 'Lê' a QUASTIONS para identificar se o Segundo Parametro passado é igual ao valor digitado pelo Usuario.
def run_test(questions): #Engraçado que ela lê QUASTIONS, mas o que esta digitado no argumento é 'questions' (???)
    score = 0
    for question in questions:
        answer = input(question.Prompt+ "Digite A B ou C: ") #Se o que o Usuario digitou...
        if answer == question.Answer: #...for igual ao segundo parametro guardado pela função "Question.py"
            #...ou seja -> Se Question for Igual a Answer;
            score += 1 #...A Variavel 'score' recebe +1
 #O LEN 'questions' conta quantas entradas de informação houveram, devido a se tratar de um laço FOR, isto é possível:
    print("\nYou got " + str(score) + " Of " + str(len(questions)) + " Correct")
run_test(quastions)


'''
Depois de dar uma boa avaliada neste codigo, continuem em 4:08:31
Object Funcions
'''
#4:08:30
#   https://www.youtube.com/watch?v=rfscVS0vtbw&feature=youtu.be&t=14258
