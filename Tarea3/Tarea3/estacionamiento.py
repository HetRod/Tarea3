'''
Created on 29/1/2015

@author: Gabo
'''
from Tarea3 import Marzullo
from doctest import SKIP

class Estacionamiento(object):
    '''
    classdocs
    '''
    puestos = []

    def __init__(self):
        '''
        Constructor
        '''
        self.puestos = []
        
    def reservar(self, horaInicio, horaFin):
        if (Marzullo.validarHora(horaInicio) and Marzullo.validarHora(horaFin)):
            hI = int(horaInicio)
            hF = int(horaFin)
            if (Marzullo.marzullo_recorrido(self.puestos, (hI,hF))):
                self.puestos.append((hI,hF))
                return True
            return False
        else:
            return False