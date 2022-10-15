
qtdArq = int(input("Quantidade de arquivos: "))
iniciais = str(input("Iniciais do arquivo: "))
if qtdArq > 2 or qtdArq < 1:
    print("False")
elif iniciais == "BKP" or iniciais == "BackUp":
    print("True")
else:
    print("False")