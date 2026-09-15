x = 1

try:  # if
    wynik = 10/x
    print("Wynik dzielenia", wynik)
except ZeroDivisionError:  # elif   - można ich wiele - zwyczajowo chcemy użyć ale nie trzeba jeśli będzie finally
    print("ZeroDivisionError Nie można dzielić przez 0")
except TypeError:  # elif
    print("TypeError Nie można dzielić litery")
except Exception as e:
    print("Exception Moja custom wiadomość", e)
else:  # opcjonalne - nie musimy tego użyć
    # wykona się tylko jeśli try NIE zwróci błędu
    print("ELSE wykona się jeśli try jest poprawny")
finally:  # opcjonalne - nie musimy tego użyć pod warunkiem że użyliśmy except
    # wykona się zawsze - niezależnie czy błąd wystąpił, czy nie
    print("FINALLY wykona się zawsze na końcu")
