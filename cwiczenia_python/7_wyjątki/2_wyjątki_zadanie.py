
"""
stwórz funkcje dzielenia - niech przyjmei 2 liczby.
Zabezpiecz ją przed dzieleniem przez 0.

Wykonaj funkcje dla liczb:
dzielnie(10/2)
dzielnie(7/2)
dzielnie(10/0)
"""
# def dzielenie(num1, num2):
#     print(num1 / num2)

def dzielenie(num1, num2):
    try:
        print(num1 / num2)
    except:
        print('Nie możemy dzielić przez 0.')


# dzielenie(10, 2)
# dzielenie(7, 2)
# dzielenie(10, 0)

dzielenie("Artur", "Makota")


def dzielenie():
    while True:
        try:
            num1 = int(input("Podaj liczbe którą chcesz podzielić: "))
            break
        except:
            print("To nie jest liczba,spróbuj jeszcze raz")
    while True:
        try:
            num2 = int(input("Podaj liczbe przez którą chcesz podzielić: "))
            if num2 == 0:
                print("Nie możemy dzielić przez 0")
                continue
            break
        except:
            print("To nie jest liczba,spróbuj jeszcze raz")

    print(num1 / num2)


dzielenie()
