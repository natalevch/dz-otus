"""
Доработайте класс `Vehicle`
"""

from homework_05 import exceptions


class Vehicle:
    weight: float = 0
    started: bool = False
    fuel: float = 0
    fuel_consumption: float = 0

    def __init__(self, weight: float = 0, fuel: float = 0, fuel_consumption: float = 0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self) -> None:
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError()

    def move(self, distance: float) -> None:
        needed_fuel = distance * self.fuel_consumption
        if needed_fuel <= self.fuel:
            self.fuel -= needed_fuel
        else:
            raise exceptions.NotEnoughFuel()

