produto_1 =(input("digite o nome do produto: "))
quantidade_produto_1 = int(input("digite a quantidade de produtos: "))
valor_produto_1= float (input("digite o preço do produto: "))
valor_total_prod_1 = quantidade_produto_1 * valor_produto_1

produto_2 =(input("digite o nome do produto: "))
quantidade_produto_2 = int(input("digite a quantidade de produtos: "))
valor_produto_2= float (input("digite o preço do produto: "))
valor_total_prod_2 = quantidade_produto_2 * valor_produto_2

produto_3 =(input("digite o nome do produto: "))
quantidade_produto_3 = int(input("digite a quantidade de produtos: "))
valor_produto_3= float (input("digite o preço do produto: "))
valor_total_prod_3 = quantidade_produto_3 * valor_produto_3

preço_todos_prod = (valor_total_prod_1 + valor_total_prod_2 + valor_total_prod_3)

print (f"o preço do total do produtos e: R${preço_todos_prod: ,.2f}")