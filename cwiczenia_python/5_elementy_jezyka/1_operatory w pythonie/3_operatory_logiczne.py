
"""
not - negacja - odwraca stan
and - iloczyn loginczy - przynajmniej 1 False oznacza że całość jest False
or  - suma logiczna - przynajmniej 1 True oznacza że całość jest True

kolejność ma znacznie - zaczynamy rozpatrywanie od not, potem and potem or
"""


""" NOT """
# wynik = not True


""" OR """
# wynik = False or False or True or False
# wynik = 0 + 0 + 1 + 0
# wynik = False or False  # False
# wynik = False or True  # True
# wynik = True or False  # True
# wynik = True or True  # True
# wynik = True or False or False or False  # True


""" AND """
# wynik = False and False   # False
# wynik = False and True    # False
# wynik = True and False    # False
# wynik = True and True     # True


""" Warunki logiczne na bardziej praktycznym przykładzie """
imie = "Kasia"
wiek = 50
wynik = imie == "Kasia" and wiek >= 18  # True and True => True


""" Łączenie OR i AND """
# wynik = True and False or True  => True
# False or True  => True

# wynik = not True or False and True
# False or False and True
# False or False => False

# wynik = not (True or False) and True
# not True and True
# False and True => False


print(wynik)
