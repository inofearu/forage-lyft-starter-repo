from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class CarFactory:
    def create_calliope(last_service_date, current_mileage, last_service_mileage, today):
        #print(f"\n\n\n\n\nfactory time\n{today} / {last_service_date}\n\n\n\n\n")
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, today)
        car = Car(engine, battery)
        return car
    
    def create_glissade(last_service_date, current_mileage, last_service_mileage, today):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, today)
        car = Car(engine, battery)
        return car
    
    def create_palindrome(last_service_date, warning_light_is_on, today): 
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(last_service_date, today)
        car = Car(engine, battery)
        return car
    
    def create_rorschach(last_service_date, current_mileage, last_service_mileage, today):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, today)
        car = Car(engine, battery)
        return car

    def create_thovex(last_service_date, current_mileage, last_service_mileage, today): 
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, today)
        car = Car(engine, battery)
        return car
