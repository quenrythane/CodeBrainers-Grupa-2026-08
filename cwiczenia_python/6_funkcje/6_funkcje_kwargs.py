
def hello(**osoba):
    for imie, wiek in osoba.items():
        print(f"Hello {imie} ma {wiek} lat")


słownik = {
    "ania": 20,
    "bartek": 25,
    "czarek": 30,
    "damian": 35,
    "ewa": 40
}


hello(ania=20, bartek=25, czarek=30, damian=35, ewa=40)
# hello(słownik=słownik)  # tutaj pojedyncza para key value
hello(**słownik)  # tutaj rozpakowujemy słownik i przekazujemy kazdy element jako osobny argument
