#
# Exemplos de como trabalhar com arquivos
#
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def criaZipModo1():
    shutil.make_archive("ArquivoCompactado", "zip", "C:\\Users\\Silvane\\Desktop\\Projetos Python\\ConhecendoPython\\Cap. 03" )

#criaZipModo1()

def criaZiModo2():
    with ZipFile("ArquivozipModo2.zip", "w") as novoZip:
        novoZip.write("NovoArquivo.bkp")
        novoZip.write("NovoArquivo.txt")
        novoZip.write("ZipModo1.zip.zip")

#criaZiModo2()

def DeletaArquivo():
    os.remove("ArquivozipModo2.zip")

DeletaArquivo()