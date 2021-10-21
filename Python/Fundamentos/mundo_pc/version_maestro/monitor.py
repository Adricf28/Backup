class Monitor:
    monitor_counter = 0
    
    def __init__(self, brand, size):
        Monitor.monitor_counter += 1
        self.__monitor_id = Monitor.monitor_counter
        self.__brand = brand
        self.__size = size
        
    def __str__(self):
        return (
            f'ID: {self.__monitor_id}, '
            f'Brand: {self.__brand}, '
            f'Size: {self.__size}'
        )
        
    def getID(self):
        return self.__monitor_id
    def getBrand(self):
        return self.__brand
    def setBrand(self, b):
        self.__brand = b
    def getSize(self):
        return self.__size
    def setSize(self, s):
        self.__size = s