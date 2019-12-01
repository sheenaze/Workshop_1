# Napisz prostą grę w zgadywanie liczb. Komputer musi wylosować liczbę w zakresie 1 – 100. Następnie:
#
# Zadać pytanie: "Zgadnij liczbę" i pobrać liczbę z klawiatury.
# Sprawdzić, czy wprowadzony napis, to rzeczywiście liczba i w razie błędu wyświetlić komunikat "To nie jest liczba", po czym wrócić do pkt. 1
# Jeśli liczba podana przez użytkownika jest mniejsza niż wylosowana, wyświetlić komunikat "Za mało!", po czym wrócić do pkt. 1.
# Jeśli liczba podana przez użytkownika jest większa niż wylosowana, wyświetlić komunikat "Za dużo!", po czym wrócić do pkt. 1.
# Jeśli liczba podana przez użytkownika jest równa wylosowanej, wyświetlić komunikat "Zgadłeś!", po czym zakończyć działanie programu.

import random
gen_liczba = random.randint(1, 100)
liczba = False
while liczba == False:
    dana_liczba = input('Zgadnij liczbę: ')
    try:
        liczba = int(dana_liczba)
    except (ValueError, TypeError):
        print("To nie jest liczba")
    if liczba < gen_liczba:
        liczba = False
        print('Za mało')
    elif liczba > gen_liczba:
        liczba = False
        print('Za dużo')
    else:
        print("zgadłeś!")

