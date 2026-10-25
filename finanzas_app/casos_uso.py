"""
Capa de Aplicación - Casos de Uso (Finanzas App)
Coordina y orquesta los casos de uso financieros del sistema Athena.
Realiza validaciones de entrada, manejo de errores de aplicación y transforma resultados.
"""

from finanzas_core import intereses as core_int
from finanzas_core import credito as core_cred
from finanzas_app.errores import ErrorValidacionEntrada, ErrorCalculoInvalido

def _validar_numero(valor, nombre, minimo=None, permitir_cero=True):
    try:
        num = float(valor)
    except (ValueError, TypeError):
        raise ErrorValidacionEntrada(f"El campo '{nombre}' debe ser un valor numérico válido.")
    
    if minimo is not None:
        if permitir_cero and num < minimo:
            raise ErrorValidacionEntrada(f"El campo '{nombre}' debe ser mayor o igual a {minimo}.")
        elif not permitir_cero and num <= minimo:
            raise ErrorValidacionEntrada(f"El campo '{nombre}' debe ser mayor a {minimo}.")
    return num

def _validar_entero(valor, nombre, minimo=1):
    num = _validar_numero(valor, nombre, minimo=minimo, permitir_cero=False)
    if not float(num).is_integer():
        raise ErrorValidacionEntrada(f"El campo '{nombre}' debe ser un número entero.")
    return int(num)

# --- CASOS DE USO: INTERÉS SIMPLE Y COMPUESTO ---

def cu_calcular_cantidad_original(cantidad_nueva, interes, tiempo):
    c_nueva = _validar_numero(cantidad_nueva, "Cantidad Nueva", minimo=0)
    i = _validar_numero(interes, "Tasa de Interés Decimal", minimo=0)
    t = _validar_numero(tiempo, "Tiempo (años)", minimo=0, permitir_cero=False)
    
    try:
        resultado = core_int.calcular_cantidad_original(c_nueva, i, t)
        v_interes = core_int.calcular_valor_interes(resultado, c_nueva)
        return {"cantidad_original": resultado, "valor_interes": v_interes}
    except ZeroDivisionError:
        raise ErrorCalculoInvalido("División por cero en el cálculo de cantidad original.")

def cu_calcular_cantidad_nueva(cantidad_original, interes, tiempo):
    c_orig = _validar_numero(cantidad_original, "Cantidad Original", minimo=0)
    i = _validar_numero(interes, "Tasa de Interés Decimal", minimo=0)
    t = _validar_numero(tiempo, "Tiempo (años)", minimo=0)
    
    resultado = core_int.calcular_cantidad_nueva(c_orig, i, t)
    v_interes = core_int.calcular_valor_interes(c_orig, resultado)
    return {"cantidad_nueva": resultado, "valor_interes": v_interes}

def cu_calcular_valor_interes(cantidad_original, cantidad_nueva):
    c_orig = _validar_numero(cantidad_original, "Cantidad Original", minimo=0)
    c_nueva = _validar_numero(cantidad_nueva, "Cantidad Nueva", minimo=0)
    
    resultado = core_int.calcular_valor_interes(c_orig, c_nueva)
    return {"valor_interes": resultado}

def cu_calcular_interes(cantidad_original, cantidad_nueva, tiempo):
    c_orig = _validar_numero(cantidad_original, "Cantidad Original", minimo=0, permitir_cero=False)
    c_nueva = _validar_numero(cantidad_nueva, "Cantidad Nueva", minimo=0)
    t = _validar_numero(tiempo, "Tiempo (años)", minimo=0, permitir_cero=False)
    
    try:
        resultado = core_int.calcular_interes(c_orig, c_nueva, t)
        return {"tasa_interes": resultado}
    except ZeroDivisionError:
        raise ErrorCalculoInvalido("División por cero: la cantidad original o el tiempo no pueden ser cero.")

def cu_calcular_tiempo(cantidad_original, cantidad_nueva, interes):
    c_orig = _validar_numero(cantidad_original, "Cantidad Original", minimo=0, permitir_cero=False)
    c_nueva = _validar_numero(cantidad_nueva, "Cantidad Nueva", minimo=0)
    i = _validar_numero(interes, "Tasa de Interés Decimal", minimo=0, permitir_cero=False)
    
    try:
        resultado = core_int.calcular_tiempo(c_orig, c_nueva, i)
        return {"tiempo_anios": resultado}
    except ZeroDivisionError:
        raise ErrorCalculoInvalido("División por cero: la cantidad original o la tasa no pueden ser cero.")

def cu_calcular_cantidad_nueva_compuesta(cantidad_original, interes, anios, periodos):
    c_orig = _validar_numero(cantidad_original, "Cantidad Original", minimo=0)
    i = _validar_numero(interes, "Tasa de Interés Decimal", minimo=0)
    a = _validar_numero(anios, "Años", minimo=0, permitir_cero=False)
    p = _validar_entero(periodos, "Periodos por año", minimo=1)
    
    resultado = core_int.calcular_cantidad_nueva_compuesta(c_orig, i, a, p)
    return {"cantidad_nueva_compuesta": resultado, "intereses_ganados": resultado - c_orig}

def cu_calcular_descuento(cantidad_original, descuento_porcentaje):
    c_orig = _validar_numero(cantidad_original, "Precio Original", minimo=0)
    desc = _validar_numero(descuento_porcentaje, "Porcentaje de Descuento", minimo=0)
    if desc > 100:
        raise ErrorValidacionEntrada("El descuento no puede ser superior al 100%.")
    
    resultado = core_int.calcular_descuento(c_orig, desc)
    monto_descuento = c_orig - resultado
    return {"precio_final": resultado, "descuento_monto": monto_descuento}

# --- CASOS DE USO: PRÉSTAMOS ---

def cu_calcular_pago_mensual_prestamo(principal, tasa_anual_decimal, meses):
    p = _validar_numero(principal, "Monto Principal", minimo=0, permitir_cero=False)
    i = _validar_numero(tasa_anual_decimal, "Tasa Anual Decimal", minimo=0)
    m = _validar_entero(meses, "Plazo en meses", minimo=1)
    
    pago = core_int.calcular_pago_mensual_prestamo(p, i, m)
    total_pagar = pago * m
    total_intereses = total_pagar - p
    return {
        "pago_mensual": pago,
        "total_pagar": total_pagar,
        "total_intereses": total_intereses
    }

def cu_simular_pago_extra(principal, tasa_anual_decimal, meses, extra_mensual):
    p = _validar_numero(principal, "Monto Principal", minimo=0, permitir_cero=False)
    i = _validar_numero(tasa_anual_decimal, "Tasa Anual Decimal", minimo=0)
    m = _validar_entero(meses, "Plazo en meses", minimo=1)
    extra = _validar_numero(extra_mensual, "Aporte Extra Mensual", minimo=0)
    
    res = core_int.simular_pago_extra(p, i, m, extra)
    if res is None:
        raise ErrorCalculoInvalido("El pago mensual total es insuficiente para cubrir los intereses del préstamo.")
    return res

# --- CASOS DE USO: RETIRO Y AHORRO ---

def cu_calcular_fondo_necesario(retiro_mensual_deseado, rendimiento_anual):
    ret = _validar_numero(retiro_mensual_deseado, "Retiro Mensual Deseado", minimo=0, permitir_cero=False)
    rend = _validar_numero(rendimiento_anual, "Rendimiento Anual Estimado", minimo=0)
    
    if rend == 0:
        fondo_4porciento = ret * 12 / 0.04
        return {
            "fondo_4porciento": fondo_4porciento,
            "fondo_preciso": None,
            "recomendacion": fondo_4porciento,
            "nota": "Para un rendimiento del 0%, se utiliza la regla base del 4%."
        }
    
    res = core_int.calcular_fondo_necesario(ret, rend)
    return res

def cu_proyectar_fondo_retiro(aporte_mensual, aporte_anual_extra, edad_actual, edad_retiro, rendimiento_anual, inflacion=0.0):
    ap_m = _validar_numero(aporte_mensual, "Aporte Mensual", minimo=0)
    ap_a = _validar_numero(aporte_anual_extra, "Aporte Anual Extra", minimo=0)
    e_act = _validar_entero(edad_actual, "Edad Actual", minimo=0)
    e_ret = _validar_entero(edad_retiro, "Edad de Retiro", minimo=e_act + 1)
    rend = _validar_numero(rendimiento_anual, "Rendimiento Anual", minimo=0)
    inf = _validar_numero(inflacion, "Inflación Anual", minimo=0)
    
    res = core_int.proyectar_fondo_retiro(ap_m, ap_a, e_act, e_ret, rend, inf)
    return res

def cu_calcular_ingreso_mensual_retiro(fondo_total, rendimiento_anual, años_retiro=30):
    f = _validar_numero(fondo_total, "Fondo Acumulado", minimo=0)
    rend = _validar_numero(rendimiento_anual, "Rendimiento Anual", minimo=0)
    a = _validar_entero(años_retiro, "Años de Retiro", minimo=1)
    
    res = core_int.calcular_ingreso_mensual_retiro(f, rend, a)
    return {"ingreso_mensual": res}

def cu_calcular_meta_ahorro(edad_actual, edad_retiro, rendimiento_anual, inflacion, retiro_mensual_deseado, ahorro_actual=0):
    e_act = _validar_entero(edad_actual, "Edad Actual", minimo=0)
    e_ret = _validar_entero(edad_retiro, "Edad de Retiro", minimo=e_act + 1)
    rend = _validar_numero(rendimiento_anual, "Rendimiento Anual", minimo=0)
    inf = _validar_numero(inflacion, "Inflación", minimo=0)
    ret = _validar_numero(retiro_mensual_deseado, "Retiro Mensual Deseado", minimo=0, permitir_cero=False)
    ahorro = _validar_numero(ahorro_actual, "Ahorro Actual", minimo=0)
    
    res = core_int.calcular_meta_ahorro(e_act, e_ret, rend, inf, ret, ahorro)
    return res

def cu_simular_retiro_con_inflacion(aporte_mensual, aporte_anual_extra, edad_actual, edad_retiro, rendimiento_anual, inflacion, retiro_mensual_deseado):
    ap_m = _validar_numero(aporte_mensual, "Aporte Mensual", minimo=0)
    ap_a = _validar_numero(aporte_anual_extra, "Aporte Anual Extra", minimo=0)
    e_act = _validar_entero(edad_actual, "Edad Actual", minimo=0)
    e_ret = _validar_entero(edad_retiro, "Edad de Retiro", minimo=e_act + 1)
    rend = _validar_numero(rendimiento_anual, "Rendimiento Anual", minimo=0)
    inf = _validar_numero(inflacion, "Inflación Anual", minimo=0)
    ret = _validar_numero(retiro_mensual_deseado, "Retiro Mensual Deseado", minimo=0, permitir_cero=False)
    
    res = core_int.simular_retiro_con_inflacion(ap_m, ap_a, e_act, e_ret, rend, inf, ret)
    return res

# --- CASOS DE USO: CRÉDITO Y AMORTIZACIÓN ---

def cu_calcular_tabla_amortizacion(balance_inicial, tasa_anual, cargo_recurrente=0, pago_fijo=None, pago_porcentaje=None, meses_mostrar=12):
    bal = _validar_numero(balance_inicial, "Balance Inicial", minimo=0, permitir_cero=False)
    tasa = _validar_numero(tasa_anual, "Tasa Anual (%)", minimo=0)
    cargo = _validar_numero(cargo_recurrente, "Cargo Recurrente", minimo=0)
    meses = _validar_entero(meses_mostrar, "Meses a mostrar", minimo=1)
    
    pf = None
    if pago_fijo is not None and str(pago_fijo).strip() != "":
        pf = _validar_numero(pago_fijo, "Pago Fijo Mensual", minimo=0)
        
    pp = None
    if pago_porcentaje is not None and str(pago_porcentaje).strip() != "":
        pp = _validar_numero(pago_porcentaje, "Porcentaje de Pago (%)", minimo=0)
        if pp > 100:
            raise ErrorValidacionEntrada("El porcentaje de pago no puede exceder el 100%.")
            
    if pf is None and pp is None:
        raise ErrorValidacionEntrada("Debe especificar un pago fijo o un pago porcentual.")
        
    tabla, total_int, total_pag = core_cred.calcular_tabla_amortizacion(
        balance_inicial=bal,
        tasa_anual=tasa,
        cargo_recurrente=cargo,
        pago_fijo=pf,
        pago_porcentaje=pp,
        meses_mostrar=meses
    )
    
    return {
        "tabla": tabla,
        "total_intereses": total_int,
        "total_pagos": total_pag,
        "deuda_saldada": (len(tabla) > 0 and tabla[-1]["balance_final"] <= 0)
    }