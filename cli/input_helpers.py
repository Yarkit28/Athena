"""
Módulo de ayuda para la captura e interacción con el usuario en la línea de comandos (CLI).
Garantiza un bucle interactivo que insiste hasta obtener datos válidos sin interrumpir el flujo.
"""

def validar_numero(numero):
    """Verifica si una cadena puede convertirse a un número flotante válido."""
    try:
        float(numero)
        return True
    except (ValueError, TypeError):
        return False

def pedir_numero_positivo(mensaje, es_entero=False, rango_min=None, rango_max=None, permitir_cero=False):
    """
    Solicita un número al usuario de forma interactiva en la CLI.
    Reintentará pedir la entrada hasta que cumpla con los criterios especificados.
    Corregido para evitar retornos prematuros (falso o booleano) ante entradas inválidas.
    """
    while True:
        try:
            val_str = input(mensaje).strip()
            if validar_numero(val_str):
                val = float(val_str)
                if not permitir_cero and val <= 0:
                    print("❌ Error, debe ser un número mayor a 0")
                    continue  # Subsanado: sustituye el antiguo 'return False'
                if permitir_cero and val < 0:
                    print("❌ Error, debe ser un número mayor o igual a 0")
                    continue
                if es_entero and not val.is_integer():
                    print("❌ Error, debe ingresar un número entero")
                    continue
                
                val = int(val) if es_entero else val
                if rango_min is not None and val < rango_min:
                    print(f"❌ El valor debe ser mayor o igual a {rango_min}")
                    continue
                if rango_max is not None and val > rango_max:
                    print(f"❌ El valor debe ser menor o igual a {rango_max}")
                    continue
                return val
            print("❌ Debe ingresar un valor numérico válido")
        except Exception:
            print("❌ Error procesando la entrada")

def pedir_confirmacion(mensaje):
    """Solicita una confirmación booleana (s/n) al usuario de manera interactiva."""
    while True:
        resp = input(f"{mensaje} (s/n): ").strip().lower()
        if resp in ['s', 'n']:
            return resp == 's'
        print("❌ Responda 's' o 'n'")