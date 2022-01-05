import os
import pandas as pd
from model.gas_station_meta import GasStationMeta
from route_data import RouteData
from model.tank_stop import TankStop


class DataReader:
    gas_stations_meta_data : pd.DataFrame


    def __init__(self) -> None:
        self.fuel_station_folder = "data/Benzinpreise"
        self.route_folder = "data/Fahrzeugrouten"
        self.gas_stations_meta_file_path = "data/Tankstellen.csv"
        self.gas_stations_meta_data = pd.DataFrame()


    def get_all_routes(self) -> list:
        return os.listdir(self.route_folder)


    def get_route_data(self, route) -> RouteData:
        route_data = RouteData(self.route_folder + os.path.sep + route)
        for index, row in route_data.data.iterrows():
            stop = TankStop(row['time'], row['fuel-station'])
            stop.meta = self.get_gas_station_meta(stop.id)
            route_data.stops.append(stop)
        return route_data


    def get_fuelstation_data(self, fuelstation_id) -> pd.DataFrame:
        data_path = self.fuel_station_folder + os.path.sep + str(fuelstation_id)
        data = pd.read_csv(data_path + ".csv", delimiter=";", names=["time", "price"])
        # Striping the last digit
        data['price'] = data['price'].apply(
            lambda price: int(price/10)
        )
        return data


    def get_gas_station_meta(self, gas_station_id: int) -> GasStationMeta:
        if self.gas_stations_meta_data.empty:
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
