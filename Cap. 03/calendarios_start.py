#
# Arquivo com exemplos de uso de calendários
#

import calendar

# criando um calendário no formato texto
def calendarioTexto():
    calendarioTexto = calendar.TextCalendar(calendar.SUNDAY)
    calendar.TextCalendar = calendarioTexto.formatmonth(2020,5)
    print(calendar.TextCalendar)

calendarioTexto()

# Criando um calendário no formato HTML

def calendarioHTML():
    calendarioHTML = calendar.HTMLCalendar(calendar.SUNDAY)
    HTMLCalendario = calendarioHTML.formatmonth(2020,5)
    print(HTMLCalendario)

calendarioHTML()

# loop ao longo dos dias de um mês






