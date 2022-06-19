# Primero: clase Mamifero - Clase padre
class Mamifero():

    # Creando constructor.
    def __init__(self, mamas, vida):
        self.__cant_mamas = mamas # Encapsulando atributo.
        self.esperanza_vida = vida
    
    def mamantar(self):
        print("Estoy dando lechita.")
    
    def nacer(self):
        print("Estoy dando a luz.")
    
    # Generando métodos de acceso para el método encapsulado.

    # Mandando valor del atributo cant_mamas
    def get_cant_mamas(self):
        return self.__cant_mamas
    
    # Modificndo valor del atributo cant_mamas
    def set_cant_mamas(self, cant_mamas):
        self.__cant_mamas = cant_mamas

# Segundo: clase AnimalMarino - Clase hija
class AnimalMarino():

    # Creando constructor
    def __init__(self, branqueas, especie):
        self.tiene_branqueas = branqueas
        self.especie = especie
    
    def nadar(self):
        print("Estoy nadando.")
    
    def comer(self):
        print("Estoy comiendo.")

# Tercero: clase Cetaceo   
class Cetaceo(Mamifero, AnimalMarino): # Heredando atributos y métodos de las clases padres.

    # Creando constructor.
    def __init__(self,  mamas, vida, branqueas, 
                 especie, notas, lugar_vive, peso): # Debo de solicitar todos los datos de las clases padres.
      
        Mamifero.__init__(self, mamas, vida) # Pasando los datos correspondiente a la clase Mamifero.
        AnimalMarino.__init__(self, branqueas, especie) # Pasando los datos correspondiente a la clase AnimalMarino
        
        # Atributos solo de la clase Cetaceo
        self.notas = notas
        self.vive_en = lugar_vive
        self.peso = peso
    
    # Sobre escribiendo métodos de las clases padres
    def nacer(self):
        print("El cetaceo está dando a luz.")
    
    def nadar(self):
        print("El cetaceo está nadando.")

# Primer cetaceo
delfin = Cetaceo(2, "25 - 40 años", False, "Delfín común", None, "Aguas tropicales", "70 - 110kg")
delfin.mamantar() # Método de la clase padre Mamifero.
delfin.nadar()
delfin.comer() # Método de la clase padre AnimalMarino.
delfin.esperanza_vida # Atributo de la clase padre Mamifero.

# cant = delfin.__cant_mamas # Error porque está encapsulado, entonces no existe, hay que llamar el método.
cant = delfin.get_cant_mamas()
print(cant)

# Segundo cetaceo
orca = Cetaceo(3, "10 - 45 años", False, "Orca", "Delfinidos más grandes.", "Oceano", "2600 - 9000kg")
print(orca.notas)
print(orca.especie)
mamarias = orca.get_cant_mamas()
print(f"Inicial: {mamarias}")
orca.set_cant_mamas(2)
mamarias = orca.get_cant_mamas()
print(f"Final: {mamarias}")
orca.mamantar()
orca.nacer()


