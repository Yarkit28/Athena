from cli.input_helpers import pedir_numero_positivo, pedir_confirmacion
from cli.io_handler import mostrar_tabla_amortizacion, guardar_tabla_archivo
from finanzas_core.credito import calcular_tabla_amortizacion

def menu_credito():
    while True:
        print("\n" + "=" * 50)
        print("SISTEMA DE AMORTIZACIÓN DE CRÉDITO".center(50))
        print("=" * 50)
        print(" 1. Calcular tabla de amortización")
        print(" 2. Volver al menú principal\n")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            balance = pedir_numero_positivo("Ingresa el balance inicial ($): ")
            tasa = pedir_numero_positivo("Ingresa la tasa anual (%): ", rango_max=100)
            cargo = pedir_numero_positivo("Ingresa cargo recurrente ($) [0 si no aplica]: ", permitir_cero=True)
            
            print("\n 1. Pago fijo (mismo monto cada mes)")
            print(" 2. Pago porcentual (porcentaje del New Balance)")
            tipo_pago = input("Selecciona tipo de pago (1 o 2): ").strip()
            
            pago_fijo = None
            pago_porcentaje = None
            if tipo_pago == "1":
                pago_fijo = pedir_numero_positivo("Ingresa el pago fijo mensual ($): ")
            elif tipo_pago == "2":
                pago_porcentaje = pedir_numero_positivo("Ingresa el porcentaje a pagar (%): ", rango_max=100)
            else:
                print("❌ Opción inválida. Regresando al submenú...")
                continue

            meses = pedir_numero_positivo("Ingresa cuántos meses mostrar: ", es_entero=True)

            if pedir_confirmacion("\n¿Deseas continuar con el cálculo?"):
                tabla, total_int, total_pag = calcular_tabla_amortizacion(
                    balance_inicial=balance,
                    tasa_anual=tasa,
                    cargo_recurrente=cargo,
                    pago_fijo=pago_fijo,
                    pago_porcentaje=pago_porcentaje,
                    meses_mostrar=meses
                )
                mostrar_tabla_amortizacion(tabla, total_int, total_pag)
                if pedir_confirmacion("\n¿Deseas guardar los resultados en un archivo?"):
                    guardar_tabla_archivo(tabla, total_int, total_pag)
        elif opcion == "2":
            break
        else:
            print("❌ Opción no válida. Seleccione 1 o 2.")