# código abstraído
class Guerrero:

    def __init__(self, nombre, ataque, defensa, salud):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("Salud:", self.salud)
        print("Ataque:", self.ataque)
        print("Defensa:", self.defensa)

    def subir_nivel(self, ataque, salud, defensa, enemigo):
        self.ataque = self.ataque + ataque
        self.salud = self.salud + salud
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        return self.salud > 0

    def morir(self):
        self.salud = 0
        print(self.nombre, "ha muerto")

    def daño(self, enemigo):
        return self.ataque - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.salud = enemigo.salud - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.salud)
        else:
            enemigo.morir()


personaje = Guerrero("Guerrero", 4, 1, 10)
enemigo = Guerrero("Caballero", 1, 4, 50)
personaje.atacar(enemigo)
