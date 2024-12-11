from zooAnimales.Animal import Animal


class Pez(Animal):
    listado=[]
    salmones=0
    bacalaos=0

    def __init__(self, nombre="", edad=0, habitat="", genero="", zona=None, colorEscamas="", cantidadAletas=0):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._colorEscamas=colorEscamas
        self._cantidadAletas=cantidadAletas
        Pez.listado.append(self)

    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, escamas):
        self._colorEscamas=escamas

    def getCantidadAletas(self):
        return self._cantidadAletas
    
    def setCantidadAletas(self, aletas):
        self._cantidadAletas=aletas

    

    @staticmethod
    def crearSalmon(nombre, edad, genero, zona=None):
        Pez.salmones+=1
        return Pez(nombre, edad, "oceano", genero, zona, "rojo", 6)

    @staticmethod
    def crearBacalao(nombre, edad, genero, zona=None):
        Pez.bacalaos+=1
        return Pez(nombre, edad, "oceano", genero, zona, "gris", 6)
    
    @staticmethod
    def cantidadPeces():
        return len(Pez.listado)
    
    def movimiento(self):
        return "nadar"