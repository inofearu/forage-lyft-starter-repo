from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, wear_level):
        self.wear_level = wear_level
    def needs_service(self):
        for i in self.wear_level:
            if i >= 0.9:
                return True
        return False