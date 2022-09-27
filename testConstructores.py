from gestion.zona import Zona
from gestion.zoologico import Zoologico 
from zooAnimales.anfibio import Anfibio
from zooAnimales.ave import Ave
from zooAnimales.mamifero import Mamifero
from zooAnimales.pez import Pez
from zooAnimales.reptil import Reptil
from zooAnimales.animal import Animal

def testZoologico():
    zoo = Zoologico("Central park", "Calle Principal")
    ok = False
    if(zoo.getNombre() == "Central park"):
        ok = True
    assert(ok)

def testZona():
    zoo1 = Zoologico("Central perk", "Calle Principal")
    zona1 = Zona("salvaje", zoo1)
    zona2 = Zona("salvaje")
    ok = False
    if zona1.getNombre() == "salvaje" and zona1.getZoo().getNombre() == "Central perk" and zona2.getZoo() == None:
        ok = True
    assert(ok)

def testAnimal():
    an1 = Animal("Perro", 10, "casa", "m")
    ok = False
    if an1.getNombre() == "Perro" and an1.getEdad() == 10 and an1.getHabitat() == "casa" and an1.getGenero() == "m":
        ok = True
    assert(ok)

def testAnfibio():
    anf1 = Anfibio("rana", 5, "pradera", "F", "verde", False)
    ok = False
    if anf1.getNombre() == "rana" and anf1.getEdad() == 5 and anf1.getHabitat() == "pradera" and anf1.getGenero() == "F" and anf1.getColorPiel() == "verde" and anf1.isVenenoso() == False:
        ok = True
    assert(ok)

def testAve():
    ave1 = Ave("paloma", 5, "ciudad", "F", "gris")
    ok = False
    if ave1.getNombre() == "paloma" and ave1.getEdad() == 5 and ave1.getHabitat() == "ciudad" and ave1.getGenero() == "F" and ave1.getColorPlumas() == "gris":
        ok = True
    assert(ok)

def testMamifero():
    mam1 = Mamifero("persona", 50, "ciudad", "F", False, 2)
    ok = True
    if mam1.getNombre() == "persona" and mam1.getEdad() == 50 and mam1.getHabitat() == "ciudad" and mam1.getGenero() == "F" and mam1.isPelaje() == False and mam1.getPatas() == 2:
        ok = True
    assert(ok)

def testPez():
    pez1 = Pez("payaso", 5, "mar", "F", "azul", 3)
    ok = False
    if pez1.getNombre() == "payaso" and pez1.getEdad() == 5 and pez1.getHabitat() == "mar" and pez1.getGenero() == "F" and pez1.getColorEscamas() == "azul" and pez1.getCantidadAletas() == 3:
        ok = True
    assert(ok)

def testReptil():
    rep1 = Reptil("lagartija", 1, "casa", "F", "cafe", 1)
    ok = False
    if rep1.getNombre() == "lagartija" and rep1.getEdad() == 1 and rep1.getHabitat() == "casa" and rep1.getGenero() == "F" and rep1.getColorEscamas() == "cafe" and rep1.getLargoCola() == 1:
        ok = True
    assert(ok)