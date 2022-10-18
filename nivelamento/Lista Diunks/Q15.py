gabarito = "ABCDEEDCBA" 
certo = 0
erro = 0
maiorAcertos = 0
maiorErros = 0 
qtdAlunos = 1
mediaTurma = 0

notas = []

rodando = True
while rodando:
    for i in range(10):
        quest = input()
        if quest == gabarito[i]:
            certo += 1
        else:
            erro += 1 

    notas.append(certo)

    if certo > maiorAcertos:
        maiorAcertos = certo
    if erro > maiorErros:
        maiorErros = erro

    resAlunos = input("Outro aluno vai utilizar?: ")
    if resAlunos == "nao":
        rodando = False
    else:
        certo = 0 
        erro = 0
        qtdAlunos += 1

mediaTurma = sum(notas) / qtdAlunos
print(maiorAcertos)
print(maiorErros)
print(qtdAlunos)
print(round(mediaTurma,2))
    


    