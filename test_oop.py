from homework_05 import base, car, engine, exceptions, plane

print("Тест Vehicle")
v = base.Vehicle(weight=1000, fuel=100, fuel_consumption=0.1)
v.start()
print(f"Started: {v.started}")
v.move(500)
print(f"Fuel left: {v.fuel}")

print("Тест Plane")
p = plane.Plane(weight=10000, fuel=1000, fuel_consumption=0.5, max_cargo=2000)
p.load_cargo(1500)
print(f"Cargo: {p.cargo}, Max: {p.max_cargo}")
print(f"Removed cargo: {p.remove_all_cargo()}")

print("Тест Car")
c = car.Car(weight=1500, fuel=50, fuel_consumption=0.2)
e = engine.Engine(volume=2.0, pistons=4)
c.set_engine(e)
print(f"Engine: {c.engine.volume}L, Pistons: {c.engine.pistons}")

print("ВСЁ РАБОТАЕТ!")
