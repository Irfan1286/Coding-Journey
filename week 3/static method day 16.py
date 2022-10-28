
class direction:
    def __init__(self, place, arrow, meter, unit):
        self.place = place
        self.arrow = arrow
        self.meter = meter
        self.unit = unit

        if self.unit == 'km':
            self.meter = float(meter)*1000

    @classmethod
    def from_dash(cls, text):
        return cls(*text.split('_'))        #it means after split _ it will assign to variable such as in __init__

    @staticmethod               #static method is a decorator which doesn't take class or instance
    def total(add1, add2):
        return int(add1) + int(add2)

Home = direction.from_dash('Azampur_front_285_m')
School = direction.from_dash('Uttara_left then right then front_1.2_km')


total_meter = direction.total(Home.meter, School.meter)
print(total_meter, 'meter')
