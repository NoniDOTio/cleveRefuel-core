import datetime
import pandas as pd
from model.tank_stop import TankStop
from forecast.base_forecast import BaseForecast

"""
Ermoeglicht das Abschaetzen zukuenftiger Preise.
"""
class BrandwideForecasts(BaseForecast):

    def __init__(self) -> None:
        self.brand_price_cache = {}
        super().__init__()

    """
    Sucht nach dem vermuteten Preis am angegebenen Tankstop.
    """
    def get_forecast_for(self, fuel_stop: TankStop) -> int:
        price_data = self.get_price_data(fuel_stop)
        return round(
            price_data['price'].mean()
        )

    """
    Gibt alle Preispunkte zurueck die fuer die gegebene Marke ermittelt werden
    koennen.
    """
    def get_brand_price_data(self, brand : str)->pd.DataFrame:
        try:
            return self.brand_price_cache[brand]
        except:
            print(f"Price Data not in cache, loading prices...")
            fuel_stations = self.data_reader.get_fuelstations_by_brand(brand)
            price_data = self.data_reader.get_all_fuelstations_data(fuel_stations['id'].tolist())
            # TODO make the time casting ... faster
            print("\nBuilding time values...")
            price_data['hour'] = price_data['time'].apply(
                lambda time: datetime.datetime.strptime(time + "00", '%Y-%m-%d %H:%M:%S%z'
            ).hour)
            self.brand_price_cache[brand] = price_data
            print(f"\nDone!")
            return self.brand_price_cache[brand]

    """
    Gibt alle Preispunkte zurueck welche an speziel an dem gegebenen Tankstop
    wichtig sind.
    """
    def get_price_data(self, fuel_stop : TankStop) -> pd.DataFrame:
        price_data = self.get_brand_price_data(fuel_stop.meta.brand)
        # Only keeping price data within our time range
        if self.stop_is_at_night(fuel_stop):
            early_data = price_data.loc[price_data['hour'] <= 6]
            late_data = price_data.loc[price_data['hour'] > 18]
            price_data = pd.concat(early_data, late_data)
        else:
            price_data = price_data.loc[price_data['hour'] > 6]
            price_data = price_data.loc[price_data['hour'] <= 18]
        return price_data

    """
    Tested ob der gegebene Tankstop nachts liegt oder nicht. Nachts ist zwischen
    18 uhr abends und 6 uhr morgens
    """
    def stop_is_at_night(self, fuel_stop : TankStop) -> bool:
        return fuel_stop.timestamp.hour <= 6 or fuel_stop.timestamp.hour > 18