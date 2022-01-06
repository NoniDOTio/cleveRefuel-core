from abc import abstractmethod
from data_reader import DataReader
from model.tank_stop import TankStop

"""
Ist die Grundlage aller Forecasting Klassen. Forecasting Klassen ermoeglichen
das abschaetzen von Spritpreisen.
"""
class BaseForecast:
    def __init__(self) -> None:
        self.data_reader = DataReader()

    """
    Versucht den Preis fuer den gegebenen Tankstop abzuschaetzen. Der Preis wird
    in ct zurueckgegeben.
    """
    @abstractmethod
    def get_forecast_for(self, fuel_stop: TankStop) -> int:
        pass