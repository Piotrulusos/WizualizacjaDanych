plt.figure(figsize=(8, 6)): Ta komenda tworzy nową figurę (wykres) o określonym rozmiarze. Parametr figsize przyjmuje krotkę (szerokość, wysokość) w calach i definiuje rozmiar wykresu. W tym przypadku, (8, 6) oznacza, że szerokość wykresu wynosi 8 cali, a wysokość wynosi 6 cali.

df_gender.plot(kind='bar', color=['blue', 'pink']): Ta komenda tworzy wykres słupkowy na podstawie danych z DataFrame df_gender. Parametr kind='bar' wskazuje, że chcemy stworzyć wykres słupkowy. Parametr color pozwala na określenie kolorów słupków. Tutaj używamy niebieskiego i różowego koloru dla chłopców i dziewczynek.

plt.xlabel('Płeć'): Ta komenda dodaje etykietę do osi X. W tym przypadku, etykieta to 'Płeć', co informuje o tym, co przedstawia oś X (czyli płcie).

plt.ylabel('Liczba urodzeń'): Ta komenda dodaje etykietę do osi Y. W tym przypadku, etykieta to 'Liczba urodzeń', co informuje o tym, co przedstawia oś Y (czyli liczbę urodzeń).

plt.title('Liczba urodzonych dzieci według płci'): Ta komenda dodaje tytuł do wykresu. W tym przypadku, tytuł to 'Liczba urodzonych dzieci według płci', który opisuje ogólny temat wykresu.

plt.show(): Ta komenda wyświetla wygenerowany wykres. Bez niej wykres nie byłby wyświetlany na ekranie. Funkcja show() jest używana na końcu, po wszystkich operacjach na wykresie, aby wyświetlić go w interaktywnym oknie.


