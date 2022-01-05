from datetime import datetime

from .gas_station_meta import GasStationMeta


class TankStop:
    # Meta
    id: int
    meta: GasStationMeta

    # Fields required to calculate optimal refueling strategy
    timestamp: datetime
    predicted_price_per_liter: float
    current_fuel_amount: float
    amount_to_refuel: float

    # Fields that are required additionally to use the fixed path gas station problem algorithm
    previous_station: None
    current_station: None
    next_station: None

    def __init__(self, timestamp, id) -> None:
        self.timestamp = timestamp
        self.id = id

    def set_meta(self, meta: GasStationMeta) -> None:
        self.meta = meta
