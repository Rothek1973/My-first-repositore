import string

# pusta lista - inicjacja, poza klasa aby byla dostepna w petlach
MojaLista = []

class Szyfr:

# inicjacja argumentu malych i duzych liter (American Standard Code for Information Interchange)
    malelitery = string.ascii_lowercase
    DUZELITERY = string.ascii_uppercase

# wydruk czesci alfabetu w jakim zakresie mozna dobierac litery do tekstu
    print(malelitery)
    print(DUZELITERY)

# wprowadzenie ciagu znakow jako string
    slowo = input("Podaj tekst do szyfrowania: ")

# wprowadzenie przesuniecia o ile w stosunku do alfabetu. Zastosowalem "__" jako bezpieczenstwo dostepu.
    __PrzesuniecieSzyfrowaniaKlucz = int(input("Klucz: "))

# petla for sprawdza w dlugosci wprowadzonego ciagu znakow czy sa duze czy male litery
# nastepnie znajduje odpowiednia litere w ASCII i przesuwa ja o "zmiana", liter w alfabecie jest 26 dlatego jest
# zastosowane modulo "%" czyli reszta z dzielenia wychodzi przesuniecie o 1
    for i in range(len(slowo)):
        if slowo[i] in malelitery:
            indeks = malelitery.find(slowo[i])
            zmiana = malelitery[(indeks + __PrzesuniecieSzyfrowaniaKlucz) % 26]
            MojaLista.append(zmiana)
            print(MojaLista)
        elif slowo[i] in DUZELITERY:
            indeks = DUZELITERY.find(slowo[i])
            zmiana = DUZELITERY[(indeks + __PrzesuniecieSzyfrowaniaKlucz) % 26]
            MojaLista.append(zmiana)
            print(MojaLista)
        else:
            MojaLista.append(slowo[i])

#polaczenie list duzych i malych liter (Liste Comprehension)
    MojSzyfr = "".join(MojaLista[i] for i in range(len(MojaLista)))
    print("Wynik - ", MojSzyfr)

s=Szyfr()