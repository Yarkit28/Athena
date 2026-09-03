from cli.menu_credito import menu_credito
from cli.menu_intereses import (
    menu_interes_simple,
    menu_interes_compuesto,
    menu_descuento,
    menu_prestamos,
    menu_retiro
)

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
            menu_interes_simple()
        elif opcion == "2":
            menu_interes_compuesto()
        elif opcion == "3":
            menu_descuento()
        elif opcion == "4":
            menu_prestamos()
        elif opcion == "5":
            menu_retiro()
        elif opcion == "6":
            menu_credito()
        elif opcion == "7":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción no válida. Por favor, selecciona un número del 1 al 7.")

if __name__ == "__main__":
    menu_principal()