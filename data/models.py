from dataclasses import dataclass, field
from typing import Tuple, List

# Base Class
class BaseEntity:
    def display(self):
        print(self.__dict__)

# Order
@dataclass
class Order(BaseEntity):
    id: str
    pickup_location: Tuple[float, float]
    dropoff_location: Tuple[float, float]
    weight: float
    volume: float
    earliest_pickup_time: str
    latest_delivery_time: str
    service_time: int
    priority: int

# Vehicle
@dataclass
class Vehicle(BaseEntity):
    id: str
    capacity_weight: float
    capacity_volume: float
    fixed_cost: float
    cost_per_km: float
    cost_per_min: float
    start_location: Tuple[float, float]
    end_location: Tuple[float, float]
    shift_start: str
    shift_end: str
    current_state: str

# Depot
@dataclass
class Depot(BaseEntity):
    id: str
    location: Tuple[float, float]
    opening_hours: str

# Route
@dataclass
class Route(BaseEntity):
    vehicle_id: str
    order_sequence: List[str] = field(default_factory=list)
    total_distance: float = 0.0
    total_time: float = 0.0
    total_cost: float = 0.0

# Network Graph
@dataclass
class NetworkGraph(BaseEntity):
    distance_matrix: List[List[float]]
    time_matrix: List[List[float]]

# Event
@dataclass
class Event(BaseEntity):
    event_type: str
    description: str