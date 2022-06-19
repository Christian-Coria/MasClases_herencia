class Persona:
    contador_persona = 0

#variable de clase:
    @classmethod
    def generar_sig_valor(cls): #en vez de self se indica cls (clase)
        Persona.contador_persona +=1
        return Persona.contador_persona

    def __init__(self,nombre,edad):
        self._id_persona = Persona.generar_sig_valor()
        self._nombre = nombre
        self._edad = edad

    def __str__(self):
        return f"Id: {self.contador_persona}, Nombre: {self._nombre} , edad: {self._edad}"


persona1 = Persona("mateo", 20)
persona2 = Persona("silvana" , 39)
print(persona1)
print(persona2)