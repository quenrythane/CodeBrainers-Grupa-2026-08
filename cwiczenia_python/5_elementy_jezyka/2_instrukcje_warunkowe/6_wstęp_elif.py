
punkty = 60


if punkty >= 90:
    ocena = '5'

elif punkty >= 75:
    ocena = '4'

elif punkty >= 60:
    ocena = '3'

else:
    ocena = '2'


print("ocena:", ocena)

""" trójargumentowy operator warunkowy """
# damską łazienka
imie = "Adam"

# przypisanie zmiennej na podstawie warunku
if imie.endswith('a'):
    jaka_lazienke_wybrac = "damską"
else:
    jaka_lazienke_wybrac = "męską"

# przypisanie zmiennej na podstawie warunku w jednej linijce (trójargumentowy operator warunkowy)
jaka_lazienke_wybrac = "damską" if imie.endswith('a') else "męską"

print("Łazienka", jaka_lazienke_wybrac)