lista = ["Artur", "Basia", "Czarek", "Artur"]
zbior = {"Artur", "Basia", "Czarek", "Artur"}

print(lista)
print(zbior)

""" Zbiorów głównie będziemy używali do zapytań, czy dana rzecz mieści się w zbiorze, czy nie.  """
"Artur" in zbior  # Czy element "Artur" jest w zbiorze 'zbior'? => True
"Artur" not in zbior # Czy element "Artur" NIE jest w zbiorze 'zbior'? => False

imie = "Adam"
print(f"Czy {imie} w zbiorze?:", imie in zbior)

""" Kolejną główną rzeczą, do której będziemy używali zbiorów, jest usuwanie duplikatów.  """
lista_męskich_imion = ["Artur", "Bartosz", "Cezary", "Artur", "Adam", "Bartosz"]
print("Lista imion:", lista_męskich_imion)

zbior_imion = list(set(lista_męskich_imion))
print("Lista imion bez duplikatów:", zbior_imion)



""" przykładowe metody na zbiorach """
zbior.add("Maciek")  # dodaje element do zbioru

zbior.update(["Ania", "Adam"])  # dodaje elementY do zbioru

lista_nowych_imion = {"Ania", "Adam"}
zbior.update(lista_nowych_imion) # dodaje elementY do zbioru
# iterowalny

zbior.remove("Artur")
print(zbior)

""" operacje na zbiorach """
'''
  * odejmowanie od siebie zbiorów:\
  `c = a - b`
  * dodawanie do siebie zbiorów:\
  `c = a | b`
  * część wspólna zbiorów:\
  `c = a & b`
  * część rozłączna zbiorów:\
  `c = a ^ b`
'''






