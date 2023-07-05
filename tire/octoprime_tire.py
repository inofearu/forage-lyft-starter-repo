from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, wear_level):
        self.wear_level = wear_level
    def needs_service(self):
        total_wear = 0
        for i in self.wear_level:
            total_wear += i
        if total_wear >= 3:
            return True
        else:
            return False