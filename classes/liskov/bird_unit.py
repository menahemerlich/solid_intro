
class FlyingUnit:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name}: I cen fly.")

class GroundUnit:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name}: I cen not fly.")

class Drone(FlyingUnit):
    pass

class Tank(GroundUnit):
    pass




