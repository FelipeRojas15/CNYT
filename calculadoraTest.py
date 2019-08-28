import unittest
import calculadora
import math

class TestCalculadora(unittest.TestCase):
    def test_Suma(self):
        tuplaA,tuplaB = (3,4),(3,5)
        self.assertEqual(calculadora.suma(tuplaA,tuplaB),(6+9j))



if __name__=='_main__':
    unittest.main()
