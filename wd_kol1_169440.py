# zad1
import math
import random
for x in range(13,30):
    wynik = math.pow(math.pow(math.e, x) + math.cos(x),1/4)
    ostateczny_wynik = round(wynik, 2)
    print(ostateczny_wynik)
# zad2
def zadanie2(min, max, ile):
    lista = []
    licznik = 0
    while licznik < ile:
        i = random.randint(min, max)
        lista.append(i)
        licznik += 1
    print(lista)
    slow = {}

    for element in lista:
        if element in slow:
            slow[element] += 1
        else:
            slow[element] = 1
    return slow

try:
    print(zadanie2(1, 3, 4))
except:
    print("Error")

# zad3
def oblicz_sume(nazwa_pliku):
    suma_wierszy = 0
    suma_kolumn = 0

    with open(nazwa_pliku, 'r') as file:
        lines = file.readlines()
        for line in lines:
            suma_wierszy += sum(map(int, line.split()))

        columns = zip(*[map(int, line.split()) for line in lines])
        suma_kolumn = sum(map(sum, columns))


    return suma_wierszy, suma_kolumn

suma_wierszy, suma_kolumn = oblicz_sume("liczby 1.txt")
print("Suma elementów z wszystkich wierszy:", suma_wierszy)
print("Suma elementów z wszystkich kolumn:", suma_kolumn)


# zad4
import sys
def zadanie4():
    sys.stdout.write('Podaj a i h')
    a = int(sys.stdin.readline())
    h = int(sys.stdin.readline())
    wynik = (a * a) * h
    return wynik

try:
    print(zadanie4())
except:
    print("Błąd wczytania wartości.")




