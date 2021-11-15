
def metade(num):
    num /= 2
    return moeda(num)


def dobro(num):
    num *= 2
    return moeda(num)


def aumentar(num, taxa):
    resp = num + (num * taxa / 100)
    return moeda(resp)


def diminuir(num, taxa):
    resp = num - (num * taxa / 100)
    return moeda(resp)


def moeda(num = 0, moeda = 'R$'):
    return f"{moeda}{num:.2f}".replace('.', ',')


def formatacao(p, a=False, r=False):
    print("+-" * 20)
    print(f"{'RESUMO DO VALOR':^40}")
    print("+-" * 20)
    print(f"Preço analisado: {moeda(p):>20}")
    print(f"Dobro do preço:  {dobro(p):>20}")
    print(f"Metade do preço: {metade(p):>20}")
    print(f"{a}% de aumento:  {aumentar(p, a):>20}")
    print(f"{r}% de redução:  {diminuir(p, r):>20}")
    print("+-" * 20)