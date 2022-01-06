from abc import abstractclassmethod
from data_reader import DataReader
from model.tank_stop import TankStop

class BaseForecast:
    def __init__(self) -> None:
        self.data_reader = DataReader()

    @abstractclassmethod
    def get_forecast_for(self, fuel_stop: TankStop) -> int:
        pass