import os
import pandas as pd
from model.gas_station_meta import GasStationMeta
from model.route_data import RouteData
from model.tank_stop import TankStop
from model.gas_station_meta import GasStationMeta

"""
Kuemmert sich um das Einlesen der Dateien.
"""
class DataReader:
    """
    Initialisiert einen neuen DataReader und liest die Metadaten der Tankstellen
    ein.
    """
    def __init__(self) -> None:
        base_path = "data"

        if os.path.exists("informaticup-data/Eingabedaten"):
            base_path = "informaticup-data/Eingabedaten"

        self.fuel_station_folder = f"{base_path}/Benzinpreise"
        self.route_folder = "data/Fahrzeugrouten"
        self.gas_stations_meta_file_path = f"{base_path}/Tankstellen.csv"
        self.gas_stations_meta_data = pd.read_csv(
            self.gas_stations_meta_file_path,
            delimiter=";",
            encoding="utf-8",
            names=[
                "id",
                "name",
                "brand",
                "street",
                "street-number",
                "plz",
                "city",
                "lat",
                "long"
            ]
        )

    """
    Gibt alle Routen zurueck die fuer die Anwendung hinterlegt sind
    """
    def get_all_routes(self) -> list:
        return os.listdir(self.route_folder)

    """
    Liest die Daten fuer die gegebene Route ein und gibt diese als zurueck
    """
    def get_route_data(self, route) -> RouteData:
        route_data = RouteData(self.route_folder + os.path.sep + route)
        for index, row in route_data.data.iterrows():
            stop = TankStop(row['time'], row['fuel-station'])
            stop.meta = self.get_gas_station_meta(stop.id)
            route_data.stops.append(stop)
        return route_data

    """
    Liest die Preise fuer die gegebene Tankstelle ein und gibt diese unbehandelt
    zurueck.
    """
    def get_fuelstation_price_data(self, fuelstation_id) -> pd.DataFrame:
        data_path = self.fuel_station_folder + os.path.sep + str(fuelstation_id)
        data = pd.read_csv(data_path + ".csv", delimiter=";", names=["time", "price"])
        # Striping the last digit
        data['price'] = data['price'].apply(
            lambda price: int(price/10)
        )
        return data

    """
    Gibt einen Generator zurueck welcher die Daten aller gegebenen tankstellen
    enthaelt.
    """
    def get_fuelstation_price_data_generator(self, fuelstations : list) -> pd.DataFrame:
        done = 0
        total = len(fuelstations)
        for fuelstation in fuelstations:
            done += 1
            print(f"Loading Price Data... {done}/{total}\r", end="")
            try:
                dataframe = self.get_fuelstation_price_data(fuelstation)
                yield dataframe.assign(fuelstation_id=fuelstation)
            except:
                yield pd.DataFrame(
                    columns=['time', 'price', 'fuelstation_id']
                )

    """
    Gibt ein Dataframe zurueck welches die Daten aller gegebenen Tankstellen
    enthaelt.
    """
    def get_all_fuelstations_data(self, fuelstations : list) -> pd.DataFrame:
        if (len(fuelstations) == 0):
            return pd.DataFrame(columns=['time', 'price', 'fuelstation_id'])
        # Generieren des Dataframes für die Optimale Performance
        return pd.concat(self.get_fuelstation_price_data_generator(fuelstations))

    """
    Gibt alle Tankstellen zurueck welche von der gegebenen Marke sind.
    """
    def get_fuelstations_by_brand(self, brand : str) -> pd.DataFrame:
        data = self.gas_stations_meta_data
        return data.loc[data['brand'] == brand]

    """
    Parsed die Metadaten fuer die gegebene Tankstelle und gibt diese zurueck.
    """
    def get_gas_station_meta(self, gas_station_id: int) -> GasStationMeta:
        data = self.gas_stations_meta_data
        gas_station = data.loc[data['id'] == gas_station_id].iloc[0]
        return GasStationMeta(
            gas_station['name'],
            gas_station['brand'],
            gas_station['street'],
            gas_station['street-number'],
            gas_station['plz'],
            gas_station['city'],
            gas_station['lat'],
            gas_station['long'],
        )
