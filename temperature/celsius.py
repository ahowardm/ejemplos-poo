class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature
    
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, new_temperature):
        if new_temperature < -273.15:
            raise ValueError("Temperature is too low to be real.")
        self.__temperature = new_temperature