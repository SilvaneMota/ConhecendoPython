#
# Escrevendo arquivos com funções do Python
#

def escreveArquivo():
    arquivo = open("NovoArquivo.txt", "w+")

    arquivo.write("Linha Gerada com a Funcao 'EscreveArquivo' \r\n")

    arquivo.close()

#escreveArquivo()

def alteraArquivo():
    arquivo = open("NovoArquivo.txt", "a+")

    arquivo.write("Linha Gerada com a Funcao 'AlteraArquivo' \r\n")

    arquivo.close()

alteraArquivo()