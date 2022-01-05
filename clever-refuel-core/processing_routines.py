
from abc import abstractmethod
from route_data import RouteData
from forecast.naive import NaiveForecasts

from calculate_gas_usage.fixed_path_gas_station_problem_algorithm import *
from calculate_gas_usage.naive import *
from calculate_gas_usage.csv_parser import read_route_file


class BaseProcessingType:
    @abstractmethod
    def run(route_data : RouteData) -> bool:
        return False

class AnalyzeWithNaiveForecast(BaseProcessingType):

    def run(route_data: RouteData) -> bool:
        # TODO Analyze stuff
        # Aktuell tanken wir bei allen Tankstellen 1. Liter, muss noch angepasst werden
        forecast = NaiveForecasts()

        route = read_route_file(route_data.path)
        calculate_naively(route, forecast)
        calculate_using_fixed_path_gas_station_problem_algorithm(route)

        return True

        total = 0
        for index, row in route_data.data.iterrows():
            time = row["time"]
            fuel_station = row["fuel-station"]

            forecasted_price = forecast.get_forecast_for(fuel_station)
            total += forecasted_price
            print(f"Preisvorhersage bei Tankstelle {fuel_station} liegt bei {forecasted_price}ct")

        print("Vorgesagter Gesamtpreis liegt bei:", total / 100, "€")
        return True