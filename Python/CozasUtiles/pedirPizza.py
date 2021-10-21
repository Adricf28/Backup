# 5.- La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Pepperoni, Jamón y Salmón.

# 6.- Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles 
# para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla 
# si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.


pedido = []

while True:
    vegetariana = ['mozzarella', 'tomate']
    noVegetariana = ['mozzarella', 'tomate']
    opcion = int(input('1- Pedir, 2- Listar orden, 3- Cerrar '))
    if opcion == 1:
        print('Todas las pizzas llevan mozzarella y tomate.')
        pizzas = int(input('Elige una pizza: 1- Vegetariana, 2- No Vegetariana '))
        if pizzas == 1:
            ingredienteVegetariana = int(input('Elige un ingrediente extra: 1- Pimiento, 2- Tofu '))
            if ingredienteVegetariana == 1:
                vegetariana.append('pimiento')
                pedido.append(vegetariana)
                print('Ha pedido una pizza vegetariana con:', vegetariana[0], ',', vegetariana[1], 'y', vegetariana[2])
            if ingredienteVegetariana == 2:
                vegetariana.append('tofu')
                pedido.append(vegetariana)
                print('Ha pedido una pizza vegetariana con:', vegetariana[0], ',', vegetariana[1], 'y', vegetariana[2])
            elif ingredienteVegetariana != 1 and ingredienteVegetariana != 2:
                print('Elige una opcion valida')
        if pizzas == 2:
            ingredienteNoVegetariana = int(input('Elige un ingrediente extra: 1- Pepperoni, 2- Jamón, 3- Salmón '))
            if ingredienteNoVegetariana == 1:
                noVegetariana.append('pepperoni')
                pedido.append(noVegetariana)
                print('Ha pedido una pizza no vegetariana con:', noVegetariana[0], ',', noVegetariana[1], 'y', noVegetariana[2])
            if ingredienteNoVegetariana == 2:
                noVegetariana.append('jamón')
                pedido.append(noVegetariana)
                print('Ha pedido una pizza no vegetariana con:', noVegetariana[0], ',', noVegetariana[1], 'y', noVegetariana[2])
            if ingredienteNoVegetariana == 3:
                noVegetariana.append('salmón')
                pedido.append(noVegetariana)
                print('Ha pedido una pizza no vegetariana con:', noVegetariana[0], ',', noVegetariana[1], 'y', noVegetariana[2])
            elif ingredienteNoVegetariana != 1 and ingredienteNoVegetariana != 2 and ingredienteNoVegetariana != 3:
                print('Elige una opcion valida')
        elif pizzas != 1 and pizzas != 2:
            print('Elige una opcion valida')
    elif opcion == 2:
        print(pedido)
    else:
        print('Elige una opcion valida')
                