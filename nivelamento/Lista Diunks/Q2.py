rodando = True
nome = input()
senha = input()

while rodando:
    if nome == senha:
        print("erro")
        nome = input()
        senha = input()
    else:
        print("tudo certo")
        rodando = False    