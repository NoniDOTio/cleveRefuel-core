from model.tank_stop import TankStop
from forecast.base_forecast import BaseForecast

"""
Gibt grob abgeschaetzt zurueck wie hoch die Preise am gegebenen Tankstop sind.
Zur abschaetzung wird der Durchschnitt aller bekannten Preispunkte genommen.
"""
class NaiveForecasts(BaseForecast):

    def __init__(self) -> None:
        self.day_night_prices = False
        super().__init__()

    def use_day_night_prices(self, value = True):
        self.day_night_prices = value

    def get_forecast_for(self, fuel_stop: TankStop) -> int:
        price_data = self.data_reader.get_fuelstation_price_data(fuel_stop.id)
        if (self.day_night_prices):
            price_data = self.get_time_relevant_price_data(price_data, fuel_stop)
        return round(
            price_data['price'].mean()
        )