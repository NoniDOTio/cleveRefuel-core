from model.route_data import RouteData
from model.tank_stop import TankStop
from model.refuel_plan import RefuelPlan
from calculate_gas_usage.distance_utils import distance_between
from calculate_gas_usage.constants import GAS_PER_KILOMETER
from forecast.base_forecast import BaseForecast

"""
Durchläuft eine Fahrzeugroute und schlägt eine bessere Tankstrategie vor
"""
def calculate_using_fixed_path_gas_station_problem_algorithm(route: RouteData, forecast: BaseForecast) -> RefuelPlan:
    max_possible_distance = route.fuel_tank_size / GAS_PER_KILOMETER
    prices = []
    distances = []
    optimal_stops = {}
    approached_stops = []

    money_spent_on_refueling = 0
    total_refueled = 0
    current_fuel = 0

    # Get necessary data
    for i in range(0, len(route.stops) - 1):
        # Store price prediction
        forecasted_price = forecast.get_forecast_for(route.stops[i])
        prices.append(forecasted_price)

        # Store distance to following stop, except for last stop
        if i == len(route.stops) - 1:
            break
        distance_to_next = distance_between(route.stops[i], route.stops[i + 1])
        distances.append(distance_to_next)

    # Loop through all gas stations starting from destination
    i = len(route.stops) - 2
    while i > 0:

        # Break out of loop if destination is reachable
        if sum(distances[0:i]) < max_possible_distance:
            optimal_stops[0] = [
                sum(distances[0:i]) * GAS_PER_KILOMETER,
                prices[0] * (sum(distances[0:i]) * GAS_PER_KILOMETER)
            ]
            break

        # Loop through stations that are within max_possible_distance
        distance = 0
        cheapest_gas_station_index = None
        cheapest_gas_station_distance = None
        for j in range(i - 1, 0, -1):
            distance += distances[j]

            # Initialize cheapest gas station with closes gas station
            if j == i - 1:
                cheapest_gas_station_index = j
                cheapest_gas_station_distance = distance

            # Quit loop if max_possible_distance is exceeded
            if distance > max_possible_distance:
                break

            # Replace cheapest gas station with j if it's cheaper
            if prices[j] < prices[cheapest_gas_station_index]:
                cheapest_gas_station_index = j
                cheapest_gas_station_distance = distance

        optimal_stops[cheapest_gas_station_index] = [
            cheapest_gas_station_distance * GAS_PER_KILOMETER,
            prices[cheapest_gas_station_index] * (cheapest_gas_station_distance * GAS_PER_KILOMETER)
        ]
        i = cheapest_gas_station_index

    money_spent_on_refueling = 0
    total_refueled = 0
    for gas_station_id, data in reversed(optimal_stops.items()):
        current_stop = route.stops[gas_station_id]
        amount_to_refuel = data[0]
        refuel_cost = data[1]
        money_spent_on_refueling += refuel_cost
        total_refueled += amount_to_refuel

        # Write to
        current_stop.amount_to_refuel = amount_to_refuel
        current_stop.predicted_price_per_liter = refuel_cost / amount_to_refuel
        approached_stops.append(current_stop)
        print(current_stop.meta.name, "-->")
        print("Refueling", round(amount_to_refuel, 2), "litres for", round(refuel_cost / 100, 2), "€")
        print("")

    print("Total refueled:", round(total_refueled, 2), "liters - Total money spend on refueling:",
          round(money_spent_on_refueling / 100, 2), "€")

    return RefuelPlan(approached_stops)
