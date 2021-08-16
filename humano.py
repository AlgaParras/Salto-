class humano():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def Aumento_Edad (self):
        Aumento = int(input("¿Cuanto de edad quieres aumentar? :"))
        self.edad += Aumento
        
    def hacerpopo(self):
        print("me hize popo")
    def numero(self):
        print(2)