"""
Repräsentiert weitere Informationen zu einer Tankstelle
"""
class GasStationMeta:
    name: str
    brand: str
    street: str
    street_number: int
    plz: int
    city: str
    lat: float
    long: float

    def __init__(self, name, brand, street, street_number, plz, city, lat, long):
        self.name = name
        self.brand = brand
        self.street = street
        self.street_number = street_number
        self.plz = plz
        self.city = city
        self.lat = lat
        self.long = long
