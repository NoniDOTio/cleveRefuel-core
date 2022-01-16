
from abc import abstractmethod
from data_reader import DataReader
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
    def run(self, route_data : RouteData) -> bool:
        return False

    def show_prediction_percision(self, plan : RefuelPlan):
        data_reader = DataReader()

        total_price_predicted = 0
        total_price_real = 0
        print()
        print()
        print("    ---- Prediction Percision ----")
        for stop in plan.stops:
            refuel_amount = stop.amount_to_refuel
            total_price_predicted += refuel_amount * stop.predicted_price_per_liter
            real_price = refuel_amount * data_reader.get_fuelstation_price_data_at_time(stop.id, stop.timestamp)
            total_price_real += real_price

            print(f"        Tankstop: {stop.meta.name}")
            print(f"        Predicted Price: {round(refuel_amount * stop.predicted_price_per_liter / 100, 2)}€")
            print(f"             Real Price: {round(real_price / 100, 2)}€")
            print()

        diff = abs(round(total_price_real / 100, 2) - round(total_price_predicted / 100, 2))
        print("    ---- Gesamt ---- ")
        print()
        print(f"    Predicted Price: {round(total_price_predicted / 100, 2)}€")
        print(f"         Real Price: {round(total_price_real / 100, 2)}€")
        print()
        print(f"    Difference: {round(diff, 2)}€")
        print()
        print()

"""
Analysiert die vom Nutzer gegebene Route mit einem Naiven Forecast auf naive
weise. hierbei wird der Durchschnittspreis der Tankstelle immer getankt wenn der
Tank nicht mehr bis zum naechsten Stop reicht
"""
class AnalyzeWithNaiveForecastOnNaiveRoute(BaseProcessingType):

    def run(self, route_data: RouteData) -> bool:
        forecast = NaiveForecasts()

        plan = calculate_naively(route_data, forecast)
        self.show_prediction_percision(plan)
        return True

"""
Analysiert die vom Nutzer gegebene Route mit einem Brandwide Forecast auf naive
weise. hierbei wird der Durchschnittspreis der Marke immer getankt wenn der
Tank nicht mehr bis zum naechsten Stop reicht
"""
class AnalyzeWithBrandwideForecastOnNaiveRoute(BaseProcessingType):

    def run(self, route_data: RouteData) -> bool:
        forecast = BrandwideForecasts()

        plan = calculate_naively(route_data, forecast)
        self.show_prediction_percision(plan)
        return True

"""
Analysiert die vom Nutzer gegebene Route mit einem Naiven Forecast mithilfe
des Fixed path gas station problem algorithm. Hierbei wird der Durchschnittspreis
der Tankstelle an den optimalen Tankstellen getankt.
"""
class AnalyzeWithFixedPathGasStationProblem(BaseProcessingType):

    def run(self, route_data: RouteData) -> bool:
        forecast = NaiveForecasts()

        plan = calculate_using_fixed_path_gas_station_problem_algorithm(route_data, forecast)
        self.show_prediction_percision(plan)
        return True

"""
Analysiert die vom Nutzer gegebene Route mit einem Naiven Forecast mithilfe
des Fixed path gas station problem algorithm. Hierbei wird der Durchschnittspreis
der Marke an den optimalen Tankstellen getankt.
"""
class AnalyzeBrandwideWithFixedPathGasStationProblem(BaseProcessingType):

    def run(self, route_data: RouteData) -> bool:
        forecast = BrandwideForecasts()

        plan = calculate_using_fixed_path_gas_station_problem_algorithm(route_data, forecast)
        self.show_prediction_percision(plan)
        return True


"""
"""
class AnalyzeWithNewFixedPathGasStationProblem(BaseProcessingType):

    def run(self, route_data: RouteData) -> bool:
        forecast = NaiveForecasts()

        plan = calculate_using_new_fixed_path_gas_station_problem_algorithm(route_data, forecast)
        self.show_prediction_percision(plan)
        return True


"""
"""
class AnalyzeBrandwideWithNewFixedPathGasStationProblem(BaseProcessingType):

    def run(self, route_data: RouteData) -> bool:
        forecast = BrandwideForecasts()

        plan = calculate_using_new_fixed_path_gas_station_problem_algorithm(route_data, forecast)
        self.show_prediction_percision(plan)
        return True