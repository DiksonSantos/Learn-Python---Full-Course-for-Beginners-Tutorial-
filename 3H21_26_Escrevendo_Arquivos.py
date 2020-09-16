'''
Arquivo = open("Funcionarios.txt", "a") # O "a" Aqui significa Append, ele acrecenta linhas ao Arquivo.txt
#print(Arquivo.read())
Arquivo.write("\nKely - Clarkson")
Arquivo.close()
'''

Arquivo = open("Index_TeiXTo.html", "w") # W Re-Escreve o arquivo totalmente, ou Cria um NOVO arquivo de TXT
#print(Arquivo.read())
Arquivo.write("<p>Pagina HTML Feita aqui</p>")
Arquivo.close()


Arquivo = open("Index_TeiXTo.html", "r+")
print(Arquivo.read())


#Continua em 3:28:13
