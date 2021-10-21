from producto import Producto


class Orden:
    contador_ordenes = 0
    
    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self.__id_orden = Orden.contador_ordenes
        self.__productos = productos
        
    def agregarProducto(self, producto):
        self.__productos.append(producto)
    
    def calcularTotal(self):
        total = 0
        for producto in self.__productos:
            total += producto.getPrecio()
        return total
        
    def __str__(self):
        productos_str = ''
        for producto in self.__productos:
            productos_str += producto.__str__()
        return 'ID Orden: ' + str(self.__id_orden) + ', Productos: ' + productos_str