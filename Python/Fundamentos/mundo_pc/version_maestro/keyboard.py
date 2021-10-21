from input_device import InputDevice

class Keyboard(InputDevice):
    mouse_counter = 0
    
    def __init__(self, brand, input_type):
        Keyboard.mouse_counter += 1
        self.__keyboard_id = Keyboard.mouse_counter
        self._brand = brand
        self._input_type = input_type
        
    def __str__(self):
        return (
            f'ID: {self.__keyboard_id}, '
            f'Brand: {self._brand}, '
            f'Input Type: {self._input_type}'
        )