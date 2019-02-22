'''
Created on 15 ene. 2019

@author: Alvaro Leiva Toledano
'''


class Fraccion:
    
    # constructor
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
        
    # getters
    def getNumerador(self):
        return self.numerador

    def getDenominador(self):
        return self.denominador
    
    # setters
    def setNumerador(self, n):
        self.numerador = n

    def setDenominador(self, d):
        if d == 0:
            print("El denominador no puede ser cero. Lo transformo en 1");
            d = 1
        self.denominador = d
        
    def getReal(self):
        # return (self.numerador / self.denominador)
        return self.getNumerador() / self.getDenominador()
    
    def multiplica(self, x):
        self.numerador = self.getNumerador() * x
        self.denominador = self.getDenominador() * 1
    
    def multiplicaFracciones(self, Fraccion):
        self.numerador = self. numerador * Fraccion.getNumerador()
        self.denominador = self.denominador * Fraccion.getDenominador()
    
    def suma(self, Fraccion):
        if self.denominador != Fraccion.getDenominador():
            print("No pueden sumarse fracciones de diferente denominador.")
        else:
            self.numerador += Fraccion.getNumerador()
    
    def resta(self, Fraccion):
        if self.denominador != Fraccion.getDenominador():
            print("No pueden restarse fracciones de diferente denominador.")
        else:
            self.numerador = Fraccion.getNumerador() - self.numerador
            
    def calculaMCM(self, Fraccion):
        mcm = 0
        min = min(self.denominador, Fraccion.getNumerador());
        for i in range(1, min):
            if self.denominador % i == 0 and Fraccion.getDenominador() % i == 0:
                mcd = i
                mcm = (self.denominador * Fraccion.getDenominador()) / mcd
        print("El mínimo común múltiplo de los denominadores es", mcm)
        print("A continuación, igualaré ambas fracciones al mismo demonimador (mcm)")
        
        '''
        el siguiente cálculo consiste en dividir el mcm por el denominador anterior
        de cada fracción. De esta manera averiguamos el valor por el que se debe
        multiplicar el numerador para que sea equivalente al nuevo denominador(es
        decir, el mcm)
        '''
        nuevoNumerador1 = (mcm / self.denominador) * self.numerador
        nuevoNumerador2 = (mcm / Fraccion.getDenominador()) * Fraccion.getNumerador()
        self.numerador = nuevoNumerador1
        self.denominador = mcm
        Fraccion.setNumerador(nuevoNumerador2)
        Fraccion.setDenominador(mcm)
        
    def __str__(self):
        return str(self.getNumerador()) + "/" + str(self.getDenominador()) + " Resultado = " + str(self.getReal())
