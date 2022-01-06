
from abc import abstractmethod
from model.route_data import RouteData
from forecast.naive_forecast import NaiveForecasts
from forecast.brandwide_forecast import BrandwideForecasts

from calculate_gas_usage.fixed_path_gas_station_problem_algorithm import *
from calculate_gas_usage.naive import *


class BaseProcessingType:
    @abstractmethod
    def run(route_data : RouteData) -> bool:
        return False

class AnalyzeWithNaiveForecast(BaseProcessingType):

    def run(route_data: RouteData) -> bool:
        forecast = NaiveForecasts()

        calculate_naively(route_data, forecast)
        return True

class AnalyzeWithFixedPathGasStationProblem(BaseProcessingType):

    def run(route_data: RouteData) -> bool:
        forecast = NaiveForecasts()

        calculate_using_fixed_path_gas_station_problem_algorithm(route_data, forecast)
        return True

class AnalyzeBrandwideWithFixedPathGasStationProblem(BaseProcessingType):

    def run(route_data: RouteData) -> bool:
        forecast = BrandwideForecasts()

        calculate_naively(route_data, forecast)
        #calculate_using_fixed_path_gas_station_problem_algorithm(route_data, forecast)
        return True