class Guerrero:

    def __init__(self, nombre, ataque, movimiento, defensa, salud, alcance):
        self.__nombre = nombre
        self.__ataque = ataque
        self.__movimiento = movimiento
        self.__defensa = defensa
        self.__salud = salud
        self.__alcance = alcance

    def atributos(self):
        print(self.__nombre, ":", sep="")
        print("Salud:", self.__salud)
        print("Ataque:", self.__ataque)
        print("Defensa:", self.__defensa)
        print("Movimiento:", self.__movimiento)
        print("Alcance", self.__alcance)

    def subir_nivel(self, ataque, movimiento, defensa):
        self.__ataque = self.__ataque + ataque
        self.__movimiento = self.__movimiento + movimiento
        self.__defensa = self.__defensa + defensa

    def esta_vivo(self):
        return self.__salud > 0

    def morir(self):
        self.__salud = 0
        print(self.__nombre, "ha muerto")

    def daño(self, enemigo):
        return self.__ataque - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.salud = enemigo.salud - daño
        print(self.__nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.salud)
        else:
            enemigo.morir()

    def get_ataque(self):
        return self.__ataque


personaje = Guerrero("Guerrero", 2, 1, 2, 10, 1)
print("Ataque............", personaje.get_ataque())
