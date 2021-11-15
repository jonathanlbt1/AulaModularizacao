
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
