#
# Exemplo de como usar os comando Break e Continue
#
def loopBreak():
    for x in range(5,10):
        if x == 10:
            break
        print("O valor de x é: ", x)

#loopBreak() 

def loopContinue():
    for x in range (0,10):
        if x == 7:
            continue
        print ("o valor de x é: ", x)

loopContinue()    
