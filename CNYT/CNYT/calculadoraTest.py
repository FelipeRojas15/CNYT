import unittest,calculadora,math as m
class TestStringMethods(unittest.TestCase):

    
    def test_sumaVectoresComplejos(self):
        #Ejemplo 1
        self.assertTrue(calculadora.sumaDeVectores([(8,3),(-1,-4),(0,-9)],[(8,-3),(2,5),(3,0)]))



        
 
        
    def test_multiplicacionVectorEscalar(self):
        #Ejemplo 3
        self.assertEqual(calculadora.multiplicacionVectorEscalar([(-2,5),(-1,-1),(2,-9)],(-1,1)),[(-3.0, -7.0), (2.0, 0.0), (7.0, 11.0)])
        
    def test_sumaMatricesComplejas(self):
        #Ejemplo 4
        matrizA = [[(-8,-3),(-6,-4),(0,-4)],[(-1,8),(6,-10),(8,-5)],[(4,0),(8,5),(-7,-9)]]
        matrizB = [[(-7,-2),(-4,-2),(7,7)],[(5,9),(0,3),(6,-5)],[(1,5),(-6,-6),(5,8)]]
        resultado = [[(-15.0, -5.0), (-10.0, -6.0), (7.0, 3.0)], [(4.0, 17.0), (6.0, -7.0), (14.0, -10.0)], [(5.0, 5.0), (2.0, -1.0), (-2.0, -1.0)]]
        self.assertEqual(calculadora.sumaMatrices(matrizA,matrizB),resultado)

        
        
    def test_multiplicacionMatrizEscalar(self):
        #Ejemplo 6
        matrizA=[[(3,-2),(8,-4)],[(4,-10),(-2,-8)]]
        escalar=(-2,3)
        resultado = [[(0,13),(-4,32)],[(22,32),(28,10)]]
        self.assertEqual(calculadora.multiplicacionMatrizEscalar(matrizA,escalar),[[(0.0, 13.0), (-4.0, 32.0)], [(22.0, 32.0), (28.0, 10.0)]])
        
        
    def test_matrizTranspuesta(self):
        #Ejemplo 7
        matriz = [[(5,9),(-7,-5),(-1,-4)],[(8,2),(-3,-7),(7,-8)]]
        self.assertEqual(calculadora.matrizTranspuesta(matriz),[[(5, 9), (8, 2)], [(-7, -5), (-3, -7)], [(-1, -4), (7, -8)]])
        

    def test_matrizConjugada(self):
        #Ejemplo 8
        matriz = [[(-6,1),(3,8)],[(2,-6),(3,0)]]
        self.assertEqual(calculadora.matrizConjugada(matriz),[[(-6.0, -1.0), (3.0, -8.0)], [(2.0, 6.0), (3.0, 0.0)]])
      
    def test_matrizAdjunta(self):
        #Ejemplo 9
        matriz=[[(7,7),(3,8),(8,4)],[(5,0),(8,-6),(-10,-1)]]
        self.assertEqual(calculadora.matrizAdjunta(matriz),[[(7,-7),(5,0)],[(3,-8),(8,6)],[(8,-4),(-10,1)]])
        
        
    def test_productoMatrices(self):
        #Ejemplo 10
        matrizA = [[(-6,2),(0,6),(7,2)],[(6,9),(7,7),(-6,-6)],[(5,8),(-6,8),(6,9)]]
        matrizB = [[(9,-6),(-3,-4),(5,-2)],[(3,6),(-1,-5),(0,-5)],[(9,9),(8,-4),(-8,-4)]]
        self.assertEqual(calculadora.multiplicacionMatrices(matrizA,matrizB),[[(-33.0, 153.0), (120.0, 0.0), (-44.0, -22.0)], [(87.0, 0.0), (-26.0, -117.0), (107.0, 70.0)], [(0.0, 165.0), (147.0, 26.0), (69.0, -36.0)]])

    def test_productoInterno(self):
        #Ejemplo 12
        vector1 = [(2,-1),(-8,-5),(-2,-6)]
        vector2 = [(6,-3),(5,-1),(-6,-2)]
        self.assertEqual(calculadora.productoInternoVectores(vector1,vector2),(-36.0, 11.0))
        
    def test_distanciaVectores(self):
        #Ejemplo 14
        vector1 = [(2,7),(4,-1),(2,-4)]
        vector2 = [(7,8),(2,-8),(1,4)]
        self.assertEqual(calculadora.distanciaEntreVectores(vector1,vector2),12.0)

        vector3 = [(9,-7),(-1,-6)]
        vector4 = [(7,-8),(5,-9)]
        
        self.assertEqual(calculadora.distanciaEntreVectores(vector3,vector4),7.07)

    
    def test_canicas(self):
            #Ejemplo 3.1.3
            m8 = [[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(0,0),(1,0),(0,0),(0,0),(0,0),(1,0)],[(0,0),(0,0),(0,0),(1,0),(0,0),(0,0)],[(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],[(1,0),(0,0),(0,0),(0,0),(1,0),(0,0)]]
            x = calculadora.marbels(m8,[(6,0),(2,0),(1,0),(5,0),(3,0),(10,0)],1)
            self.assertEqual(x,[(0.0, 0.0), (0.0, 0.0), (12.0, 0.0), (5.0, 0.0), (1.0, 0.0), (9.0, 0.0)])
    def test_canicas1(self):
            M = [[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(1,0)], 
                 [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(1,0),(0,0),(0,0)], 
                 [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(1,0),(0,0)],  
                 [(0,0),(0,0),(1,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)], 
                 [(0,0),(0,0),(0,0),(1,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],  
                 [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(1,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)], 
                 [(0,0),(0,0),(0,0),(0,0),(0,0),(1,0),(0,0),(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],
                 [(0,0),(0,0),(0,0),(0,0),(1,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
                 [(0,0),(1,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
                 [(1,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
                 [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(1,0),(0,0),(0,0),(0,0),(0,0)],
                 [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(1,0),(0,0),(0,0),(0,0),(0,0),(0,0)], 
                 [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]]
            V = [(10,0),  
                 (4,0),   
                 (1,0),  
                 (7,0),   
                 (2,0),   
                 (2,0),  
                 (11,0),  
                 (0,0),   
                 (3,0),  
                 (1,0),   
                 (0,0),   
                 (5,0),   
                 (2,0)    
               ]
            x = calculadora.marbels(M,V,25)
            
            self.assertEqual(x,[(0.0, 0.0), (0.0, 0.0), (1.0, 0.0), (7.0, 0.0), (2.0, 0.0), (21.0, 0.0), (5.0, 0.0), (0.0, 0.0), (4.0, 0.0), (0.0, 0.0), (3.0, 0.0), (5.0, 0.0), (0.0, 0.0)])

    def test_ensamble(self):
        MA = [[(0,0),(0.2,0),(0.3,0),(0.5,0)],
              [(0.3,0),(0.2,0),(0.1,0),(0.4,0)],
              [(0.4,0),(0.3,0),(0.2,0),(0.1,0)],
              [(0.3,0),(0.3,0),(0.4,0),(0,0)]]
        VA = [(0.2,0),(0.1,0),(0.6,0),(0.1,0)]
        MB = [[(0,0),(1/6,0),(5/6,0)], 
              [(1/3,0),(1/2,0),(1/6,0)], 
              [(2/3,0),(1/3,0),(0,0)]]
        VB = [(0.7,0),(0.15,0),(0.15,0)]
        x = calculadora.ensamble(MA,VA,MB,VB,5)
        self.assertEqual(x,[(0.06854114583333333, 0.0), (0.08497952546296297, 0.0), (0.09477932870370372, 0.0), (0.06920364583333334, 0.0), (0.08580091435185187, 0.0), (0.09569543981481482, 0.0), (0.06930522916666668, 0.0), (0.08592686064814815, 0.0), (0.0958359101851852, 0.0), (0.06899164583333334, 0.0), (0.08553806990740741, 0.0), (0.09540228425925927, 0.0)])
    def test_doble_rendija(self):
        num_rendijas = 2
        num_blancas_pared = 5
        vector_amplitud = [(1/(22)**0.5,1/(22)**0.5),(-1/(22)**0.5,-1/(22)**0.5),(-1/(22)**0.5,1/(22)**0.5),(-1/(22)**0.5,-1/(22)**0.5),(1/(22)**0.5,-1/(22)**0.5),(-1/(22)**0.5,-1/(22)**0.5),(-1/(22)**0.5,-1/(22)**0.5),(-1/(22)**0.5,-1/(22)**0.5),(1/(22)**0.5,-1/(22)**0.5),(1/(22)**0.5,-1/(22)**0.5),(-1/(22)**0.5,1/(22)**0.5)]
        x = calculadora.doble_rendija(num_rendijas,num_blancas_pared,vector_amplitud)

        print(x)

if __name__ == '__main__':
    unittest.main()