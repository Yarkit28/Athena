import unittest
from finanzas_core.intereses import (
    calcular_pago_mensual_prestamo,
    simular_pago_extra
)

class TestPrestamos(unittest.TestCase):
    def test_calcular_pago_mensual_prestamo(self):
        # Tasa positiva normal
        pago = calcular_pago_mensual_prestamo(10000, 0.12, 12)
        self.assertAlmostEqual(pago, 888.4879, places=4)
        
        # Caso límite: Tasa 0%
        pago_cero = calcular_pago_mensual_prestamo(12000, 0, 12)
        self.assertEqual(pago_cero, 1000.0)

    def test_simular_pago_extra(self):
        # Escenario normal: pago extra suficiente
        resultado = simular_pago_extra(10000, 0.12, 12, 100)
        self.assertIsNotNone(resultado)
        self.assertTrue(resultado['nuevos_meses'] < 12)
        self.assertTrue(resultado['ahorro_interes'] > 0)

        # Caso límite: Tasa 0% con pago extra
        res_tasa_cero = simular_pago_extra(12000, 0, 12, 100) # Normal es 1000, total = 1100
        self.assertEqual(res_tasa_cero['nuevos_meses'], 11)

        # Caso límite: Pago insuficiente para cubrir intereses
        # Interés del mes 1 = 100. Si el pago total <= 100, debe devolver None
        pago_normal = calcular_pago_mensual_prestamo(10000, 0.12, 120)
        pago_extra_negativo_extremo = -(pago_normal - 50) # El total quedará en 50
        resultado_insuficiente = simular_pago_extra(10000, 0.12, 120, pago_extra_negativo_extremo)
        self.assertIsNone(resultado_insuficiente)

if __name__ == '__main__':
    unittest.main()