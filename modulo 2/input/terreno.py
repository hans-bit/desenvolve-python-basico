# leitura de dados

comprimento = int(input("digite o comprimento"))
largura = int(input("digite a largura"))
preço = float(input("digite o preço"))

#processamento

area = comprimento * largura
preço_total = area * preço

#impressao de dados

print(f"o preço do terreno {area}m2 e custa {preço_total:,.2f} ")