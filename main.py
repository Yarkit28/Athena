from cli import menu_credito as mc
from cli import menu_intereses as mi

def menu_principal():
    while True:
        print("\n" + "=" * 50)
        print("SISTEMA FINANCIERO ATHENA".center(50))
        print("=" * 50)
        print(" 1. Interés Simple")
        print(" 2. Interés Compuesto")
        print(" 3. Descuentos")
        print(" 4. Préstamos")
        print(" 5. Fondos de Retiro")
        print(" 6. Tarjeta de Crédito (Amortización)")
        print(" 7. Salir\n")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            mi.menu_interes_simple()
        elif opcion == "2":
            mi.menu_interes_compuesto()
        elif opcion == "3":
            mi.menu_descuento()
        elif opcion == "4":
            mi.menu_prestamos()
        elif opcion == "5":
            mi.menu_retiro()
        elif opcion == "6":
            mc.menu_credito()
        elif opcion == "7":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción no válida. Por favor, selecciona un número del 1 al 7.")

if __name__ == "__main__":
    menu_principal()