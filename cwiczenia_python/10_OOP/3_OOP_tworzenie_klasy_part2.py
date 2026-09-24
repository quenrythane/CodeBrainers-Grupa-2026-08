

"""  zestaw lego """

class LegoSet:
    def __init__(self, name, pieces_count, price, universe_name):
        self.name = name
        self.pieces_count = pieces_count
        self.price = price
        self.universe_name = universe_name

    def advertise(self):
        print(f"""Produkt: {self.name}!
        Ilość elementów: {self.pieces_count}
        Cena: {self.price} PLN
        Uniwersum: {self.universe_name}
        Super cena \n
        """)

    def get_build(self):
        print(f"Zestaw {self.name} został zbudowany")


lego_barbie_5150 = LegoSet("Barbie Dreamhouse", 5150, 299.99, "Barbie")
lego_cars_8180 = LegoSet("Ferrari Daytona SP3", 3779, 1699.99, "Lego Cars")


print("ilość elementów barbie", lego_barbie_5150.pieces_count)
print("cena barbie", lego_barbie_5150.price)
lego_barbie_5150.advertise()







