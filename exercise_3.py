# Odwróćmy teraz sytuację z warsztatu "Gra w zgadywanie liczb": to użytkownik pomyśli sobie liczbę z zakresu
# 1-1000, a komputer będzie zgadywał i zrobi to maksymalnie w 10 ruchach (pod warunkiem, że gracz nie będzie oszukiwał).
#
# Zadaniem gracza będzie udzielanie odpowiedzi "więcej", "mniej", "trafiłeś".
#
# Do tego warsztatu dołączony jest schemat blokowy algorytmu. Zaimplementuj go w Pythonie.

print('Pomyśl liczbę od 1 do 1000 a ja ją zgadnę w maksymalnie 10 próbach.')

minimum = 0
maximum = 1000
odp =''
i = 1
while odp != 'z':
    guess = int((maximum - minimum) / 2)+minimum
    print(f'Zgaduję: {guess}')
    odp = input("czy podana odpowiedź to za dużo, za mało czy zgadłem [d/m/z]: ")
    if odp == 'd':
        maximum = guess
        i +=1
    elif odp == 'm':
        minimum = guess
        i+= 1
    else:
        print('Nie oszukuj!')

print(f'Wygrałem! Liczba prób: {i}')

