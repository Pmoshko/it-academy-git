class Building:
    def __init__(self, wall_1: float, wall_2: float, number_of_storeys: int):
        self.wall_1 = wall_1
        self.wall_2 = wall_2
        self.number_of_storeys = number_of_storeys

    def floor_area(self):
        return print(f" Площадь здания:{self.wall_1*self.wall_2}")


class Cars:
    def __init__(self, model: str, length: float, width: float, power: int, volume: float, class_car: str, prise: float):
        self.model = model
        self.length = length
        self.width = width
        self.power = power
        self.volume = volume
        self.class_car = class_car
        self.prise = prise

    def parking_space_size(self):
        if isinstance(self, Cars):
            return print(f'парковочная площадь: {self.length*self.width}')

    def __gt__(self, other):
        if isinstance(other, Cars):
            return self.volume > other.volume
        raise ValueError("Внесите экземпляр класса 'Cars'")

    def __eq__(self, other):
        if isinstance(other, Cars):
            return self.volume == other.volume
        raise ValueError("Внесите экземпляр класса 'Cars'")

    def __lt__(self, other):
        if isinstance(other, Cars):
            return self.volume < other.volume
        raise ValueError("Внесите экземпляр класса 'Cars'")

    def __le__(self, other):
        if isinstance(other, Cars):
            return self.volume <= other.volume or self.power <= other.power
        raise ValueError("Внесите экземпляр класса 'Cars'")

    def __ge__(self, other):
        if isinstance(other, Cars):
            return self.volume >= other.volume
        raise ValueError("Внесите экземпляр класса 'Cars'")

class Staff:
    number_of_staff = 0

    def __init__(self, surname: str, name: str, age: int, position: str):
        self.surname = surname
        self.name = name
        self.age = age
        self.position = position
        Staff.number_of_staff = Staff.number_of_staff + 1

    @property
    def stuff_info(self):
        return f"{self.surname} {self.name}, {self.age} - {self.position}"

    @stuff_info.setter
    def stuff_info(self, new_information: dict):
        for key, value in new_information.items():
            if self.__dict__.get(key):
                self.__dict__[key] = value

    @stuff_info.deleter
    def stuff_info(self):
        del self.surname
        del self.name
        del self.age
        del self.position

    @classmethod
    def total_object(cls):
        print(f"Total number of stuff:{cls.number_of_staff}")


class SalesOffice(Building):
    count_stuff = []

    def __init__(self, wall_1: float, wall_2: float, number_of_storeys: int, number_of_workplaces: int):
        super().__init__(wall_1, wall_2, number_of_storeys)
        self.number_of_workplaces = number_of_workplaces

    def add_stuff(self, stuff):
        self.count_stuff.append(stuff)

    @staticmethod
    def counter():
        if len(SalesOffice.count_stuff) > 1:
            print(f"There are {len(SalesOffice.count_stuff)} people working in the sales office")
        elif len(SalesOffice.count_stuff) == 1:
            print(f"There is {len(SalesOffice.count_stuff)} person working in the sales office")
        else:
            print("No employees in the sales office ")


class ShowRoom(Building):
    car_in_showroom = []

    def __init__(self, wall_1: float, wall_2: float, number_of_storeys: int, number_of_car_space: int):
        super().__init__(wall_1, wall_2, number_of_storeys )
        self.number_of_car_space = number_of_car_space

    def add_car(self, car):
        self.car_in_showroom.append(car)

    @staticmethod
    def welcome():
        print(f'Welcome to our showroom\n'
              f'There are {len(ShowRoom.car_in_showroom)} cars in our showroom\n'
              f'The following cars are presented in our showroom: {ShowRoom.car_in_showroom}')


class OrderCar(Cars):
    def __init__(self, model:str,  length: float, width: float, power: int, volume: float, class_car: str, prise: float):
        super().__init__(model, length, width, power, volume, class_car, prise)

    def write_file(self):
        with open("car_file.txt", 'w+') as file:
            file.write(f" Order - {self.__str__()}\n")
            file.write(f" Length - {self.length}\n")
            file.write(f" Width - {self.width}\n")
            file.write(f" Power - {self.power}\n")
            file.write(f" Volume - {self.volume}\n")
            file.write(f" Class Car - {self.class_car}\n")
            file.write(f" Total Prise - {self.prise}\n")


# p1 = Staff("Mashko", "Pavel", 33, "Boss")
# p2 = Staff("Marchenko", "Oksana", 34, "deputy Boss")
o1 = SalesOffice(3,2,2,3)
# o1.add_stuff(p1.surname)
# o1.add_stuff(p2.surname)
print(o1.count_stuff)
SalesOffice.counter()
bmw = Cars('BMW X6', 3.2, 2.5, 500, 3.0, 'S',100000)
audi = Cars('AUDI Q8', 3.2, 2.5, 400, 3.0, 'S',150000)
s1 = ShowRoom(50.5,30.5, 1, 3)
s1.add_car(bmw.model)
s1.add_car(audi.model)
ShowRoom.welcome()
print(bmw <= audi)