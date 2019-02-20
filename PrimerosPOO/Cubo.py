'''
Created on 14 ene. 2019

@author: Alvaro Leiva Toledano
'''


class Cubo:
    
    # constructor
    def __init__(self, capacidad, contenido):
        self.capacidad = capacidad
        self.contenido = contenido
        
    # getters
    def getCapacidad(self):
        return self.capacidad

    def getContenido(self):
        return self.contenido
    
    # setters
    def setCapacidad(self, capacidad):
        self.capacidad = capacidad

    def setContenido(self, contenido):
        self.contenido = contenido
    
    def vacia(self):
        self.contenido = 0
        print("Cubo vaciado.")
        # print (contenido)
  
    def llena(self):
        self.contenido = self.capacidad
        print("Cubo llenado.")
        # print (contenido)
  
    def pinta(self):
        for nivel in range(self.capacidad, 0, -1):
            if self.contenido >= nivel:
                print("#~~~~~~#")
            else:
                print("#      #")
        print("########")

    def vuelcaEn(self, otroCubo):
        libre = otroCubo.capacidad - otroCubo.contenido
        if libre > 0:
            if self.contenido > libre:
                print ("¡Se va a desbordar el agua!")
            else:
                otroCubo.contenido += self.contenido
                self.contenido = 0
                print("Cubo volcado correctamente.")


cubo1 = Cubo(10, 5)
cubo2 = Cubo(5, 0)

print("cubo 1:")
cubo1.pinta()
print("cubo 2:")
cubo2.pinta()
cubo1.vuelcaEn(cubo2)
print("cubo 1:")
cubo1.pinta()
print("cubo 2:")
cubo2.pinta()
# cuboEstandar.llena()
# cuboEstandar.pinta()
# cuboEstandar.vacia()
# cuboEstandar.pinta()
