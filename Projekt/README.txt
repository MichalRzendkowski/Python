Projekt: Implementacja "Conway's Game of Life" w aplikacji okienkowej

===========================================================================
Problem:

Game of life to automat komórkowy. Jest on reprezentowany na siatce
kwadratowych pól. Każda komórka może być "żywa" lub "martwa". W następnych
pokoleniach stan komórek zmienia się zgodnie z kilkoma zasadami:

* Martwa komórka, która ma dokładnie 3 żywych sąsiadów,
     staje się żywa w następnej jednostce czasu (rodzi się)
* Żywa komórka z 2 albo 3 żywymi sąsiadami pozostaje nadal żywa;
     przy innej liczbie sąsiadów umiera (z „zatłoczenia”)

===========================================================================
Interfejs:

Główna część interfejsu składa się z siatki kwadratowych przycisków
reprezentujących komórki. Naciśnięcie przycisku zmienia jego stan na
przeciwny.

W górnej częsci okna znajdują się przyciski (od lewej):

* Do manualnej zmiany stanu na następny.
* Do startu/pauzy automatycznej zmiany stanów.
* Do przyspieszenia automatycznej zmiany stanów.
* Do zwolnienia automatycznej zmiany stanów.
* Do zmiany wszystkich komórek na "martwe".

===========================================================================
Implementacja:

Program używa biblioteki tkinter do rysowania interfejsu.

W pliku main.py znajduje się główna implementacja interfejsu i przycisków.
Ten plik należy otworzyć aby uruchomić program.

W pliku grid.py znajduje się implementacja klasy Grid (dziedziczącej po
tk.Label), która odpowiada za rysowanie siatki przycisków składających się
na automat.

W pliku game.py znajduje się implementacja klasy GameOfLife, odpowiadającej
za logikę automatu.

Folder /images zawiera pliki z ikonami na przyciski interfejsu.
