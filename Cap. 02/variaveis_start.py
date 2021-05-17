
# Declarando e inicializando uma variável
f = 0 
print(f)

# declarando a mesma variável novamente
f = "abc"
print(f)

# Gerando um erro, tentando unir variáveis de tipos diferentes

print("Isto é uma String " + str( 123))

# Variável Global X Variável local 
def algumafuncao():
    global f
    f = "def"
    print(f)

algumafuncao()
print(f)

