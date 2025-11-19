osztando = 10
try:
    oszto = int(input(f"Mennyivel osszam el a(z) {osztando} számot:"))
    print(f'A {osztando} és {oszto} hányadosa: {osztando/oszto}')
except ZeroDivisionError as e:
    print(e)
    print("Ne osszá nullával")
except ValueError as e:
    print(e)
    print("Számot...légyszives...köszii")