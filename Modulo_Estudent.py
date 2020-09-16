class Student:
    def __init__(self, nome, formation, gpa, is_on_probation):
        self.Nome = nome
        self.Formation = formation
        self.GPA = gpa
        self.probation = is_on_probation

        #Tudo = nome ,formation ,gpa ,is_on_probation #Fica bem tosco
        print(nome," ",formation," ",gpa," ",is_on_probation)

