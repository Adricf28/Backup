class InputDevice:
    def __init__(self, input_type, brand):
        self._input_type = input_type
        self._brand = brand
        
    def getInputType(self):
        return self._input_type
    def setInputType(self, t):
        self._input_type = t
    def getBrand(self):
        return self._brand
    def setBrand(self, b):
        self._brand = b