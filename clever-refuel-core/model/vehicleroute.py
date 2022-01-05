from .tank_stop import TankStop


class VehicleRoute:
    title: str
    tank_capacity: float
    stops: list[TankStop]

    def __init__(self, title, tank_capacity, stops):
        self.title = title
        self.tank_capacity = tank_capacity
        self.stops = stops
