
lista_potęg = []

for liczba in range(1, 6):
    lista_potęg.append(liczba ** 2)

print("Klasyczna pętla for", lista_potęg)


# lista_potęg_v2 = [liczba ** 2 for liczba in range(1, 6)]
# print(lista_potęg_v2)

wynik = [liczba ** 2 for liczba in range(1, 6)]
print("list comprehension", wynik)

