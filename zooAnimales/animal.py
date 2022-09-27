class Animal:
    _totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = []
        Animal._totalAnimales += 1

    def movimieto(self):
        return "desplazarse"

    def toString(self):
        response = "Mi nombre es " + str(self._nombre) + ", tengo una edad de " + str(self._edad) + ", habito en " + str(self._habitat) + " y mi genero es " + str(self._genero)
        if (len(self._zona) > 0):
            response += "la zona en la que me ubico es " + str(self._zona[0].getNombre()) + " , en el " + str(self._zona[0].getZoo().getNombre())
        return response

    @staticmethod
    def totalPorTipo():
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.ave import Ave
        from zooAnimales.reptil import Reptil
        from zooAnimales.pez import Pez
        from zooAnimales.anfibio import Anfibio
        childs = [Mamifero, Ave, Reptil, Pez, Anfibio]
        response = ""
        for child in range(0, len(childs)):
            response += childs[child]._plural + " : " + str(
                childs[child].__getattribute__(childs[child], "cantidad" + childs[child]._plural).__get__(childs[child])())
            if (child + 1 != len(childs)):
                response += "\n"
        return response

    def getTotalAnimales(cls, ):
        return cls.totalAnimales

    def getNombre(self, ):
        return self._nombre

    def getEdad(self, ):
        return self._edad

    def getHabitat(self, ):
        return self._habitat

    def getGenero(self, ):
        return self._genero

    def getZona(self, ):
        return self._zona

    @classmethod
    def setTotalAnimales(cls, totalAnimales):
        cls.totalAnimales = totalAnimales

    def setNombre(self, nombre):
        self._nombre = nombre

    def setEdad(self, edad):
        self._edad = edad

    def setHabitat(self, habitat):
        self._habitat = habitat

    def setGenero(self, genero):
        self._genero = genero

    def setZona(self, zona):
        self._zona = zona

