import random

body = int(0)

def nasobeni(a, b):
    vysledek = (a * b)
    return vysledek

def kontrola(c, d):
    if c == d:
        (body + 1)
        print("Správně")
        return True
    else:
        print("Špatně")
        return False


for _ in range(10):
    x = random.randint(1,10)
    y = random.randint(1,10)
    vysledek = nasobeni(x, y)
    
    vysledek_zak = input(f"{x} * {y} = ")
    vysledek_zak = int(vysledek_zak)

    if kontrola(vysledek_zak,vysledek):
        continue
    else:
        print("Zkus znovu")
print(body)
#udělj body aby fungovali#