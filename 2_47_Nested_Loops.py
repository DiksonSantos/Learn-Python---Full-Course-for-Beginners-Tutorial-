number_grid = [
    ["Alpha",1,2,3],
    ["Bravo",4,5,6],
    ["Charlie",7,8,9],
    ["Delta",0]
]

#Linha 1 Coluna 1 = "Alpha"
print(number_grid[0][0])

#Linha 1 Coluna 0 = "Bravo"
print(number_grid[1][0]) #Pode selecionar 0 para Alpha , 1 Para Bravo Etc... #


for row in number_grid: #Imprime Todos Os Arrays\Itens da Lista
    print(row)

print("\n")

'''
#Imprime TODOS os Itens
for row in number_grid:
    for col in row:
        print(col)
'''
