from zooAnimales.animal import Animal


class Pez(Animal):
    _plural = "Peces"
    _listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._listado.append(self)

    @classmethod
    def cantidadPeces(cls):
        return len(Pez._listado)

    def movimieto(self):
        return "nadar"

    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        cls.salmones += 1
        return cls(nombre, edad, "oceano", genero, "rojo", 7)

    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        cls.bacalaos += 1
        return cls(nombre, edad, "oceano", genero, "gris", 7)

    @classmethod
    def getListado(cls):
        return cls._listado

    def getColorEscamas(self, ):
        return self._colorEscamas

    def getCantidadAletas(self, ):
        return self._cantidadAletas

    @classmethod
    def setListado(cls, listado):
        cls._listado = listado

    def setColorEscamas(self, value):
        self._colorEscamas = value

    def setCantidadAletas(self, value):
        self._cantidadAletas = value