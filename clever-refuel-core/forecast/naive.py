from data_reader import DataReader

class NaiveForecasts:
    def __init__(self) -> None:
        self.data_reader = DataReader()


    def get_forecast_for(self, fuelstation_id) -> int:
        return round(
            self.data_reader.get_fuelstation_data(fuelstation_id)['price'].mean()
        )