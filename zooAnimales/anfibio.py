from zooAnimales.animal import Animal


class Anfibio(Animal):
    _plural = "Anfibios"
    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)

    @classmethod
    def cantidadAnfibios(cls):
        return len(Anfibio._listado)

    def movimieto(self):
        return "saltar"

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        cls.ranas += 1
        return cls(nombre, edad, "selva",genero,"rojo", True)

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        cls.salamandras += 1
        return cls(nombre, edad, "selva",genero,"negro y amarillo", False)

    @classmethod
    def getListado(cls):
        return cls._listado

    def getColorPiel(self, ):
        return self._colorPiel

    def isVenenoso(self, ):
        return self._venenoso

    @classmethod
    def setListado(cls, listado):
        cls._listado = listado

    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel

    def setVenenoso(self, venenoso):
        self._venenoso = venenoso
