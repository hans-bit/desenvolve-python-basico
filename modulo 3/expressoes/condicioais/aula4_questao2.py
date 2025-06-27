filme = (input("escolha um filme: "))
alvaliaçao_filme = int(input("digite sua avaliaçao sobre o filme: "))
if alvaliaçao_filme == 1:
    print("ruim")
elif alvaliaçao_filme == 2:
    print("regular")
elif alvaliaçao_filme == 3:
    print("bom")
elif alvaliaçao_filme == 4:
    print("muito bom")
elif alvaliaçao_filme == 5:
    print("otimo")
else:
    print("avaliaçao invalida, digite um numero de 1 a 5")