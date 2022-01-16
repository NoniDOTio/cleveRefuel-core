
from abc import abstractmethod
from model.route_data import RouteData
from forecast.naive_forecast import NaiveForecasts
from forecast.brandwide_forecast import BrandwideForecasts

from calculate_gas_usage.fixed_path_gas_station_problem_algorithm import *
from calculate_gas_usage.new_fixed_path_gas_station_problem_algorithm import *
from calculate_gas_usage.naive import *

"""
Grundlage fuer alle Processing Typen. Jeder Processing type stellt einen
Menupunkt dar der ausgefuehrt werden kann.
"""
class BaseProcessingType:
    @abstractmethod
    def run(route_data : RouteData) -> bool:
        return False

"""
Analysiert die vom Nutzer gegebene Route mit einem Naiven Forecast auf naive
weise. hierbei wird der Durchschnittspreis der Tankstelle immer getankt wenn der
Tank nicht mehr bis zum naechsten Stop reicht
"""
class AnalyzeWithNaiveForecastOnNaiveRoute(BaseProcessingType):

    def run(route_data: RouteData) -> bool:
        forecast = NaiveForecasts()

        calculate_naively(route_data, forecast)
        return True

"""
Analysiert die vom Nutzer gegebene Route mit einem Brandwide Forecast auf naive
weise. hierbei wird der Durchschnittspreis der Marke immer getankt wenn der
Tank nicht mehr bis zum naechsten Stop reicht
"""
class AnalyzeWithBrandwideForecastOnNaiveRoute(BaseProcessingType):

    def run(route_data: RouteData) -> bool:
        forecast = BrandwideForecasts()

        calculate_naively(route_data, forecast)
        return True

"""
Analysiert die vom Nutzer gegebene Route mit einem Naiven Forecast mithilfe
des Fixed path gas station problem algorithm. Hierbei wird der Durchschnittspreis
der Tankstelle an den optimalen Tankstellen getankt.
"""
class AnalyzeWithFixedPathGasStationProblem(BaseProcessingType):

    def run(route_data: RouteData) -> bool:
        forecast = NaiveForecasts()

        calculate_using_fixed_path_gas_station_problem_algorithm(route_data, forecast)
        return True

"""
Analysiert die vom Nutzer gegebene Route mit einem Naiven Forecast mithilfe
des Fixed path gas station problem algorithm. Hierbei wird der Durchschnittspreis
der Marke an den optimalen Tankstellen getankt.
"""
class AnalyzeBrandwideWithFixedPathGasStationProblem(BaseProcessingType):

    def run(route_data: RouteData) -> bool:
        forecast = BrandwideForecasts()

        temp = calculate_using_fixed_path_gas_station_problem_algorithm(route_data, forecast)
        for i in temp:
            print(temp.amount_to_refuel)
        return True


"""
"""
class AnalyzeWithNewFixedPathGasStationProblem(BaseProcessingType):

    def run(route_data: RouteData) -> bool:
        forecast = NaiveForecasts()

        calculate_using_new_fixed_path_gas_station_problem_algorithm(route_data, forecast)
        return True


"""
"""
class AnalyzeBrandwideWithNewFixedPathGasStationProblem(BaseProcessingType):

    def run(route_data: RouteData) -> bool:
        forecast = BrandwideForecasts()

        calculate_using_new_fixed_path_gas_station_problem_algorithm(route_data, forecast)
        return True