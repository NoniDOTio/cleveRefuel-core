from model.route_data import RouteData
from calculate_gas_usage.distance_utils import distance_between
from calculate_gas_usage.constants import GAS_PER_KILOMETER
from forecast.base_forecast import BaseForecast


def calculate_naively(route: RouteData, forecast: BaseForecast) -> None:
    max_possible_distance = route.fuel_tank_size / GAS_PER_KILOMETER
    money_spent_on_refueling = 0
    total_refueled = 0
    current_fuel = 0

    # Loop through all stops in route
    for i in range(0, len(route.stops) - 1):
        current_stop = route.stops[i]
        next_stop = route.stops[i+1]

        if i == len(route.stops) + 1:
            km_to_next_stop = 0
        else:
            km_to_next_stop = distance_between(route.stops[i], route.stops[i+1])

        fuel_to_next_stop = km_to_next_stop * GAS_PER_KILOMETER

        print(current_stop.meta.name, "-->", next_stop.meta.name, f"({km_to_next_stop}km)")
        print("Fuel required to next stop:", fuel_to_next_stop, "liters")
        print("Current fuel: " + str(current_fuel) + "/" + str(route.fuel_tank_size) + "")

        if current_fuel < fuel_to_next_stop:
            # Refuel to max tank capacity
            price_prediction = forecast.get_forecast_for(current_stop)
            amount_to_refuel = route.fuel_tank_size - current_fuel
            refuel_cost = amount_to_refuel * price_prediction
            money_spent_on_refueling += refuel_cost
            total_refueled += amount_to_refuel
            current_fuel = route.fuel_tank_size

            print("Refueling", amount_to_refuel, "litres for", refuel_cost, "cents")

        current_fuel -= fuel_to_next_stop
        print("")

    print("Total refueled:", total_refueled, "Total money spend on refueling:", round(money_spent_on_refueling / 100, 2), "€")
