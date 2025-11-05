
class Shoot:
    def shoot(self):
        print("shoot")

class Navigate:
    def navigate(self):
        print("navigate")

class CallAirSupport:
    def call_air_support(self):
        print("call air support")

class Infantry(Shoot, Navigate):
    pass

class ForwardObserver(Shoot, CallAirSupport):
    pass

class Pilot(CallAirSupport):
    pass
