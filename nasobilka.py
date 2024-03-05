import random


def nasobeni(a, b):
    vysledek = (a * b)
    return vysledek

def kontrola(c, d):
    body = False
    if (c == d):
        print("Správně")
        body = True
    else:
        print("Špatně")
        return kontrola
    return body

#udělej aby to generovalo 10 příkladů#
x = random.randint(1,10)
y = random.randint(1,10)
vysledek = nasobeni(x, y)

vysledek_zak = input(f"{x} * {y} = ")
vysledek_zak = int(vysledek_zak)
kontrola(vysledek_zak, vysledek)
