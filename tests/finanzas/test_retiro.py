import unittest
from finanzas_core.intereses import (
    calcular_fondo_necesario,
    proyectar_fondo_retiro,
    calcular_ingreso_mensual_retiro,
    calcular_meta_ahorro,
    simular_retiro_con_inflacion
)

class TestRetiro(unittest.TestCase):
    def test_calcular_fondo_necesario(self):
        resultado = calcular_fondo_necesario(1000, 0.05)
        self.assertIn('fondo_4porciento', resultado)
        self.assertIn('fondo_preciso', resultado)
        self.assertTrue(resultado['recomendacion'] > 0)
        
        # Caso límite conocido: Rendimiento 0.0 provoca ZeroDivisionError en formula precisa
        with self.assertRaises(ZeroDivisionError):
            calcular_fondo_necesario(1000, 0.0)

    def test_proyectar_fondo_retiro(self):
        # Rendimiento e inflación
        res = proyectar_fondo_retiro(100, 1000, 30, 60, 0.08, 0.03)
        self.assertTrue(res['fondo_total'] > res['aportes_totales'])
        
        # Rendimiento e inflación 0%
        res_cero = proyectar_fondo_retiro(100, 0, 30, 60, 0.0, 0.0)
        self.assertEqual(res_cero['fondo_total'], 36000) # 100 * 360 meses

    def test_calcular_ingreso_mensual_retiro(self):
        # Sin rendimiento
        ingreso_cero = calcular_ingreso_mensual_retiro(360000, 0.0, 30)
        self.assertEqual(ingreso_cero, 1000.0) # 360000 / 360
        
        # Con rendimiento
        ingreso = calcular_ingreso_mensual_retiro(360000, 0.05, 30)
        self.assertTrue(ingreso > 1000.0)

    def test_calcular_meta_ahorro(self):
        res = calcular_meta_ahorro(30, 60, 0.05, 0.02, 2000, 50000)
        self.assertTrue(res['aporte_mensual_necesario'] > 0)

    def test_simular_retiro_con_inflacion(self):
        res = simular_retiro_con_inflacion(500, 0, 30, 60, 0.08, 0.03, 2000)
        self.assertIn('ingreso_real', res)
        self.assertIn('porcentaje_meta', res)

if __name__ == '__main__':
    unittest.main()