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
        price_data = self.get_brand_price_data(fuel_stop.meta.brand)
        price_data = self.get_time_relevant_price_data(price_data, fuel_stop)
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

            self.brand_price_cache[brand] = price_data
            return self.brand_price_cache[brand]