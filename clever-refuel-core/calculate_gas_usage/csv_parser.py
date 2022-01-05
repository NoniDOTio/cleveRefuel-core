import csv

from model.vehicleroute import VehicleRoute
from model.tank_stop import TankStop
from model.gas_station_meta import GasStationMeta


def read_route_file(route_file_path: str) -> VehicleRoute:
    if not route_file_path.endswith(".csv"):
        raise Exception

    title = route_file_path.replace(".csv", "")
    tank_capacity = None
    stops = []
    with open(route_file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")

        for i, line in enumerate(reader):
            if i == 0:
                tank_capacity = int(line[0])
                continue
            timestamp = line[0]
            id = int(line[1])
            tank_stop = TankStop(timestamp, id)
            tank_stop.meta = get_gas_station_meta(id)
            stops.append(tank_stop)
    route = VehicleRoute(title, tank_capacity, stops)
    route.title = title
    route.tank_capacity = tank_capacity
    route.stops = stops
    return route


def get_gas_station_meta(gas_station_id: int) -> GasStationMeta:
    gas_stations_file_path = "data/Tankstellen.csv"

    with open(gas_stations_file_path, "r", encoding = "utf-8") as file:
        reader = csv.reader(file, delimiter=";")

        for i, line in enumerate(reader):
            if int(line[0]) == int(gas_station_id):
                return GasStationMeta(
                    line[1],
                    line[2],
                    line[3],
                    line[4],
                    int(line[5]),
                    line[6],
                    float(line[7]),
                    float(line[8])
                )
