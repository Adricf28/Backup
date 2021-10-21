from input_device import InputDevice

class Keyboard(InputDevice):
    keyboard_counter = 0
    
    def __init__(self, keyboard_id, input_type, brand):
        super().__init__(input_type, brand)
        self.__keyboard_id = keyboard_id
        
    def __str__(self):
        return f'ID: {self.__keyboard_id}, InputType: {self.getInputType()}, Brand: {self.getBrand()}'
