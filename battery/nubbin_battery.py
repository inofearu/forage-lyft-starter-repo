from sys import path
path.append("C:\\Users\\Inofearu\\Desktop\\Work\\Work Experience\\forage-lyft-starter-repo")
from battery.battery import Battery
from time_manager import *

class NubbinBattery(Battery):
    def __init__(self, last_service_date, today):
        self.today = today
        self.last_service_date = last_service_date
    def needs_service(self):
        service_by = add_years(self.last_service_date,4)
        if service_by < self.today:
            return True
        else:
            return False