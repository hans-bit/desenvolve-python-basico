
distancia = float(input("digite a distancia: "))
peso = float(input("digite o peso: "))
if distancia <= 100 :
    preço_por_kg = 1
elif distancia >100 <=300:
    preço_por_kg = 1.5
else: 
    preço_por_kg = 2
frete = distancia * preço_por_kg
if peso >10:
   frete += 10

print(f"Valor do frete: R${frete:.2f}")




