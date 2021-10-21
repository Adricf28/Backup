import monitor
import mouse
import keyboard

class PC:
    pc_counter = 0
    
    def __init__(self, pc_id, name, monitor, keyboard, mouse):
        self.__pc_id = pc_id
        self.__name = name
        self.__monitor = monitor
        self.__keyboard = keyboard
        self.__mouse = mouse
        
    def __str__(self):
        return f'ID: {self.__pc_id}, Name: {self.__name}, Monitor: {self.__monitor}, Keyboard: {self.__keyboard}, Mouse: {self.__mouse}'
    
    def getID(self):
        return self.__pc_id
    def setID(self, id):
        self.__pc_id = id

    def getName(self):
        return self.__name
    def setName(self, n):
        self.__name = n
        
    def getMonitor(self):
        return self.__monitor
    def setMonitor(self, m):
        self.__monitor = m
        
    def getKeyboard(self):
        return self.__keyboard
    def setKeyboard(self, k):
        self.__keyboard = k
        
    def getMouse(self):
        return self.__mouse
    def setMouse(self, mo):
        self.__mouse = mo