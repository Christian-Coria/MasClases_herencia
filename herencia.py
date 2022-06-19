class Mamifero:
    def __init__(self,cant_mamas,esperanza_vida):
        self._cant_mamas = cant_mamas
        self._esperanza_vida = esperanza_vida
    
    def __str__(self):
        return f"""
        Mamas : {self._cant_mamas} 
        Esperanza de Vida: {self._esperanza_vida}
        """

    @property
    def cant_mamas(self):
        return self._cant_mamas

    @cant_mamas.setter
    def cant_mamas(self,cant_mamas):
        self._cant_mamas = cant_mamas

    def mamar(self):
        print("Tomando Leche")
        
    def nacer(self):
        print("Nacido")
    



class AnimalMarino:
    def __init__(self,especie,branqueas):
        self._especie = especie
        self._branqueas = branqueas
        

    def __str__(self):
        return f"""
        Especie : {self._especie} 
        Branqueas: {self._branqueas}
        """


    def nadar(self):
        return f" Puede nadar"

class Cetaceo(Mamifero,AnimalMarino):
    def __init__(self,notas,vive_en,peso,especie,branqueas,cant_mamas,esperanza_vida):
        AnimalMarino.__init__(self,especie,branqueas)
        Mamifero.__init__(self,cant_mamas,esperanza_vida)
        self._notas = notas
        self._vive_en = vive_en
        self._peso = peso
    
    def __str__(self):
        return super().__str__()

    def nadar(self):
        return AnimalMarino.__str__(self)
       

    def nacer(self):
        return Mamifero.__str__(self)

mam = Mamifero("6","20 años")
anmar = AnimalMarino("delfin","tiene branqueas")
prueba1 = Cetaceo("este es un Cetaceo","vive en agua salada","pesa 32 kg","delfin","posee branqueas","8 mamas","vive 30 años")
print(mam)
mam.mamar()
mam.nacer()
anmar.nadar()
print(anmar)
print(prueba1)
prueba1.nacer()
prueba1.nadar()


