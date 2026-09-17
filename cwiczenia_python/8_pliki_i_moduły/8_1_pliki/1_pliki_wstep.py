

nazwa_pliku = "plik_xd.txt"
poziom_uprwanien_read = "r"

""" Otwieramy plik i przechowujemy go w zmiennej o nazwie `plik_xd`.  """
plik_xd = open(nazwa_pliku, poziom_uprwanien_read)

""" Odczytujemy całą zawartość pliku.  """
# print(plik_xd.read())

""" Odczytujemy linię po linii.  """
# print("To jest linia nr 1: ", plik_xd.readline())
# print("To jest linia nr 2: ", plik_xd.readline())
# print("To jest linia nr 3: ", plik_xd.readline())
# print("To jest linia nr 4: ", plik_xd.readline())

""" Odczytujemy wszystkie linie jako listę.  """
# print("To jest lista wszystkich linii: ", plik_xd.readlines())