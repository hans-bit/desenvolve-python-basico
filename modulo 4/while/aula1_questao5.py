n_respondente = int(input("digite o numerode pessoa: "))
soma = 0
cont = 0
while cont < n_respondente:
    idade = int(input("digite as idades: "))
    soma += idade
    cont +=1
print (f" idade total é: {soma}") 
print (f"a media das idades é: {soma/n_respondente}")






