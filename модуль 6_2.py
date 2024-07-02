class Vehicle:
    __COLOR_VARIANTS = ['blue', 'black', 'red', 'green']

    def __init__(self, owner: str, model: int, engine_power: str, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model(), self.get_horsepower(), self.get_color(),
              f'Владелец: {self.owner}', sep='\n', end='\n\n')

    def set_color(self, new_color: str):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'\033[33mНельзя сменить цвет на {new_color}\033[0m')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Alexey', 'Audi A7', 450, 'white')

vehicle1.print_info()

vehicle1.set_color('желтый')
vehicle1.set_color('black')
vehicle1.owner = 'Oleg'

vehicle1.print_info()
