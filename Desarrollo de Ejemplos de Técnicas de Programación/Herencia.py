class Guerrero:

    def __init__(self, nombre, ataque, defensa, salud):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("Salud.........", self.salud)
        print("Ataque........", self.ataque)
        print("Defensa.......", self.defensa)

    def subir_nivel(self, ataque, salud, defensa):
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


class Caballero(Guerrero):

    def __init__(self, nombre, ataque, defensa, salud, espada):
        super().__init__(nombre, ataque, defensa, salud)
        self.espada = espada

    def atributos(self):
        super().atributos()
        print("Espada........", self.espada)

    def daño(self, enemigo):
        return self.ataque * self.espada - enemigo.defensa


class Escudo(Guerrero):

    def __init__(self, nombre, ataque, defensa, salud, escudo):
        super().__init__(nombre, ataque, defensa, salud)
        self.escudo = escudo

    def atributos(self):
        super().atributos()
        print("Escudo........", self.escudo)

    def daño(self, enemigo):
        return self.defensa * self.escudo - enemigo.defensa


personaje_1 = Guerrero("Guerrero", 20, 10, 5)
personaje_2 = Caballero("Caballero", 2, 1, 100, 1.2)
personaje_3 = Escudo("Escudero", 5, 15, 10, 1.5)

personaje_1.atributos()
personaje_2.atributos()
personaje_3.atributos()
