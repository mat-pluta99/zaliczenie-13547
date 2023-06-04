# Zaliczenie Mateusz Pluta 13547
Testy zostały przeprowadzone na zmodyfikowanej wersji mojej aplikacji symulującej grę w BlackJack, napisanej w języku Python.

Program został oparty o klasy obiektów Gracza, Kart i Talii. Przy jego obsłudze działają różne funkcje, służące do prowadzenia rundy gry karcianej.

Zastosowane bilbioteki: unittest

## Scenariusze
Test jednostkowy:

Rozpoczęcie rundy.
Wyświetlenie przebiegu rundy.
Otrzymanie informacji o wyniku i zakończenie gry.
Spodziewany efekt: gra kończy się otrzymaniem wyniku Rezultat: gra kończy się otrzymaniem wyniku

Test integracyjny A:

1. Zainicjowanie talii
2. Zainicjowanie gracza
3. Gracz dobiera kartę
Spodziewany efekt: talia kart zostaje zmniejszona o 1, czyli wynosi 51 Rezultat: Otrzymujemy błąd o nieprawidłowej ilość kart w talii

Test integracyjny B:

1. Zainicjowanie gracza
2. Zainicjowanie dealera
3. Zainicjowanie talii
4. Gracz dobiera kartę
5. Dealer dobiera kartę
6. Gracz dobiera kartę
7. Porównanie ilości kart gracza i dealera
Spodziewany rezultat: gracz ma większą ilość kart 
Rezultat: gracz ma większą ilość kart

Niestety, nie udało mi się wykonać testu akceptacji ze względu na problemy dotyczące wykrywania dodatkowych bibliotek przez interpreter
