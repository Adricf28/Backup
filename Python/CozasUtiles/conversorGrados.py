class Temperature:
    def __init__(self, fahrenheit, celsius):
        self.fahrenheit = fahrenheit
        self.celsius = celsius
    def convertFahrenheit(self):
        ºC_to_ºF = (self.celsius * (9/5)) + 32
        return '{} grados celsius son {} grados fahrenheit.'.format(self.celsius, ºC_to_ºF)
    def convertCelsius(self):
        ºF_to_ºC = (self.fahrenheit - 32) * (5/9)
        return '{faren} grados fahrenheit son {conversion} grados celsius.'.format(faren = self.fahrenheit, conversion =  ºF_to_ºC)
    
temperature1 = Temperature(int(input('Fahrenheit: ')), int(input('Celsius: ')))
print('Celsius a farenheit:', temperature1.convertFahrenheit(), '\n' + 'Fahrenheit a celsius:', temperature1.convertCelsius())