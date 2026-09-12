

# print("1")
# print("2")
# print("3")
# print("4")
# print("5")
# print("6")
# print("7")
# print("8")
# print("9")
# print("10")


"""
for element in iterable:
    co ma się wykonać dla każdego obiegu z elementem
"""

lista_liczba = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for liczba in lista_liczba:
    # print("pętla:", liczba)


lista_imion = ["Adam", "Basia", "Cezary", "Damian", "Ewa"]

print("Ręczene cześć")
print(f"Cześć {lista_imion[0]}!")
print(f"Cześć {lista_imion[1]}!")
print(f"Cześć {lista_imion[2]}!")
print(f"Cześć {lista_imion[3]}!")
print(f"Cześć {lista_imion[4]}!")
print("\n\n")

print("Pętla for cześć:")
for imie in lista_imion:
    print(f"Cześć {imie}!")

print("koniec programu")
