import os
import pandas as pd
from route_data import RouteData


class DataReader:
    def __init__(self) -> None:
        self.fuel_station_folder = "data/Benzinpreise"
        self.route_folder = "data/Fahrzeugrouten"


    def get_all_routes(self) -> list:
        return os.listdir(self.route_folder)


    def get_route_data(self, route) -> RouteData:
        return RouteData(self.route_folder + os.path.sep + route)


    def get_fuelstation_data(self, fuelstation_id) -> pd.DataFrame:
        data_path = self.fuel_station_folder + os.path.sep + str(fuelstation_id)
        data = pd.read_csv(data_path + ".csv", delimiter=";", names=["time", "price"])
        # Striping the last digit
        data['price'] = data['price'].apply(
            lambda price: int(price/10)
        )
        return data


