import math

def calcular_cantidad_original(cantidad_nueva, interes, tiempo):
    return cantidad_nueva / (1 + interes * tiempo)

def calcular_cantidad_nueva(cantidad_original,interes, tiempo):
    return cantidad_original * (1 + interes * tiempo)

def calcular_valor_interes(cantidad_original, cantidad_nueva):
    return cantidad_nueva - cantidad_original

def calcular_interes(cantidad_original, cantidad_nueva, tiempo):
    return (cantidad_nueva - cantidad_original) / (cantidad_original * tiempo)

def calcular_tiempo(cantidad_original, cantidad_nueva, interes):
    return (cantidad_nueva - cantidad_original) / (cantidad_original * interes)

def calcular_cantidad_nueva_compuesta(cantidad_original, interes, anios, periodos):
    return cantidad_original * (1 + interes / periodos) ** (anios * periodos)

def calcular_descuento(cantidad_original, descuento):
    return cantidad_original * (1 - (descuento / 100))

def calcular_pago_mensual_prestamo(principal, tasa_anual_decimal, meses):
    if tasa_anual_decimal == 0:
        return principal / meses
    i = tasa_anual_decimal / 12
    return principal * (i * (1 + i) ** meses) / ((1 + i) ** meses - 1)

def simular_pago_extra(principal, tasa_anual_decimal, meses, extra_mensual):
    pago_normal = calcular_pago_mensual_prestamo(principal, tasa_anual_decimal, meses)
    pago_total = pago_normal + extra_mensual
    i = tasa_anual_decimal / 12

    if i > 0 and pago_total <= principal * i:
        return None

    if i == 0:
        nuevos_meses = math.ceil(principal / pago_total)
    else:
        nuevos_meses = math.ceil(-math.log(1 - (i * principal) / pago_total) / math.log(1 + i))

    interes_original = (pago_normal * meses) - principal
    interes_nuevo = (pago_total * nuevos_meses) - principal

    return {
        'pago_normal': pago_normal,
        'pago_total': pago_total,
        'nuevos_meses': nuevos_meses,
        'meses_ahorrados': meses - nuevos_meses,
        'ahorro_interes': interes_original - interes_nuevo
    }

def calcular_fondo_necesario(retiro_mensual_deseado, rendimiento_anual):
    fondo_4porciento = retiro_mensual_deseado * 12 / 0.04
    años_retiro = 30
    tasa_mensual = rendimiento_anual / 12
    fondo_preciso = retiro_mensual_deseado * (1 - (1 + tasa_mensual) ** (-años_retiro * 12)) / tasa_mensual
    return {
        'fondo_4porciento': fondo_4porciento,
        'fondo_preciso': fondo_preciso,
        'recomendacion': max(fondo_4porciento, fondo_preciso)
    }

def proyectar_fondo_retiro(aporte_mensual, aporte_anual_extra, edad_actual, edad_retiro, 
                           rendimiento_anual, inflacion=0.0):
    años_hasta_retiro = edad_retiro - edad_actual
    meses_hasta_retiro = años_hasta_retiro * 12
    
    if inflacion > 0:
        rendimiento_real = (1 + rendimiento_anual) / (1 + inflacion) - 1
        if rendimiento_real < 0:
            rendimiento_real = rendimiento_anual - inflacion
    else:
        rendimiento_real = rendimiento_anual
    
    tasa_mensual = rendimiento_real / 12
    
    if tasa_mensual == 0:
        vf_aportes_mensuales = aporte_mensual * meses_hasta_retiro
    else:
        vf_aportes_mensuales = aporte_mensual * ((1 + tasa_mensual) ** meses_hasta_retiro - 1) / tasa_mensual
    
    vf_aportes_anuales = 0
    if aporte_anual_extra > 0:
        if tasa_mensual == 0:
            vf_aportes_anuales = aporte_anual_extra * años_hasta_retiro
        else:
            tasa_anual = (1 + tasa_mensual) ** 12 - 1
            if tasa_anual == 0:
                vf_aportes_anuales = aporte_anual_extra * años_hasta_retiro
            else:
                vf_aportes_anuales = aporte_anual_extra * ((1 + tasa_anual) ** años_hasta_retiro - 1) / tasa_anual
    
    fondo_total = vf_aportes_mensuales + vf_aportes_anuales
    
    return {
        'fondo_total': fondo_total,
        'aportes_totales': (aporte_mensual * meses_hasta_retiro) + (aporte_anual_extra * años_hasta_retiro),
        'intereses_ganados': fondo_total - ((aporte_mensual * meses_hasta_retiro) + (aporte_anual_extra * años_hasta_retiro)),
        'años_hasta_retiro': años_hasta_retiro,
        'rendimiento_real': rendimiento_real
    }

def calcular_ingreso_mensual_retiro(fondo_total, rendimiento_anual, años_retiro=30):
    tasa_mensual = rendimiento_anual / 12
    if tasa_mensual == 0:
        return fondo_total / (años_retiro * 12)
    return fondo_total * tasa_mensual / (1 - (1 + tasa_mensual) ** (-años_retiro * 12))

def calcular_meta_ahorro(edad_actual, edad_retiro, rendimiento_anual, inflacion, 
                         retiro_mensual_deseado, ahorro_actual=0):
    fondo_necesario = calcular_fondo_necesario(retiro_mensual_deseado, 0.04)['recomendacion']
    fondo_ajustado = fondo_necesario - ahorro_actual
    años = edad_retiro - edad_actual
    meses = años * 12
    
    if inflacion > 0:
        rendimiento_real = (1 + rendimiento_anual) / (1 + inflacion) - 1
        if rendimiento_real < 0:
            rendimiento_real = rendimiento_anual - inflacion
    else:
        rendimiento_real = rendimiento_anual
    
    tasa_mensual = rendimiento_real / 12
    if tasa_mensual == 0:
        aporte_necesario = fondo_ajustado / meses
    else:
        aporte_necesario = fondo_ajustado * tasa_mensual / ((1 + tasa_mensual) ** meses - 1)
    
    return {
        'fondo_necesario': fondo_necesario,
        'aporte_mensual_necesario': max(0, aporte_necesario),
        'aporte_anual_necesario': max(0, aporte_necesario * 12)
    }

def simular_retiro_con_inflacion(aporte_mensual, aporte_anual_extra, edad_actual, edad_retiro,
                                 rendimiento_anual, inflacion, retiro_mensual_deseado):
    proyeccion = proyectar_fondo_retiro(aporte_mensual, aporte_anual_extra, 
                                       edad_actual, edad_retiro, rendimiento_anual, inflacion)
    fondo_total = proyeccion['fondo_total']
    ingreso_nominal = calcular_ingreso_mensual_retiro(fondo_total, rendimiento_anual)
    años_hasta_retiro = edad_retiro - edad_actual
    factor_inflacion = (1 + inflacion) ** años_hasta_retiro
    ingreso_real = ingreso_nominal / factor_inflacion
    porcentaje_meta = (ingreso_real / retiro_mensual_deseado) * 100
    diferencia = ingreso_real - retiro_mensual_deseado
    
    return {
        'fondo_total': fondo_total,
        'ingreso_nominal': ingreso_nominal,
        'ingreso_real': ingreso_real,
        'porcentaje_meta': porcentaje_meta,
        'diferencia': diferencia,
        'aportes_totales': proyeccion['aportes_totales'],
        'intereses_ganados': proyeccion['intereses_ganados'],
        'años_hasta_retiro': años_hasta_retiro
    }