from Exercicio_110_B import moeda, metade, dobro, aumentar, diminuir

def formatacao(p, a, r):
    print("+-" * 20)
    print(f"{'RESUMO DO VALOR':^40}")
    print("+-" * 20)
    print(f"Preço analisado: {moeda(p):>20}")
    print(f"Dobro do preço:  {dobro(p):>20}")
    print(f"Metade do preço: {metade(p):>20}")
    print(f"{a}% de aumento:  {aumentar(p, a):>20}")
    print(f"{r}% de redução:  {diminuir(p, r):>20}")
    print("+-" * 20)

