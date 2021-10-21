class Monitor:
    monitor_counter = 0
    
    def __init__(self, monitor_id, brand, size):
        self.__monitor_id = monitor_id
        self.__brand = brand
        self.__size = size
        
    def __str__(self):
        return f'ID: {self.__monitor_id}, Brand: {self.__brand}, Size: {self.__size}'
    
    def getID(self):
        return self.__monitor_id
    def setID(self, id):
        self.__monitor_id = id
        
    def getBrand(self):
        return self.__brand
    def setBrand(self, b):
        self.__brand = b
        
    def getSize(self):
        return self.__size
    def setSize(self, s):
        self.__size = s