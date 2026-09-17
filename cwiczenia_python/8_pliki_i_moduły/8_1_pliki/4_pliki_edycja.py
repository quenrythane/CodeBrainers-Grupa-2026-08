

plik_do_edycji = "plik_do_edycji.txt"

# otwieramy plik i zczytujemy jego treść do zmiennej lista_linii
with open(plik_do_edycji, "r") as mój_plik:
   lista_linii = mój_plik.readlines()

# definiujemy niechciane linie - Wymyśliśmy sobie, że są to linie o indeksie dwa i trzy.
cezary = lista_linii[2]
dawid = lista_linii[3]

# usuwamy niechciane linie
lista_linii.remove(cezary)
lista_linii.remove(dawid)

# nadpisujemy plik plik_do_edycji metodą writelines() z argumentem lista_linii
with open(plik_do_edycji, "w") as mój_plik:
    mój_plik.writelines(lista_linii)

