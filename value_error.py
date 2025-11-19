try:
    szam = int(input("Adj egy egész számot: "))
    print(f'A szám négyzete: {szam ** 2}')
except ValueError:
    print("Számot adjál má teee")