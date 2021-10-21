from monitor import Monitor
from mouse import Mouse
from keyboard import Keyboard

class Computer:
    computer_counter = 0
    
    def __init__(self, name, monitor, keyboard, mouse):
        Computer.computer_counter += 1
        self.__computer_id = Computer.computer_counter
        self.__name = name
        self.__monitor = monitor
        self.__keyboard = keyboard
        self.__mouse = mouse
        
    def __str__(self):
        return (
            f"""
            {self.__name}, ID: {self.__computer_id}
                Monitor: {self.__monitor}
                Keyboard: {self.__keyboard}
                Mouse: {self.__mouse}
            """
        )
        
    def getID(self):
        return self.__computer_id
    def getName(self):
        return self.__name
    def setName(self, n):
        self.__name = n