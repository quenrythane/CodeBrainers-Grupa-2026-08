

nazwa_pliku = "plik_do_pisania.txt"
poziom_uprwanien_write = "w"

# otwarcie pliku
plik_xd = open(nazwa_pliku, poziom_uprwanien_write)

# zapis w pliku
plik_xd.write("Linia 4")

# zapis w pliku
plik_xd.write("\nLinia xd")

# zamknięcie pliku
plik_xd.close()
