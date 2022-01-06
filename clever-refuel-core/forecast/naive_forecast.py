from data_reader import DataReader
from model.tank_stop import TankStop

class NaiveForecasts:
    def __init__(self) -> None:
        self.data_reader = DataReader()


    def get_forecast_for(self, fuel_stop: TankStop) -> int:
        return round(
            self.data_reader.get_fuelstation_data(fuel_stop.id)['price'].mean()
        )