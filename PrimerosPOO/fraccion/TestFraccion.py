'''
Created on 15 ene. 2019

@author: Alvaro Leiva Toledano
'''
from PrimerosPOO.fraccion.Fraccion import Fraccion

fraccion1 = Fraccion(1, 2)
fraccion2 = Fraccion(3, 4)
print(fraccion1)
print(fraccion2)

fraccion1.calculaMCM(fraccion2)
print(fraccion1)
print(fraccion2)

fraccion1.multiplica(2)
print(fraccion1)

fraccion1.multiplicaFracciones(Fraccion)
print(fraccion1)

fraccion1.resta(fraccion2)
print(fraccion1)

fraccion1.suma(fraccion2)
print(fraccion1)