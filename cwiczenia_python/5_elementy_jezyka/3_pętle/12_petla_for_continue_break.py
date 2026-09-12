lista_imion = ["Adam", "Basia", "Cezary", "Damian", "Ewa"]

""" Continue skipuje obieg pętli """
# for imie in lista_imion:
#     print("Start", imie)
#     if imie == "Basia":
#         print("Continue\n")
#         continue
#     print("Zwracam duże imie:", imie.upper())
#     print("koniec obiegu iteracji\n")


""" Break przerywa całą pętlę """

for imie in lista_imion:
    print("Start", imie)
    if imie == "Basia":
        print("Break\n")
        break
    print("Zwracam duże imie:", imie.upper())
    print("koniec obiegu iteracji\n")


