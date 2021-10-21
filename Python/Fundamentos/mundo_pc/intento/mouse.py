from input_device import InputDevice

class Mouse(InputDevice):
    mouse_counter = 0
    
    def __init__(self, mouse_id, input_type, brand):
        super().__init__(input_type, brand)
        self.__mouse_id = mouse_id
        
    def __str__(self):
        return f'ID: {self.__mouse_id}, InputType: {self.getInputType()}, Brand: {self.getBrand()}'