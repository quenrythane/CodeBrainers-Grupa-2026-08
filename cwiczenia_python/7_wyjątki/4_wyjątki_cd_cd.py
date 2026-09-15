
imie = "Adama"

try:
    if imie.endswith("a"):
        raise ValueError("imię żeńskie")
        print("żeńskie")
    else:
        print("męskie")
except Exception as e:
    print("Custom ValueError", e)


raise TypeError("To jest błąd który sam na koniec wywołuje bo mogę")
