from decimal import Decimal, ROUND_HALF_UP
from cli.input_helpers import pedir_numero_positivo
import finanzas_core.intereses as core_int

def menu_interes_simple():
    while True:
        print("\n" + "Menú de intereses simples".center(50, "*"))
        print(" 1. Calcular la cantidad original\n 2. Calcular la nueva cantidad\n 3. Calcular el interés necesario\n 4. Calcular el tiempo necesario\n 5. Calcular valor de los intereses\n 6. Volver al menú anterior\n")
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            nueva = pedir_numero_positivo("Ingresa la nueva cantidad: ")
            interes = pedir_numero_positivo("Ingresa los intereses como decimal (ej. 0.12): ", rango_max=1)
            tiempo = pedir_numero_positivo("Ingresa el tiempo (años): ")
            orig = core_int.calcular_cantidad_original(nueva, interes, tiempo)
            v_int = core_int.calcular_valor_interes(orig, nueva)
            print(f"La cantidad original es: ${orig:,.2f}\nLos intereses equivalen a: ${v_int:,.2f}")
        elif opcion == "6":
            break

def menu_interes_compuesto():
    while True:
        print("\n" + "="*50 + "\nINTERÉS COMPUESTO\n" + "="*50)
        print(" 1. Calcular interés compuesto\n 2. Volver\n")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            orig = pedir_numero_positivo("Cantidad original ($): ")
            interes = pedir_numero_positivo("Tasa decimal (ej. 0.12): ", rango_max=1)
            tiempo = pedir_numero_positivo("Tiempo en años: ")
            periodos = pedir_numero_positivo("Veces al año que se paga: ")
            res = core_int.calcular_cantidad_nueva_compuesta(orig, interes, tiempo, periodos)
            print(f"La nueva cantidad es: ${res:,.2f}")
        elif opcion == "2":
            break

def menu_descuento():
    while True:
        print("\n" + "="*50 + "\nCÁLCULO DE DESCUENTOS\n" + "="*50)
        print(" 1. Calcular Precio con Descuento\n 2. Volver\n")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            orig = pedir_numero_positivo("Cantidad original ($): ")
            desc = pedir_numero_positivo("Porcentaje de descuento (%): ", rango_max=100)
            res = core_int.calcular_descuento(orig, desc)
            print(f"Precio con descuento: ${res:,.2f}")
        elif opcion == "2":
            break

def menu_prestamos():
    while True:
        print("\n" + "="*50 + "\nPRÉSTAMOS\n" + "="*50)
        print(" 1. Pago mensual fijo\n 2. Volver\n")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            p = pedir_numero_positivo("Monto principal ($): ")
            i = pedir_numero_positivo("Tasa anual decimal (ej. 0.12): ", rango_max=1)
            m = pedir_numero_positivo("Plazo en meses: ", es_entero=True)
            pago = core_int.calcular_pago_mensual_prestamo(p, i, m)
            print(f"Pago mensual fijo: ${pago:,.2f}")
        elif opcion == "2":
            break

def menu_retiro():
    while True:
        print("\n" + "="*50 + "\nPLANIFICACIÓN DE RETIRO\n" + "="*50)
        print(" 1. Fondo necesario para retiro\n 2. Volver\n")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            ret = pedir_numero_positivo("Ingreso mensual deseado ($): ")
            rend = pedir_numero_positivo("Rendimiento estimado decimal (ej. 0.04): ", rango_max=0.12)
            res = core_int.calcular_fondo_necesario(ret, rend)
            print(f"Recomendado (Regla 4% / Preciso): ${res['recomendacion']:,.2f}")
        elif opcion == "2":
            break