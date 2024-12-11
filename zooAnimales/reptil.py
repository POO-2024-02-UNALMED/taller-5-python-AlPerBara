from zooAnimales.animal import Animal

class Reptil(Animal):
    listado=[]
    iguanas=0
    serpientes=0

    def __init__(self, nombre="", edad=0, habitat="", genero="", colorEscamas="", largoCola=0):
        super().__init__(nombre, edad, habitat, genero)
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
    def crearIguana(nombre, edad, genero):
        Reptil.iguanas+=1
        return Reptil(nombre, edad, "humedal", genero, "verde", 3)

    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        Reptil.serpientes+=1
        return Reptil(nombre, edad, "jungla", genero, "blanco", 1)
    
    @staticmethod
    def cantidadReptiles():
        return len(Reptil.listado)
    
    def movimiento(self):
        return "reptar"