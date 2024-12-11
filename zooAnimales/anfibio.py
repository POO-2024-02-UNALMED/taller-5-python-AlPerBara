from zooAnimales.animal import Animal

class Anfibio(Animal):
    listado=[]
    ranas=0
    salamandras=0

    def __init__(self, nombre="", edad=0, habitat="", genero="", colorPiel="", venenoso=False):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel=colorPiel
        self._venenoso=venenoso
        Anfibio.listado.append(self)

    def getColorPiel(self):
        return self._colorPiel
    
    def setColorPiel(self, piel):
        self._colorPiel= piel

    def isVenenoso(self):
        return self._venenoso
    
    def setVenenoso(self, veneno):
        self._venenoso=veneno

    

    @staticmethod
    def crearRana(nombre, edad, genero):
        Anfibio.ranas+=1
        return Anfibio(nombre, edad, "selva", genero, "rojo", True)

    @staticmethod
    def crearSalamandra(nombre, edad, genero):
        Anfibio.salamandras+=1
        return Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
    
    @staticmethod
    def cantidadAnfibios():
        return len(Anfibio.listado)
    
    def movimiento(self):
        return "saltar"