from abc import abstractmethod
from data_reader import DataReader
from model.tank_stop import TankStop
import pandas as pd

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

    """
    Tested ob der gegebene Tankstop nachts liegt oder nicht. Nachts ist zwischen
    18 uhr abends und 6 uhr morgens
    """
    def stop_is_at_night(self, fuel_stop : TankStop) -> bool:
        return fuel_stop.timestamp.hour <= 6 or fuel_stop.timestamp.hour > 18

    """
    Gibt alle Preispunkte zurueck welche an speziel an dem gegebenen Tankstop
    wichtig sind.
    """
    def get_time_relevant_price_data(self, price_data : pd.DataFrame, fuel_stop : TankStop) -> pd.DataFrame:
        # Only keeping price data within our time range
        if self.stop_is_at_night(fuel_stop):
            early_data = price_data.loc[price_data['hour'] <= 6]
            late_data = price_data.loc[price_data['hour'] > 18]
            price_data = pd.concat(early_data, late_data)
        else:
            price_data = price_data.loc[price_data['hour'] > 6]
            price_data = price_data.loc[price_data['hour'] <= 18]
        return price_data