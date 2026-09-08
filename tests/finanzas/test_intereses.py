import unittest
from finanzas_core.intereses import (
    calcular_cantidad_original,
    calcular_cantidad_nueva,
    calcular_valor_interes,
    calcular_interes,
    calcular_tiempo,
    calcular_cantidad_nueva_compuesta,
    calcular_descuento
)

class TestIntereses(unittest.TestCase):
    # --- INTERÉS SIMPLE ---
    def test_calcular_cantidad_original(self):
        self.assertAlmostEqual(calcular_cantidad_original(1100, 0.10, 1), 1000.0)
        # Caso límite: División por cero si 1 + (interes * tiempo) == 0
        with self.assertRaises(ZeroDivisionError):
            calcular_cantidad_original(1000, -1.0, 1)

    def test_calcular_cantidad_nueva(self):
        self.assertAlmostEqual(calcular_cantidad_nueva(1000, 0.10, 1), 1100.0)
        self.assertAlmostEqual(calcular_cantidad_nueva(1000, 0, 5), 1000.0)

    def test_calcular_valor_interes(self):
        self.assertEqual(calcular_valor_interes(1000, 1100), 100.0)
        self.assertEqual(calcular_valor_interes(1000, 1000), 0.0)

    def test_calcular_interes(self):
        self.assertAlmostEqual(calcular_interes(1000, 1100, 1), 0.10)
        # Casos límite: División por cero
        with self.assertRaises(ZeroDivisionError):
            calcular_interes(0, 1100, 1)
        with self.assertRaises(ZeroDivisionError):
            calcular_interes(1000, 1100, 0)

    def test_calcular_tiempo(self):
        self.assertAlmostEqual(calcular_tiempo(1000, 1100, 0.10), 1.0)
        with self.assertRaises(ZeroDivisionError):
            calcular_tiempo(1000, 1100, 0)

    # --- INTERÉS COMPUESTO ---
    def test_calcular_cantidad_nueva_compuesta(self):
        # 1000 al 12% anual compuesto mensualmente por 1 año
        resultado = calcular_cantidad_nueva_compuesta(1000, 0.12, 1, 12)
        self.assertAlmostEqual(resultado, 1126.825, places=3)
        
    # --- DESCUENTOS ---
    def test_calcular_descuento(self):
        self.assertEqual(calcular_descuento(100, 20), 80.0)
        self.assertEqual(calcular_descuento(100, 0), 100.0)  # 0%
        self.assertEqual(calcular_descuento(100, 100), 0.0)  # 100%

if __name__ == '__main__':
    unittest.main()