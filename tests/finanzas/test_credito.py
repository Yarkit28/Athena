import unittest
from finanzas_core.credito import calcular_tabla_amortizacion

class TestCredito(unittest.TestCase):
    def test_calcular_tabla_amortizacion_pago_fijo(self):
        balance_inicial = 1000
        tabla, intereses, pagos = calcular_tabla_amortizacion(
            balance_inicial, 12, pago_fijo=150, meses_mostrar=12
        )
        self.assertTrue(len(tabla) > 0)
        # Verificar que la deuda termine en 0 (debe pagarse en menos de 12 meses)
        self.assertEqual(tabla[-1]['balance_final'], 0)
        self.assertTrue(intereses > 0)
        self.assertAlmostEqual(pagos, balance_inicial + intereses, places=2)

    def test_calcular_tabla_amortizacion_pago_porcentual(self):
        tabla, _, _ = calcular_tabla_amortizacion(
            1000, 24, pago_porcentaje=10, meses_mostrar=5
        )
        self.assertEqual(len(tabla), 5)
        # El balance debe ir disminuyendo pero no llegar a cero en 5 meses
        self.assertTrue(tabla[-1]['balance_final'] < 1000)
        self.assertTrue(tabla[-1]['balance_final'] > 0)

    def test_calcular_tabla_amortizacion_con_cargo(self):
        tabla, _, _ = calcular_tabla_amortizacion(
            1000, 12, cargo_recurrente=50, pago_fijo=200, meses_mostrar=12
        )
        # El balance al final del primer mes debe incluir el cargo
        # Interes mes 1: 1000 * (0.12/12) = 10
        # New balance: 1000 + 10 + 50 = 1060
        # Pago: 200 -> Balance final: 860
        self.assertEqual(tabla[0]['balance_final'], 860.0)

    def test_calcular_tabla_amortizacion_sin_pago(self):
        # Si no hay pagos, la deuda debe crecer
        tabla, _, _ = calcular_tabla_amortizacion(
            1000, 12, meses_mostrar=3
        )
        self.assertTrue(tabla[-1]['balance_final'] > 1000)

if __name__ == '__main__':
    unittest.main()