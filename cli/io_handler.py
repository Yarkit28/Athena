from decimal import Decimal, ROUND_HALF_UP

def mostrar_tabla_amortizacion(tabla, total_intereses, total_pagos):
    if not tabla:
        print("\n No hay datos para mostrar")
        return
    
    print("\n" + "=" * 95)
    print("TABLA DE AMORTIZACIÓN - TARJETA DE CRÉDITO".center(95))
    print("=" * 95)
    print(f"{'Mes':^6} | {'Balance':^14} | {'Interés':^12} | {'Cargo':^12} | {'New Balance':^14} | {'Pago':^14} | {'Balance Final':^14}")
    print("-" * 95)
    
    for row in tabla:
        dbalance = Decimal(str(row['balance'])).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        dinteres = Decimal(str(row['interes'])).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        dcargo = Decimal(str(row['cargo'])).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        dnew = Decimal(str(row['new_balance'])).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        dpago = Decimal(str(row['pago'])).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        dfinal = Decimal(str(row['balance_final'])).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        print(f"{row['mes']:^6} | ${dbalance:>13} | ${dinteres:>11} | ${dcargo:>11} | ${dnew:>13} | ${dpago:>13} | ${dfinal:>13}")
    
    print("-" * 95)
    print(f"Total intereses pagados: ${Decimal(str(total_intereses)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)}")
    print(f"Total pagos realizados:  ${Decimal(str(total_pagos)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)}")
    
    ultimo = tabla[-1]
    if ultimo['balance_final'] <= 0:
        print(f"¡Tarjeta pagada completamente en {ultimo['mes']} meses!")
    else:
        print(f"Balance restante: ${Decimal(str(ultimo['balance_final'])).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)}")
    print("=" * 95)

def guardar_tabla_archivo(tabla, total_intereses, total_pagos):
    try:
        nombre = input("Ingresa el nombre del archivo (sin extensión): ")
        with open(f"{nombre}.txt", "w", encoding="utf-8") as archivo:
            archivo.write("=" * 95 + "\n")
            archivo.write("TABLA DE AMORTIZACIÓN - TARJETA DE CRÉDITO\n")
            archivo.write("=" * 95 + "\n\n")
            archivo.write(f"{'Mes':^6} | {'Balance':^14} | {'Interés':^12} | {'Cargo':^12} | {'New Balance':^14} | {'Pago':^14} | {'Balance Final':^14}\n")
            archivo.write("-" * 95 + "\n")
            
            for row in tabla:
                dbalance = Decimal(str(row['balance'])).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
                dinteres = Decimal(str(row['interes'])).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
                dcargo = Decimal(str(row['cargo'])).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
                dnew = Decimal(str(row['new_balance'])).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
                dpago = Decimal(str(row['pago'])).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
                dfinal = Decimal(str(row['balance_final'])).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
                archivo.write(f"{row['mes']:^6} | ${dbalance:>13} | ${dinteres:>11} | ${dcargo:>11} | ${dnew:>13} | ${dpago:>13} | ${dfinal:>13}\n")
            
            archivo.write("-" * 95 + "\n")
            archivo.write(f"Total intereses pagados: ${Decimal(str(total_intereses)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)}\n")
            archivo.write(f"Total pagos realizados:  ${Decimal(str(total_pagos)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)}\n")
            ultimo = tabla[-1]
            if ultimo['balance_final'] <= 0:
                archivo.write(f" ¡Tarjeta pagada completamente en {ultimo['mes']} meses!\n")
            else:
                archivo.write(f"Balance restante: ${Decimal(str(ultimo['balance_final'])).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)}\n")
        print(f"Archivo '{nombre}.txt' guardado exitosamente")
    except Exception as e:
        print(f"Error al guardar: {e}")