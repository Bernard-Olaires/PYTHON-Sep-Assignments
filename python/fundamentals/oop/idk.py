class Driver:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.verified_license = False
        self.car = Vehical()

    def verified_driver_license(self):
        print("Driver license is verrified")
        self.verified_driver_license = True
        
    def is_allowed_to_drive(self):
        pass

class Vehical:
    def __init__(self, make, model, year, milage):
        self.make = make
        self.model = model
        self.year = year
        self.milage = milage
    
    def is_driving(self, mpg):
        print("I am driving down the road going ", mpg)
    
    def not_driving(self):
        print("I am no driving")
    
    def check_engine(self):
        if 95000 <= self.milage:
            print("Check Engine")
        return self


scion_tc = Vehical("Scion", "tC", 2013, 96500)

scion_tc.is_driving(15)
scion_tc.check_engine()

