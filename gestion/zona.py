class Zona:
    def __init__(self, nombre, *zoo):
        self._nombre = nombre
        self._zoo = [None]
        if (len(zoo)>0 and zoo[0] != None):
            zoo[0].agregarZonas(self)
        self._animales = []

    def agregarAnimales(self, animal):
        self._animales.append(animal)
        animal.setZona([self])

    def cantidadAnimales(self):
        return len(self._animales)

    def getNombre(self, ):
        return self._nombre

    def getZoo(self, ):
        return self._zoo[0]

    def getAnimales(self, ):
        return self._animales

    def setNombre(self, nombre):
        self._nombre = nombre

    def setZoo(self, zoo):
        self._zoo[0] = zoo

    def setAnimales(self, animales):
        self._animales = animales
