import random
import math

n = int(input("Digite a quantidade de valores inteiros a serem gerados: "))
soma = 0
for i in range (n):
    valor = random.randint(0,100)
    print(valor)
    soma += valor 
    
print (soma)
print(math.sqrt(soma))

