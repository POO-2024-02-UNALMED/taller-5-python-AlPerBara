from zooAnimales.animal import Animal


class Ave(Animal):
    listado=[]
    halcones=0
    aguilas=0

    def __init__(self, nombre="", edad=0, habitat="", genero="", zona=None, colorPlumas=""):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._colorPlumas=colorPlumas
        Ave.listado.append(self)

    def getColorPlumas(self):
        return self._colorPlumas
    
    def setColorPlumas(self, colorNuevo):
        self._colorPlumas=colorNuevo

    

    @staticmethod
    def crearHalcon(nombre, edad, genero, zona=None):
        Ave.halcones+=1
        return Ave(nombre, edad, "montañas", genero, zona, "cafe glorioso")

    @staticmethod
    def crearAguila(nombre, edad, genero, zona=None):
        Ave.aguilas+=1
        return Ave(nombre, edad, "montañas", genero, zona, "blanco y amarillo")
    
    @staticmethod
    def cantidadAves():
        return len(Ave.listado)
    
    def movimiento(self):
        return "volar"