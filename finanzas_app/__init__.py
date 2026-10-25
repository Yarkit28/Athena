"""
Módulo de Aplicación para Athena - Finanzas.
Expone los casos de uso y las excepciones personalizadas del sistema.
"""

from .errores import (
    ErrorFinancieroApp,
    ErrorValidacionEntrada,
    ErrorCalculoInvalido,
    ErrorReglaNegocio,
)

from .casos_uso import (
    cu_calcular_cantidad_original,
    cu_calcular_cantidad_nueva,
    cu_calcular_valor_interes,
    cu_calcular_interes,
    cu_calcular_tiempo,
    cu_calcular_cantidad_nueva_compuesta,
    cu_calcular_descuento,
    cu_calcular_pago_mensual_prestamo,
    cu_simular_pago_extra,
    cu_calcular_fondo_necesario,
    cu_proyectar_fondo_retiro,
    cu_calcular_ingreso_mensual_retiro,
    cu_calcular_meta_ahorro,
    cu_simular_retiro_con_inflacion,
    cu_calcular_tabla_amortizacion,
)

__all__ = [
    "ErrorFinancieroApp",
    "ErrorValidacionEntrada",
    "ErrorCalculoInvalido",
    "ErrorReglaNegocio",
    "cu_calcular_cantidad_original",
    "cu_calcular_cantidad_nueva",
    "cu_calcular_valor_interes",
    "cu_calcular_interes",
    "cu_calcular_tiempo",
    "cu_calcular_cantidad_nueva_compuesta",
    "cu_calcular_descuento",
    "cu_calcular_pago_mensual_prestamo",
    "cu_simular_pago_extra",
    "cu_calcular_fondo_necesario",
    "cu_proyectar_fondo_retiro",
    "cu_calcular_ingreso_mensual_retiro",
    "cu_calcular_meta_ahorro",
    "cu_simular_retiro_con_inflacion",
    "cu_calcular_tabla_amortizacion",
]