import math

from model.tank_stop import TankStop
from model.gas_station_meta import GasStationMeta


def distance_between(stop_a: TankStop, stop_b: TankStop) -> float:
    stop_a_meta: GasStationMeta = stop_a.meta
    stop_b_meta: GasStationMeta = stop_b.meta

    stop_a_lat: float = stop_a_meta.lat
    stop_a_long: float = stop_a_meta.long
    stop_b_lat: float = stop_b_meta.lat
    stop_b_long: float = stop_b_meta.long

    # Formular as seen in intellitank.pdf
    # TODO Check for errors
    distance = 6378.388 * math.acos(math.sin(stop_a_lat) * math.sin(stop_b_lat) + (math.cos(stop_a_lat) * math.cos(stop_b_lat) * math.cos(stop_b_long - stop_a_long)))
    return distance / 100
