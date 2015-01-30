import unittest
from Tarea3 import Marzullo
from Tarea3 import estacionamiento


class CasosDePruebaMarzullo(unittest.TestCase):
       
        def testHoraCorrecta(self):
            self.assertEqual(True, Marzullo.validarHora("0600"), 'Correcto')
        
        def testHoraIncorrecta1(self):
            self.assertEqual(False, Marzullo.validarHora("0630"),'hora errada')
              
        def testHoraIncorrecta2(self):
            self.assertEqual(False,Marzullo.validarHora("0630"),'hora errada')
            
        def testHoraIncorrecta3(self):
            self.assertEqual(False,Marzullo.validarHora("0630"),'hora errada')
        
        def testMarzulloCorrecto(self):
            self.assertEqual(True, Marzullo.marzullo_recorrido([(8,12),(11,13),(10,12)], ((12,14))), 'disponible')
        
        def testMarzulloIncorrecto1(self):
            self.assertEqual(False, Marzullo.marzullo_recorrido([(11,15),(11,15),(11,15),(11,15),(11,15),(11,15),(11,15),(11,15),(11,15),(11,15)], ((11,14))), 'no disponible')
        
        def testMarzulloIncorrecto2(self):
            self.assertEqual(False, Marzullo.marzullo_recorrido([(11,15),(11,15),(11,15),(11,15),(11,15),(11,15),(11,15),(11,15),(11,15),(11,15)], ((12,14))), 'no disponible')
        
        def testMarzulloIncorrecto3(self):
            self.assertEqual(True, Marzullo.marzullo_recorrido([(11,15),(11,15),(11,15),(11,15),(11,15),(11,15),(11,15),(11,15),(11,15),(11,15)], ((16,18))), 'no disponible')
        
        def testIntegracion1(self):
            e = estacionamiento.Estacionamiento()
            e.reservar("1100","1500")
            e.reservar("1100","1500")
            e.reservar("1100","1500")
            e.reservar("1100","1500")
            e.reservar("1100","1500")
            e.reservar("1100","1500")
            e.reservar("1100","1500")
            e.reservar("1100","1500")
            e.reservar("1100","1500")
            e.reservar("1100","1500")
            self.assertEqual(True, e.reservar("1600","1800"), 'Estacionamiento full en hora no requerida (puesto disponible)')
        
        def testIntegracion2(self):
            e = estacionamiento.Estacionamiento()
            e.reservar("1100","1500")
            e.reservar("1100","1500")
            e.reservar("1100","1500")
            e.reservar("1100","1500")
            e.reservar("1100","1500")
            e.reservar("1100","1500")
            e.reservar("1100","1500")
            e.reservar("1100","1500")
            e.reservar("1100","1500")
            e.reservar("1100","1500")
            self.assertEqual(False, e.reservar("1300","1800"), 'Estacionamiento full en hora requerida')
        
        def testIntegracion3(self):
            e = estacionamiento.Estacionamiento()
            e.reservar("1100","1500")
            e.reservar("1100","1500")
            e.reservar("1100","1500")
            e.reservar("1100","1500")
            e.reservar("1100","1500")
            e.reservar("1100","1500")
            self.assertEqual(True, e.reservar("1300","1800"), 'Estacionamiento no lleno')
       
if __name__ == '__main__':
    unittest.main()    