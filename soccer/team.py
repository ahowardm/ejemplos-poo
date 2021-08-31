class Team:
    def __init__(self, name, city, color):
        self.name = name
        self.city = city
        self.color = color

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    def __str__(self):
        return f"Nombre: {self.name}, Ciudad: {self.city}, Color: {self.color}"
        # return "Nombre: " + self.name + "Ciudad: " + self.name + "Color: " + self.color