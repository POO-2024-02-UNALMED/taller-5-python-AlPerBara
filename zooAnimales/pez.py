from zooAnimales.animal import Animal


class Pez(Animal):
    listado=[]
    salmones=0
    bacalaos=0

    def __init__(self, nombre="", edad=0, habitat="", genero="", colorEscamas="", cantidadAletas=0):
        super().__init__(nombre, edad, habitat, genero)
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
    def crearSalmon(nombre, edad, genero):
        Pez.salmones+=1
        return Pez(nombre, edad, "oceano", genero, "rojo", 6)

    @staticmethod
    def crearBacalao(nombre, edad, genero):
        Pez.bacalaos+=1
        return Pez(nombre, edad, "oceano", genero, "gris", 6)
    
    @staticmethod
    def cantidadPeces():
        return len(Pez.listado)
    
    def movimiento(self):
        return "nadar"