"""
Módulo principal del Núcleo Financiero (Finanzas Core).
Agrupa las funciones puras de cálculo para intereses, préstamos, retiro y crédito.
"""

from .intereses import (
    calcular_cantidad_original,
    calcular_cantidad_nueva,
    calcular_valor_interes,
    calcular_interes,
    calcular_tiempo,
    calcular_cantidad_nueva_compuesta,
    calcular_descuento,
    calcular_pago_mensual_prestamo,
    simular_pago_extra,
    calcular_fondo_necesario,
    proyectar_fondo_retiro,
    calcular_ingreso_mensual_retiro,
    calcular_meta_ahorro,
    simular_retiro_con_inflacion,
)

from .credito import (
    calcular_tabla_amortizacion,
)

__all__ = [
    "calcular_cantidad_original",
    "calcular_cantidad_nueva",
    "calcular_valor_interes",
    "calcular_interes",
    "calcular_tiempo",
    "calcular_cantidad_nueva_compuesta",
    "calcular_descuento",
    "calcular_pago_mensual_prestamo",
    "simular_pago_extra",
    "calcular_fondo_necesario",
    "proyectar_fondo_retiro",
    "calcular_ingreso_mensual_retiro",
    "calcular_meta_ahorro",
    "simular_retiro_con_inflacion",
    "calcular_tabla_amortizacion",
]