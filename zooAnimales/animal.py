
class Animal:
    totalAnimales=0

    def __init__(self, nombre="", edad=0, habitat="", genero="", zona=None):
        self._nombre=nombre
        self._edad=edad
        self._habitat=habitat
        self._genero=genero
        self._zona=zona
        Animal.totalAnimales+=1

    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombreNuevo):
        self._nombre=nombreNuevo

    def getEdad(self):
        return self._edad
    
    def setEdad(self, edadNueva):
        self._edad=edadNueva

    def getHabitat(self):
        return self._habitat
    
    def setHabitat(self, habitatNueva):
        self._habitat=habitatNueva

    def getGenero(self):
        return self._genero
    
    def setGenero(self, generoNuevo):
        self._genero=generoNuevo

    def getZona(self):
        return self._zona
    
    def setZona(self, zonaNueva):
        self._zona=zonaNueva


    
    @staticmethod
    def totalPorTipo():
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.ave import Ave
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil
        return f"Mamíferos: {Mamifero.cantidadMamiferos()}\n" \
               f"Aves: {Ave.cantidadAves()}\n" \
               f"Reptiles: {Reptil.cantidadReptiles()}\n" \
               f"Peces: {Pez.cantidadPeces()}\n" \
               f"Anfibios: {Anfibio.cantidadAnfibios()}"
    
    def movimiento(self):
        return "desplazarse"
    
    def toString(self):
        if self._zona:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona._nombre}, en el {self._zona._zoo._nombre}."
        
        else:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"