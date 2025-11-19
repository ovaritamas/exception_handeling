osztando = 10
try:
    oszto = int(input("Mennyivel osszam el a(z) {osztando} számot:"))
    print(f'A {osztando} és {oszto} hányadosa: {osztando/oszto}')
except ZeroDivisionError:
    print("Ne osszá nullával")
