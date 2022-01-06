from model.tank_stop import TankStop
from forecast.base_forecast import BaseForecast

class NaiveForecasts(BaseForecast):
    def get_forecast_for(self, fuel_stop: TankStop) -> int:
        return round(
            self.data_reader.get_fuelstation_price_data(fuel_stop.id)['price'].mean()
        )