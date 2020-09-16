class Estudante:
    def __init__(self, nome, Curso, Nota):
        self.Nome = nome
        self.Major = Curso
        self.Gpa = Nota
        #No exemplo do Instrutor, as duas linhas de baixo não Existem.
        infos = nome + Curso + str(Nota)
        print(infos)



    def Roll_Da_Honra(self):
        if self.Gpa >= 3.4:
            return True
        else:
            return  False

Fulano_01 = Estudante("Oscar ", 'Instrutor, Nota: ', 9.9)
print("Esta no Roll Da Honra? ",Fulano_01.Roll_Da_Honra())
#print(Fulano_01)

Cicrano01 = Estudante('\nWillis',' Professor ', 3.2)
print("Esta no Roll Da Honra? ",Cicrano01.Roll_Da_Honra())


