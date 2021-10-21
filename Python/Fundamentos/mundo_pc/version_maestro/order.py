class Order:
    order_counter = 0
    
    def __init__(self,computers):
        Order.order_counter += 1
        self.__order_id = Order.order_counter
        self.__computers = computers
        
    def addComputer(self, computer):
        self.__computers.append(computer)
    def __str__(self):
        computer_str = ''
        for i in self.__computers:
            computer_str += i.__str__()
        return (
            f'Order: {self.__order_id}, '
            f'Computers: {computer_str}'
        )
    def getID(self):
        return self.__order_id
    def getComputers(self):
        return self.__computers