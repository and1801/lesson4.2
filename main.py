class Bird():
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color

    def fly(self):
        print(f'{self.name} летает')

    def eat(self):
        print(f'{self.name} ест')

    def sing(self):
        print(f'{self.name} поет чирик')

    def info(self):
        print(f'{self.name} - имя')
        print(f'{self.voice} - голос')
        print(f'{self.color} - цвет')

class Pigeon(Bird):
    def __init__(self, name, voice, color, favorite_food):
        super().__init__(name, voice, color)
        self.favorite_food = favorite_food
    def walk(self):
        print(f'{self.name} гуляет')
    def sing(self):
        print(f'{self.name} поет курлык')

bird1 = Pigeon('gosha', 'pisk', 'brown', 'хлебные крошки')
bird2 = Bird('masha', 'hru', 'blond')

bird1.sing()
bird1.info()
bird1.walk()
bird2.info()