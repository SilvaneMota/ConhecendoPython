#
# Exemplos de como trabalhar com arquivos
#
import os
from os import path
import shutil

def copiaArquivo():
    if path.exists("NovoArquivo.txt"):
        pathAtual = path.realpath("NovoArquivo.txt")
        novopath = pathAtual +".bkp"
        shutil.copy(pathAtual, novopath)

        shutil.copystat(pathAtual, novopath)
    
#copiaArquivo()

def renomearArquivo():
    if path.exists("NovoArquivo.txt.bkp"):
        os.rename("NovoArquivo.txt.bkp", "ArquivoAlterado.txt")

renomearArquivo()