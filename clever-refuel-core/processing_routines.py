
from abc import abstractmethod
from route_data import RouteData
from forecast.naive import NaiveForecasts

from calculate_gas_usage.fixed_path_gas_station_problem_algorithm import *
from calculate_gas_usage.naive import *


class BaseProcessingType:
    @abstractmethod
    def run(route_data : RouteData) -> bool:
        return False

class AnalyzeWithNaiveForecast(BaseProcessingType):

    def run(route_data: RouteData) -> bool:
        # TODO Analyze stuff
        # Aktuell tanken wir bei allen Tankstellen 1. Liter, muss noch angepasst werden
        forecast = NaiveForecasts()

        calculate_naively(route_data, forecast)
        calculate_using_fixed_path_gas_station_problem_algorithm(route_data)
        return True