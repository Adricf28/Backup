from input_device import InputDevice

class Mouse(InputDevice):
    mouse_counter = 0
    
    def __init__(self, brand, input_type):
        Mouse.mouse_counter += 1
        self.__mouse_id = Mouse.mouse_counter
        self._brand = brand
        self._input_type = input_type
        
    def __str__(self):
        return (
            f'ID: {self.__mouse_id}, '
            f'Brand: {self._brand}, '
            f'Input type: {self._input_type}'
        )