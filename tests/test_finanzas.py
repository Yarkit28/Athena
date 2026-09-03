import unittest
from finanzas_core.intereses import (
    calcular_cantidad_original,
    calcular_cantidad_nueva,
    calcular_pago_mensual_prestamo,
    calcular_descuento
)
from finanzas_core.credito import calcular_tabla_amortizacion

class TestFinanzasCore(unittest.TestCase):

    def test_interes_simple(self):
        self.assertAlmostEqual(calcular_cantidad_nueva(1000, 0.10, 2), 1200.0)
        self.assertAlmostEqual(calcular_cantidad_original(1200, 0.10, 2), 1000.0)

    def test_descuento(self):
        self.assertAlmostEqual(calcular_descuento(100, 15), 85.0)

    def test_pago_prestamo(self):
        pago = calcular_pago_mensual_prestamo(10000, 0.12, 12)
        self.assertAlmostEqual(pago, 888.48788678, places=4)

    def test_amortizacion_credito(self):
        tabla, total_int, total_pag = calcular_tabla_amortizacion(
            balance_inicial=1000,
            tasa_anual=20,
            cargo_recurrente=0,
            pago_fijo=200,
            meses_mostrar=6
        )
        self.assertTrue(len(tabla) > 0)
        self.assertEqual(tabla[0]['mes'], 1)
        self.assertAlmostEqual(tabla[0]['interes'], 16.67, places=2)

if __name__ == '__main__':
    unittest.main()