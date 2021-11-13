# Exercicio 108 - Formatando moedas em Python
import modulo2

preco = float(input("Digite o preço: R$"))

print(f"A metade de {modulo2.moeda(preco)} é {modulo2.metade(preco)}")
print(f"O dobro de {modulo2.moeda(preco)} é {modulo2.dobro(preco)}")
print(f"Aumentando 10%, temos {modulo2.aumentar(preco, 10)}")
