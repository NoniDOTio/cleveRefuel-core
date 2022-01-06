import pandas as pd
from model.tank_stop import TankStop
from forecast.base_forecast import BaseForecast
from model.gas_station_meta import GasStationMeta

class BrandwideForecasts(BaseForecast):

    def __init__(self) -> None:
        self.brand_price_cache = {}
        super().__init__()

    def get_forecast_for(self, fuel_stop: TankStop) -> int:
        price_data = self.get_price_data(fuel_stop)
        return round(
            price_data['price'].mean()
        )

    def get_brand_price_data(self, brand : str)->pd.DataFrame:
        try:
            return self.brand_price_cache[brand]
        except:
            print(f"Price Data not in cache, loading prices...")
            fuel_stations = self.data_reader.get_fuelstations_by_brand(brand)
            price_data = self.data_reader.get_all_fuelstations_data(fuel_stations['id'].tolist())

            # TODO make the time casting not suck
            #print("\nBuilding time values...")
            #price_data['hour'] = price_data['time'].apply(
            #    lambda time: datetime.datetime.strptime(time + "00", '%Y-%m-%d %H:%M:%S%z'
            #).hour)
            self.brand_price_cache[brand] = price_data
            print(f"Done!")
            return self.brand_price_cache[brand]


    def get_price_data(self, fuel_stop : TankStop) -> pd.DataFrame:
        price_data = self.get_brand_price_data(fuel_stop.meta.brand)
        return price_data
        # Only keeping price data within our time range
        if self.stop_is_at_night(fuel_stop):
            early_data = price_data.loc[price_data['hour'] <= 6]
            late_data = price_data.loc[price_data['hour'] > 18]
            price_data = pd.concat(early_data, late_data)
        else:
            price_data = price_data.loc[price_data['hour'] > 6]
            price_data = price_data.loc[price_data['hour'] <= 18]
        return price_data


    def stop_is_at_night(self, fuel_stop : TankStop) -> bool:
        return fuel_stop.timestamp.hour <= 6 or fuel_stop.timestamp.hour > 18


    def get_cache_key(self, fuel_stop : TankStop) -> str:
        day_night = "day"
        if self.stop_is_at_night(fuel_stop):
            day_night = "night"
        return f"{day_night}-{fuel_stop.meta.brand}"