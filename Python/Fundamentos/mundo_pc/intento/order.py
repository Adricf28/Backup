from pc import PC
from monitor import Monitor
from mouse import Mouse
from keyboard import Keyboard
import random

class Order:
    order_counter = 0
    pcs = []
    
    def __init__(self, order_id):
        self.__order_id = order_id 
        
    def addPC(self):
        while True:
            option = int(input('1- Add PC, 2- Close '))
            if option == 1:
                self.order_counter += 1
                mouseID_number = random.randint(1,9999)
                print(f'Mouse ID: {mouseID_number}')
                mouse = Mouse(mouseID_number, 'Mouse', input('Mouse brand: '))
                keyboardID_number = random.randint(1,9999)
                print(f'Keyboard ID: {keyboardID_number}')
                keyboard = Keyboard(keyboardID_number, 'Keyboard', input('Keyboard brand: '))
                monitorID_number = random.randint(1,9999)
                print(f'Monitor ID: {monitorID_number}')
                monitor = Monitor(monitorID_number, input('Monitor brand: '), input('Monitor size: '))
                PCID_number = random.randint(1,9999)
                print(f'PC ID: {PCID_number}')
                pc = PC(PCID_number, input('PC Name: '), monitor, keyboard, mouse)
                self.pcs.append(f'ID: {pc.getID()}, PC Name: {pc.getName()}, Monitor{pc.getMonitor()}, Keyboard{pc.getKeyboard()}, Mouse{pc.getMouse()}')
            elif option == 2:
                break
            else:
                print('Choose a valid option.')
        
    def __str__(self):
        return f'Order ID: {self.__order_id}, Order counter: {self.order_counter}, Order: {self.pcs}'
        
    def getID(self):
        return self.__order_id
    def setID(self, id):
        self.__order_id = id    
        

order1 = Order(1)
order2 = Order(2)
order1.addPC()
order2.addPC()
print(order1)
print(order2)