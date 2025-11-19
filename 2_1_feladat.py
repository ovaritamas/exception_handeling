szamok_listaja = []
for i in range (1, 4):
    while True:
        try:
            szam = int(input(f'Adj meg egy számot: {i}'))
            szamok_listaja.append(szam)
            break
        except ValueError:
            print("Számot adjál meg")
print(szamok_listaja)