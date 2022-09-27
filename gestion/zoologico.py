class Zoologico:
    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []

    def agregarZonas(self, zona):
        self._zonas.append(zona)
        zona.setZoo(self)

    def cantidadTotalAnimales(self):
        count = 0
        for zona in self._zonas:
            count += zona.cantidadAnimales()
        return count

    def getNombre(self, ):
        return self._nombre

    def getUbicacion(self, ):
        return self._ubicacion

    def getZona(self, ):
        return self._zonas

    def setNombre(self, nombre):
        self._nombre = nombre

    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion

    def setZona(self, zonas):
        self._zonas = zonas
