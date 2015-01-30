import unittest
import Marzullo
import re


class CasosDePruebaMarzullo(unittest.TestCase):
       
        def testHoraCorrecta(self):
            self.assertEqual(True, Marzullo.validarHora("0600"), 'Correcto')
        
        def testHoraIncorrecta1(self):
            self.assertEqual(False, Marzullo.validarHora("0630"),'hora errada')
              
        def testHoraIncorrecta2(self):
            self.assertEqual(False,Marzullo.validarHora("0630"),'hora errada')
            
        def testHoraIncorrecta2(self):
            self.assertEqual(False,Marzullo.marzullo_recorrido("0630"),'hora errada')
        
       
if __name__ == '__main__':
    unittest.main()    