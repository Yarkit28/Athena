"""
Suite de Pruebas de Aceptación y No-Regresión — Misión 3.2 Athena
Garantiza de forma reproducible:
1. Correcto funcionamiento de la Capa de Aplicación (`finanzas_app`).
2. Subsanación de los errores de interacción en la CLI (`cli/input_helpers.py`).
3. Interoperabilidad limpia sin acoplamiento.
"""

import unittest
from unittest.mock import patch
import sys
import os

# Asegurar path raíz
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from finanzas_app.casos_uso import (
    cu_calcular_pago_mensual_prestamo,
    cu_calcular_cantidad_nueva_compuesta,
    cu_calcular_fondo_necesario,
    cu_calcular_tabla_amortizacion,
)
from finanzas_app.errores import ErrorValidacionEntrada, ErrorCalculoInvalido
from cli.input_helpers import pedir_numero_positivo, pedir_confirmacion


class TestCapaAplicacion(unittest.TestCase):
    """Pruebas unitarias para la capa de aplicación finanzas_app."""

    def test_calculo_prestamo_exitoso(self):
        res = cu_calcular_pago_mensual_prestamo(principal="100000", tasa_anual_decimal="0.10", meses="12")
        self.assertAlmostEqual(res["pago_mensual"], 8791.5887, places=2)
        self.assertIn("total_intereses", res)
        self.assertIn("total_pagar", res)

    def test_prestamo_entrada_invalida(self):
        with self.assertRaises(ErrorValidacionEntrada):
            cu_calcular_pago_mensual_prestamo(principal="-5000", tasa_anual_decimal="0.10", meses="12")

    def test_interes_compuesto_exitoso(self):
        res = cu_calcular_cantidad_nueva_compuesta(cantidad_original="1000", interes="0.05", anios="2", periodos="12")
        self.assertAlmostEqual(res["cantidad_nueva_compuesta"], 1104.9413, places=2)
        self.assertAlmostEqual(res["intereses_ganados"], 104.9413, places=2)

    def test_fondo_retiro_rendimiento_cero(self):
        # Evalúa el manejo seguro en Application
        res = cu_calcular_fondo_necesario(retiro_mensual_deseado="20000", rendimiento_anual="0")
        self.assertIsNotNone(res["fondo_4porciento"])
        self.assertIsNone(res["fondo_preciso"])

    def test_tabla_amortizacion_valida(self):
        res = cu_calcular_tabla_amortizacion(
            balance_inicial="10000",
            tasa_anual="12",
            cargo_recurrente="0",
            pago_fijo="1000",
            meses_mostrar="12"
        )
        self.assertTrue(len(res["tabla"]) > 0)
        self.assertIn("total_intereses", res)


class TestCLINoRegresion(unittest.TestCase):
    """Pruebas para verificar que la CLI no se rompe y los helpers reintentan ante errores."""

    @patch('builtins.input', side_effect=["-50", "abc", "100"])
    @patch('builtins.print')
    def test_pedir_numero_positivo_reintento_interactivo(self, mock_print, mock_input):
        """
        Verifica que ante entradas inválidas (-50 y 'abc'), el helper NO retorna False
        sino que insiste en el bucle hasta recibir '100'.
        """
        resultado = pedir_numero_positivo("Ingrese un número: ", permitir_cero=False)
        self.assertEqual(resultado, 100.0)
        self.assertEqual(mock_input.call_count, 3)

    @patch('builtins.input', side_effect=["x", "s"])
    @patch('builtins.print')
    def test_pedir_confirmacion_valida(self, mock_print, mock_input):
        resultado = pedir_confirmacion("¿Desea continuar?")
        self.assertTrue(resultado)
        self.assertEqual(mock_input.call_count, 2)


if __name__ == "__main__":
    unittest.main()