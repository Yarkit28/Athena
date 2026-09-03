from decimal import Decimal, ROUND_HALF_UP

def calcular_tabla_amortizacion(balance_inicial, tasa_anual, cargo_recurrente=0,
                                pago_fijo=None, pago_porcentaje=None, meses_mostrar=12):
    tasa_mensual = (tasa_anual / 100) / 12
    balance = balance_inicial
    tabla = []
    total_intereses = 0
    total_pagos = 0
    
    mes = 1
    while mes <= meses_mostrar and balance > 0.005:
        interes = balance * tasa_mensual
        interes_redondeado = Decimal(str(interes)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        interes = float(interes_redondeado)
        
        new_balance = balance + interes + cargo_recurrente
        new_balance_redondeado = Decimal(str(new_balance)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        new_balance = float(new_balance_redondeado)
        
        if pago_fijo is not None:
            pago = min(pago_fijo, new_balance)
        elif pago_porcentaje is not None:
            pago = new_balance * (pago_porcentaje / 100)
        else:
            pago = 0
        
        pago_redondeado = Decimal(str(pago)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        pago = float(pago_redondeado)
        
        balance_final = new_balance - pago
        if balance_final < 0 and balance_final > -0.01:
            balance_final = 0
        balance_final_redondeado = Decimal(str(balance_final)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        balance_final = float(balance_final_redondeado)
        
        tabla.append({
            'mes': mes,
            'balance': balance,
            'interes': interes,
            'cargo': cargo_recurrente,
            'new_balance': new_balance,
            'pago': pago,
            'balance_final': balance_final
        })
        
        total_intereses += interes
        total_pagos += pago
        balance = balance_final
        mes += 1
        
        if balance <= 0:
            break
    
    return tabla, total_intereses, total_pagos