from model.route_data import RouteData
from model.tank_stop import TankStop
from model.refuel_plan import RefuelPlan
from forecast.base_forecast import BaseForecast
from calculate_gas_usage.constants import GAS_PER_KILOMETER

"""
Durchläuft eine Fahrzeugroute und schlägt eine optimale Tankstrategie vor
"""
def calculate_using_new_fixed_path_gas_station_problem_algorithm(route: RouteData, forecast: BaseForecast) -> RefuelPlan:
    print("I am running")



