from abc import ABC, abstractmethod

# Clase base abstracta para los personajes
class PersonajeBase(ABC):

    def __init__(self, nombre, agilidad, magia, resistencia, vida):
        self.nombre = nombre
        self.agilidad = agilidad
        self.magia = magia
        self.resistencia = resistencia
        self.vida = vida

    def atributos(self):
        # Imprime los atributos del personaje
        print(self.nombre, ":", sep="")
        print("·Agilidad:", self.agilidad)
        print("·Magia:", self.magia)
        print("·Resistencia:", self.resistencia)
        print("·Vida:", self.vida)

    def subir_nivel(self, agilidad, magia, resistencia):
        # Incrementa los atributos del personaje
        self.agilidad = self.agilidad + agilidad
        self.magia = self.magia + magia
        self.resistencia = self.resistencia + resistencia

    def esta_vivo(self):
        # Verifica si el personaje sigue vivo
        return self.vida > 0

    def morir(self):
        # Marca al personaje como muerto
        self.vida = 0
        print(self.nombre, "ha muerto")

    @abstractmethod
    def daño(self, enemigo):
        # Método abstracto que debe ser implementado por las subclases para calcular el daño
        pass

    def atacar(self, enemigo):
        # Realiza un ataque a otro personaje
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

# Clase para personajes de tipo Arquero, que hereda de PersonajeBase
class Arquero(PersonajeBase):

    def __init__(self, nombre, agilidad, magia, resistencia, vida, arco):
        super().__init__(nombre, agilidad, magia, resistencia, vida)
        self.arco = arco

    def cambiar_arma(self):
        # Permite al arquero cambiar de arma
        opcion = int(input("Elige un arco: (1) Arco Largo, daño 5. (2) Arco Corto, daño 3"))
        if opcion == 1:
            self.arco = 5
        elif opcion == 2:
            self.arco = 3
        else:
            print("Número de arco incorrecto")

    def atributos(self):
        # Imprime los atributos del arquero
        super().atributos()
        print("·Arco:", self.arco)

    def daño(self, enemigo):
        # Calcula el daño que el arquero inflige basado en su agilidad y el arco
        return self.agilidad * self.arco - enemigo.resistencia

# Clase para personajes de tipo Hechicero, que hereda de PersonajeBase
class Hechicero(PersonajeBase):

    def __init__(self, nombre, agilidad, magia, resistencia, vida, cetro):
        super().__init__(nombre, agilidad, magia, resistencia, vida)
        self.cetro = cetro

    def atributos(self):
        # Imprime los atributos del hechicero
        super().atributos()
        print("·Cetro:", self.cetro)

    def daño(self, enemigo):
        # Calcula el daño que el hechicero inflige basado en su magia y el cetro
        return self.magia * self.cetro - enemigo.resistencia


# Función para simular el combate entre dos personajes
def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() & jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de ", jugador_1.nombre, ":", sep="")
        jugador_1.atacar(jugador_2)
        if jugador_2.esta_vivo():
            print(">>> Acción de ", jugador_2.nombre, ":", sep="")
            jugador_2.atacar(jugador_1)
        turno = turno + 1
    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.nombre)
    else:
        print("\nEmpate")

# Crear instancias de personajes y mostrar sus atributos
personaje_1 = Arquero("Legolas", 18, 5, 3, 80, 4)
personaje_2 = Hechicero("Gandalf", 7, 20, 5, 80, 4)

personaje_1.atributos()
personaje_2.atributos()

# Iniciar el combate entre los personajes
combate(personaje_1, personaje_2)
