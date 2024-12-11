from zooAnimales.animal import Animal


class Mamifero(Animal):
    listado=[]
    caballos=0
    leones=0

    def __init__(self, nombre="", edad=0, habitat="", genero="", zona=None, pelaje=False, patas=0):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._pelaje=pelaje
        self._patas=patas
        Mamifero.listado.append(self)

    def isPelaje(self):
        return self._pelaje
    
    def setPelaje(self, pelaje):
        self._pelaje=pelaje

    def getPatas(self):
        return self._patas
    
    def setPatas(self, patasNuevo):
        self._patas=patasNuevo

    

    @staticmethod
    def crearCaballo(nombre, edad, genero, zona=None):
        Mamifero.caballos+=1
        return Mamifero(nombre, edad, "pradera", genero, zona, True, 4)

    @staticmethod
    def crearLeon(nombre, edad, genero, zona=None):
        Mamifero.leones+=1
        return Mamifero(nombre, edad, "selva", genero, zona, True, 4)
    
    @staticmethod
    def cantidadMamiferos():
        return len(Mamifero.listado)