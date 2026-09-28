import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.manage_employees_page import ManageEmployeesPage

# Powiązanie scenariuszy z pliku .feature
scenarios('../features/dodaj_pracownika.feature')


@pytest.fixture
def manage_employees_page(driver, wait):
    return ManageEmployeesPage(driver, wait)


@given('użytkownik jest zalogowany w systemie')
def zaloguj_uzytkownika(logowanie_ui):
    """Logowanie następuje automatycznie przez fixturę logowanie_ui."""
    pass


@when(parsers.parse('użytkownik wprowadza imię "{name}", pensję {salary:d}, wiek {age:d}, stanowisko "{position}" i urlop {on_leave}'))
def wprowadz_dane_pracownika(manage_employees_page, name, salary, age, position, on_leave):
    on_leave_bool = str(on_leave).lower() in ('true', 'yes', '1', 'tak')
    manage_employees_page.fill_name(name)
    manage_employees_page.fill_salary(salary)
    manage_employees_page.fill_age(age)
    manage_employees_page.fill_position(position)
    manage_employees_page.fill_on_leave(on_leave_bool)


@when('użytkownik zatwierdza formularz')
def wyslij_formularz(manage_employees_page):
    manage_employees_page.submit_form()


@then(parsers.parse('nowy pracownik z imieniem "{name}", pensją {salary:d}, wiekiem {age:d}, stanowiskiem "{position}" i urlopem {on_leave} pojawia się na końcu tabeli'))
def weryfikuj_pracownika_w_tabeli(manage_employees_page, name, salary, age, position, on_leave):
    on_leave_bool = str(on_leave).lower() in ('true', 'yes', '1', 'tak')
    dane_ostatniego_wiersza = manage_employees_page.get_last_employee_data()
    
    assert int(dane_ostatniego_wiersza[0]) > 0
    assert dane_ostatniego_wiersza[1] == name
    assert dane_ostatniego_wiersza[2] == str(salary)
    assert dane_ostatniego_wiersza[3] == str(age)
    assert dane_ostatniego_wiersza[4] == position
    assert dane_ostatniego_wiersza[5] == ("✅" if on_leave_bool else "❌")
