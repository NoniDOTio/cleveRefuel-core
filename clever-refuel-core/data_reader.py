import os
import pandas as pd
from model.gas_station_meta import GasStationMeta
from model.route_data import RouteData
from model.tank_stop import TankStop
from model.gas_station_meta import GasStationMeta


class DataReader:
    gas_stations_meta_data : pd.DataFrame


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


    def get_all_routes(self) -> list:
        return os.listdir(self.route_folder)


    def get_route_data(self, route) -> RouteData:
        route_data = RouteData(self.route_folder + os.path.sep + route)
        for index, row in route_data.data.iterrows():
            stop = TankStop(row['time'], row['fuel-station'])
            stop.meta = self.get_gas_station_meta(stop.id)
            route_data.stops.append(stop)
        return route_data


    def get_fuelstation_price_data(self, fuelstation_id) -> pd.DataFrame:
        data_path = self.fuel_station_folder + os.path.sep + str(fuelstation_id)
        data = pd.read_csv(data_path + ".csv", delimiter=";", names=["time", "price"])
        # Striping the last digit
        data['price'] = data['price'].apply(
            lambda price: int(price/10)
        )
        return data

    def get_fuelstation_price_data_generator(self, fuelstations) -> pd.DataFrame:
        done = 0
        total = len(fuelstations)
        for fuelstation in fuelstations:
            print(f"Loading Price Data... {done}/{total}\r", end="")
            done += 1
            try:
                dataframe = self.get_fuelstation_price_data(fuelstation)
                yield dataframe.assign(fuelstation_id=fuelstation)
            except:
                yield pd.DataFrame(
                    columns=['time', 'price', 'fuelstation_id']
                )


    def get_all_fuelstations_data(self, fuelstations : list) -> pd.DataFrame:
        return pd.concat(self.get_fuelstation_price_data_generator(fuelstations))


    def get_fuelstations_by_brand(self, brand : str) -> pd.DataFrame:
        data = self.gas_stations_meta_data
        return data.loc[data['brand'] == brand]


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
