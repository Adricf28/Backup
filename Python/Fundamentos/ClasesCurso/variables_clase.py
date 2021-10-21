class myClass:
    classVariable = 'Class variable'
    def __init__(self, instanceVariable):
        self.instanceVariable = instanceVariable
        
print(myClass.classVariable)
o1 = myClass('Instance Variable')
#print(myClass.instanceVariable) # Las variables de instancia se llaman a traves de los objetos
print(o1.instanceVariable)       # Ya que no tienen valor definido en la clase, se lo dan los objetos en sí
myClass.instanceVariable = 'Modifying instance variable' # A no ser que le demos valor en la clase
print(myClass.instanceVariable) # Así se puede acceder desde ella en vez de desde el objeto

print('----------------------------------------------')
print(o1.classVariable) # Se puede acceder a las variables de clase desde los objetos

o1.classVariable = 'Modifying class variable'
print(o1.classVariable)      # Le puedes dar un valor a la variable de clase exclusivo de un objeto
print(myClass.classVariable)

o2 = myClass('New instance variable')
print(o2.classVariable)  # No tenemos el valor anterior ya que era exclusivo del primer objeto

o3 = myClass('Third object')
myClass.classVariable = 'Change from class'  # Si cambiamos el valor desde la clase se ve afectado
print(myClass.classVariable)                 # en todos los objetos a no ser que le hayamos dado 
print(o1.classVariable)                      # un valor exclusivo de ese objeto
print(o2.classVariable)  
print(o3.classVariable)