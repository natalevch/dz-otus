"""
Создайте класс `Plane`, наследник `Vehicle`
"""
from homework_05.base import Vehicle
from homework_05 import exceptions


class Plane(Vehicle):
    cargo: float = 0

    def __init__(self, weight: float = 0, fuel: float = 0,
                 fuel_consumption: float = 0, max_cargo: float = 0):
        super().__init__(weight=weight, fuel=fuel, fuel_consumption=fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, amount: float) -> None:
        if self.cargo + amount <= self.max_cargo:
            self.cargo += amount
        else:
            raise exceptions.CargoOverload()

    def remove_all_cargo(self) -> float:
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo
