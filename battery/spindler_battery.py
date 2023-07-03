from sys import path
path.append("C:\\Users\\Inofearu\\Desktop\\Work\\Work Experience\\forage-lyft-starter-repo")
from battery import Battery
from time_manager import *

class SpindlerBattery(Battery):
    def __init__(self,last_service_date):
        self.current_date = get_time()
        self.last_service_date = last_service_date
    def needs_service(self):
        service_by = add_years(self.current_date,2)
        if service_by < self.current_date:
            return True
        else:
            return False