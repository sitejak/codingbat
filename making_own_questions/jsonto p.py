import json
class Vehicle():

    def __init__(self,name,brand,year):
        self.name = name
        self.brand = brand
        self.year = year




v1 = json.loads('{"name":"toyota","brand":"corolla","year":2020}')
print(v1)
