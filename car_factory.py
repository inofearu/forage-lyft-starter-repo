from car import Car
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tire.octoprime_tire import OctoprimeTire
from tire.carrigan_tire import CarriganTire

class CarFactory:
    def create_calliope(last_service_date, current_mileage, last_service_mileage, today, wear_level):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, today)
        tire = OctoprimeTire(wear_level)
        car = Car(engine, battery, tire)
        return car
    
    def create_glissade(last_service_date, current_mileage, last_service_mileage, today, wear_level):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, today)
        tire = CarriganTire(wear_level)
        car = car = Car(engine, battery, tire)
        return car
    
    def create_palindrome(last_service_date, warning_light_is_on, today, wear_level): 
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(last_service_date, today)
        tire = CarriganTire(wear_level)
        car = car = Car(engine, battery, tire)
        return car
    
    def create_rorschach(last_service_date, current_mileage, last_service_mileage, today, wear_level):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, today)#
        tire = CarriganTire(wear_level)
        car = car = Car(engine, battery, tire)
        return car

    def create_thovex(last_service_date, current_mileage, last_service_mileage, today, wear_level): 
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, today)
        tire = OctoprimeTire(wear_level)
        car = car = Car(engine, battery, tire)
        return car
