krotka = ("Artur", "Basia", "Czarek", "Artur")

print("Oryginalna krotka:", krotka)
print("Pierwszy element krotki:", krotka[0])

""" Krotek nie można modyfikować. """
# krotka[0] = "Marek"  # ta linijka zwróciłaby błąd
print("Krotka po nieudanej próbie modyfikacji:", krotka)

""" Można to obejść, zamieniając na moment krotkę w listę, a potem na powrót zamieniając ją w krotkę.  """
krotkolista = list(krotka) # zamiana na moment na liste
krotkolista[0] = "Marek"  # modyfikacja listy
krotka = tuple(krotkolista)  # przywrócenie listy w krotke
print("Krotka po edycji:", krotka)
