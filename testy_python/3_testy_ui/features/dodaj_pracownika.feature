@test_bdd
@dodaj_pracownika
Feature: Dodawanie nowego pracownika
  Jako zalogowany kierownik
  Chcę dodać nowego pracownika do systemu
  Aby jego dane znajdowały się w tabeli pracowników

  @test_bdd
  Scenario Outline: Pomyślne dodanie nowego pracownika
    Given użytkownik jest zalogowany w systemie
    When użytkownik wprowadza imię "<name>", pensję <salary>, wiek <age>, stanowisko "<position>" i urlop <on_leave>
    And użytkownik zatwierdza formularz
    Then nowy pracownik z imieniem "<name>", pensją <salary>, wiekiem <age>, stanowiskiem "<position>" i urlopem <on_leave> pojawia się na końcu tabeli

    Examples:
      | name  | salary | age | position  | on_leave |
      | Basia | 10000  | 30  | Junior QA | True     |
