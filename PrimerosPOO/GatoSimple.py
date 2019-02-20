'''
Created on 14 ene. 2019

@author: Alvaro Leiva Toledano
'''


class GatoSimple:

    #constructor
    def __init__(self, color, raza, sexo, edad, peso):
        self.color = color
        self.raza = raza
        self.sexo = sexo
        self.edad = edad
        self. peso = peso
  
    #getter sexo
    def get_sexo(self):
        return self.sexo
    
    #hacer que el gato maulle
    def maulla(self):
        print("Miauuuu")
    
    #hacer que el gato ronronee  
    def ronronea(self):
        print("mrrrrrr")
    
    def come(self, comida):
        if comida == ("pescado"):
            print("Hmm, gracias.")
        else:
            print("Lo siento, yo solo como pescado.")
  
    #poner a pelear 2 gatos
    def peleaCon(self, contrincante):
        if self.sexo == 'hembra':
            print("No me gusta pelear.")
        else:
            if(contrincante.get_sexo() == 'hembra'):
                print("No peleo contra gatitas.")
            else:
                print("Ven aquí que te vas a enterar.")
        
# color = input("Dime el color del pelo: ")
# raza = input("Dime la raza: ")
# sexo = input("Dime el sexo: ")


garfield = GatoSimple('naranja', 'exótico', 'macho',0,0)
isa = GatoSimple('negro', 'persa', 'hembra',0,0)

garfield.peleaCon(isa)

# print("Soy Garfield, soy de color", garfield.color, "de raza", garfield.raza, "y soy de sexo", garfield.sexo)
# garfield.maulla()
# garfield.ronronea()
# garfield.come('pescado')
