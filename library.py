class Microwave:
    def __init__(self, brand="Generic", power="strong"):
        self.brand = brand
        self.power = power


smeg1= Microwave('Smeg', 'B')
print(smeg1.brand)
print(smeg1.power)