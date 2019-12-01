# Warsztat: Symulator LOTTO.
# Jak wszystkim wiadomo, LOTTO to gra liczbowa polegająca na losowaniu 6 liczb z zakresu 1–49. Zadaniem gracza
# jest poprawne wytypowanie losowanych liczb. Nagradzane jest trafienie 3, 4, 5 lub 6 poprawnych liczb.
#
# Napisz program, który:
#
# zapyta o typowane liczby, przy okazji sprawdzi następujące warunki:
# czy wprowadzony ciąg znaków jest poprawną liczbą,
# czy użytkownik nie wpisał tej liczby już poprzednio,
# czy liczba należy do zakresu 1-49,
# po wprowadzeniu 6 liczb, posortuje je rosnąco i wyświetli na ekranie,
# wylosuje 6 liczb z zakresu i wyświetli je na ekranie,
# poinformuje gracza, czy trafił przynajmniej "trójkę".

import random
lotto = [i for i in range(1, 50)]
los = random.sample(lotto, 6)
liczby = []
i = 1
while i <= 6:
    try:
        liczba = int(input(f'Podaj liczbę {i}: '))
        if liczba not in liczby and liczba in lotto:
            liczby.append(liczba)
            i += 1
        else:
            print('Podana liczba wykracza poza zakres od 1 do 49 lub została już raz podana')
    except (ValueError, TypeError):
        print("To nie jest liczba")

liczby.sort()
print(liczby)
print(los)
comp = sum([liczby[i] in los for i in range(0,5)])
if comp >= 3:
    print(f'Trafiłeś {comp}!')


