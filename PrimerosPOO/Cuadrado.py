'''
Created on 14 ene. 2019

@author: Alvaro Leiva Toledano
'''
class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def __str__(self):
        resultado = ""
        for i in range(self.lado):
            resultado += "#"
          
        resultado +="\n"

        for i in range(1,self.lado-1):
            resultado += "#"
            for espacios in range(self.lado -2):
                resultado += " "
                
            resultado += "#"
            resultado +="\n"

        for i in range(self.lado):
            resultado += "#"
            
        resultado +="\n"
        return resultado


    

cuadrado1 = Cuadrado(9)
print(cuadrado1.__str__())