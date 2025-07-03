
n_exp = int(input("digite o numero de experimentos: "))
cont = 0
soma_sapos, soma_coelhos, soma_ratos = 0,0,0
while cont < n_exp:
    tipo = input("digite o tipo de animal usado: ")
    quantia = int(input("digite a quantia de cobais usadas: "))
    
    if tipo == 'sapo':
        soma_sapos += quantia
    elif tipo == 'rato':
        soma_ratos += quantia
    elif tipo == 'coelho':
        soma_coelhos += quantia
    cont += 1

print(f"total de cobaias:  {soma_coelhos+soma_sapos+soma_ratos}")
print(f"total de coelhos: {soma_coelhos}")
print(f"total de ratos: {soma_ratos}")
print(f"total de ratos: {soma_sapos}")

print(f"porcentagem de coelhos: {soma_coelhos/n_exp}")
print(f"porcentagem de ratos: {soma_ratos/n_exp}")
print(f"porcentagem de ratos: {soma_sapos/n_exp}")

