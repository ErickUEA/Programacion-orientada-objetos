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
        print(self.nombre, f"ha realizado {daño:.2f} puntos de daño a", enemigo.nombre)
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


def combate(personaje_1, personaje_2):
    turno = 1
    while personaje_1.esta_vivo() and personaje_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de ", personaje_1.nombre, ":", sep="")
        personaje_1.atacar(personaje_2)
        print(">>> Acción de ", personaje_2.nombre, ":", sep="")
        personaje_2.atacar(personaje_1)
        turno = turno + 1
        if turno == 4:
            personaje_1.subir_nivel(2, 2, 1.9)
            personaje_2.subir_nivel(2, 2, 0.2)
            print("El personaje", personaje_1.nombre, "y el personaje", personaje_2.nombre, "han subido de nivel")
        else:
            if personaje_1.esta_vivo():
                print("\nHa ganado", personaje_1.nombre)
            elif personaje_2.esta_vivo():
                print("\nHa ganado", personaje_2.nombre)
            else:
                print("\nEmpate")


jugador_1 = Guerrero("Guerrero", 2, 2, 5)
jugador_2 = Caballero("Caballero", 5, 1, 100, 1.2)
jugador_3 = Escudo("Escudero", 3, 5, 10, 2)

combate(jugador_2, jugador_3)
