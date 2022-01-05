
from abc import abstractmethod
from route_data import RouteData
from forecast.naive import NaiveForecasts

class BaseProcessingType:
    @abstractmethod
    def run(route_data : RouteData) -> bool:
        return False

class AnalyzeWithNaiveForecast(BaseProcessingType):

    def run(route_data: RouteData) -> bool:
        # TODO Analyze stuff
        # Aktuell tanken wir bei allen Tankstellen 1. Liter, muss noch angepasst werden
        forecast = NaiveForecasts()

        total = 0
        for index, row in route_data.data.iterrows():
            time = row["time"]
            fuel_station = row["fuel-station"]

            forecasted_price = forecast.get_forecast_for(fuel_station)
            total += forecasted_price
            print(f"Preisvorhersage bei Tankstelle {fuel_station} liegt bei {forecasted_price}ct")

        print("Vorgesagter Gesamtpreis liegt bei:", total / 100, "€")
        return True