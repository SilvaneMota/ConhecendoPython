#
# Exemplo de como criar classes
#

class minhaClasse():
    def __init__(self):
        self.meuAtributo = "Passou pelo Construto!"

    def meuMetodo(self):
        print("Passou pelo meuMetodo")

    def meuMetodos2(self, valor):
        self.outroatibuto = valor
        print(self.outroatibuto)

def criaObjeto():
    meuObj = minhaClasse()
    var1 =meuObj.meuAtributo
    print(var1)

    meuObj.meuMetodo()

    meuObj.meuMetodos2("Executando um método") 

criaObjeto()    