#
# Arquivo com exemplos de como trabalhar com paths
#

from os  import path
import time

def dadosArquivo():
    arquivoExiste = path.exists("NovoArquivo.txt")
    ehDiretorio = path.isdir ("NovoArquivo.txt")
    pathArquivo = path.realpath ("NovoArquivo.txt")
    pathRelativo = path.relpath ("NovoArquivo.txt")
    dataCriacao= time.ctime(path.getctime("NovoArquivo.txt"))
    dataModicacao = time.ctime(path.getmtime("NovoArquivo.txt"))

    print(arquivoExiste)
    print(ehDiretorio)
    print(pathArquivo)
    print(pathRelativo)
    print (dataCriacao)
    print(dataModicacao)

dadosArquivo()
