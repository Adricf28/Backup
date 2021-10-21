from order import Order
from computer import Computer
from monitor import Monitor
from mouse import Mouse
from keyboard import Keyboard

razerKeyboard = Keyboard('Razer', 'USB')
razerMouse = Mouse('Razer', 'USB')
razerMonitor = Monitor('Razer', '27 inches')
razerComputer = Computer('Razer', razerMonitor, razerKeyboard, razerMouse)

asusKeyboard = Keyboard('Asus ROG', 'Bluetooth')
asusMouse = Mouse('Asus ROG', 'Bluetooth')
asusMonitor = Monitor('Asus ROG', '22 inches')
asus_computer = Computer('Asus ROG', asusMonitor, asusKeyboard, asusMouse)

hpKeyboard = Keyboard('HP', 'USB')
hpMouse = Mouse('HP', 'USB')
hpMonitor = Monitor('HP', '24 inches')
hp_computer = Computer('HP', hpMonitor, hpKeyboard, hpMouse)

mixed_computer = Computer('Mixed', razerMonitor, asusKeyboard, hpMouse)

computers1 = [razerComputer, asus_computer]
order1 = Order(computers1)
order1.addComputer(hp_computer)
print(order1)

computers2 = [hp_computer, razerComputer, mixed_computer]
order2 = Order(computers2)
print(order2)