from .tank_stop import TankStop

"""
Beinhaltet Tankstellen, welche planmäßig angefahren werden sollen
"""
class RefuelPlan:
    stops: [TankStop]

    def __init__(self, stops: [TankStop]) -> None:
        self.stops = stops
