from zooAnimales.animal import Animal

class Reptil(Animal):
    listado=[]
    iguanas=0
    serpientes=0

    def __init__(self, nombre="", edad=0, habitat="", genero="", zona=None, colorEscamas="", largoCola=0):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._colorEscamas=colorEscamas
        self._largoCola=largoCola
        Reptil.listado.append(self)

    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, escamas):
        self._colorEscamas=escamas

    def getLargoCola(self):
        return self._largoCola
    
    def setLargoCola(self, cola):
        self._largoCola=cola

    

    @staticmethod
    def crearIguana(nombre, edad, genero, zona=None):
        Reptil.iguanas+=1
        return Reptil(nombre, edad, "humedal", genero, zona, "verde", 3)

    @staticmethod
    def crearSerpiente(nombre, edad, genero, zona=None):
        Reptil.serpientes+=1
        return Reptil(nombre, edad, "jungla", genero, zona, "blanco", 1)
    
    @staticmethod
    def cantidadReptiles():
        return len(Reptil.listado)
    
    def movimiento(self):
        return "reptar"