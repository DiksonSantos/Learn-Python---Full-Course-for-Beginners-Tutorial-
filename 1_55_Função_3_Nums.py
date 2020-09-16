#Vai sempre mostrar apenas o Numero MAIOR:
def max_num(N1, N2, N3):
    if N1 >= N2 and N1 >= N3:
        return  N1
    elif N2 >= N1 and N2 >= N3:
        return N2
    else:
        #return  N3
        print(N3)

#print(max_num(300,40,305))
max_num(1,2,0) #UM e DOIS não funcionariam aqui, pois o RETURN necessita de PRINT para funcionar.
