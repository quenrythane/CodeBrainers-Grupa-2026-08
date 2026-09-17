

nazwa_pliku = "plik_do_dopisania.txt"

# otwarcie pliku
plik_xd = open(nazwa_pliku, "a")

# zapis w pliku
plik_xd.write("\nLinia 4")

# zapis w pliku
plik_xd.write("Linia xd")
plik_xd.writelines(["Linia 1", "Linia 2"])

# zamknięcie pliku
plik_xd.close()
