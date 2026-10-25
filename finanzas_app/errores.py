"""
Excepciones personalizadas para la Capa de Aplicación de Finanzas.
Aíslan los errores de dominio y validación de las interfaces de usuario (CLI / GUI).
"""

class ErrorFinancieroApp(Exception):
    """Excepción base para todos los errores de la capa de aplicación."""
    pass

class ErrorValidacionEntrada(ErrorFinancieroApp):
    """Se lanza cuando los datos de entrada provistos por la interfaz son inválidos."""
    pass

class ErrorCalculoInvalido(ErrorFinancieroApp):
    """Se lanza cuando una operación financiera no puede completarse por restricciones matemáticas o de dominio."""
    pass

class ErrorReglaNegocio(ErrorFinancieroApp):
    """Se lanza cuando se viola una regla de negocio del sistema."""
    pass