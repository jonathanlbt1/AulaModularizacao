# Exercicio 109 - Formatando moedas em Python: Part 2
from Exercicio_109_B import moeda, metade, dobro, aumentar, diminuir

preco = float(input("Digite o preço: R$"))

print(f"A metade de {moeda(preco)} é {metade(preco)}")
print(f"O dobro de {moeda(preco)} é {dobro(preco)}")
print(f"Aumentando 10%, temos {aumentar(preco, 10)}")
print(f"Reduzindo 13%, temos {diminuir(preco, 13)}")