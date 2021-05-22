#
# Arquivo com exemplos de manipulação de  datas
#
from datetime import date
from datetime import time
from datetime import datetime

def ManipulaDataHora():
    hoje = date.today()
    print("hoje é: ", hoje)
    print ("Dia :", hoje.day, "Mes :", hoje.month,"Ano :", hoje.year)
    print ("Numero do dia da semana :", hoje.weekday())
    dias = ["Seg","ter","quar","quin","sex","sab","dom"]
    print("nome abreviado do dia da semana: ", dias[hoje.weekday()])

    data = datetime.now()
    print("Data e Hora: ", data)

    Tempo = datetime.time(data)
    print("Hora Atual :", Tempo)

ManipulaDataHora() 
