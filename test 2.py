class Building:
    def __init__(self, wall_1: float, wall_2: float, number_of_storeys: int):
        self.wall_1 = wall_1
        self.wall_2 = wall_2
        self.number_of_storeys = number_of_storeys

    def floor_area(self):
        return print(f" Площадь здания:{self.wall_1*self.wall_2}")

class Cars:
    def __init__(self, length: float, width: float, power: int, volume: float, class_car: str, prise: float):
        self.length = length
        self.width = width
        self.power = power
        self.volume = volume
        self.class_car = class_car
        self.prise = prise

    def parking_space_size(self):
        if isinstance(self, Cars):
            return print(f'парковочная площадь: {self.length*self.width}')
class ShowRoom(Building):
    cars_showroom = []
    def __init__(self, wall_1: float, wall_2: float, number_of_storeys: int, number_of_car_space: int):
        super().__init__(wall_1, wall_2, number_of_storeys )
        self.number_of_car_space = number_of_car_space

    def add_car(self):
        self.cars_showroom.append()
        return print(self.cars_showroom)


if __name__ == "__main__":
    bmw = Cars(3,2, 300, 2.5, "b",100000)
    audi = Cars(5.3,2, 400, 2.5, "b",300000)

    b1 = ShowRoom(5,3,2,5)
    ShowRoom.add_car(bmw)
