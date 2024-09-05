# Enunciado: Uma loja aplica um imposto de 12% sobre o valor dos produtos. Crie um programa que receba o preço de um produto e calcule o preço final com o imposto incluído.
p1=float(input("valor do seu produto"))

v=p1*(21/100)
v2=p1+v
print(f"preço com imposto {v2}")