def analizar_linea(linea):
    nombre = linea[0:20].strip()
    codigo_identificacion = linea[20:30].strip()
    codigo_orden_de_pago = linea[30:40].strip()
    monto_nominal = linea[40:50].strip()
    calculo_comision = linea[50:52].strip()
    calculo_impositivo = linea[52:54].strip()

    return nombre, codigo_identificacion, codigo_orden_de_pago, monto_nominal, calculo_comision, calculo_impositivo

  #R1
def identificador_de_moneda(codigo_orden_de_pago):
    moneda = None
    monedas = ["ARS", "USD", "EUR", "GBP", "JPY"]

    for moneda_actual in monedas:
        if not moneda and moneda_actual in codigo_orden_de_pago:
            moneda = moneda_actual
        elif moneda and moneda_actual in codigo_orden_de_pago and moneda != moneda_actual:
            return

    return moneda

#R2

def es_mayuscula(car):
    return  "A"<=car <= "Z"

def es_numero(car):
    return  "0"<=car <= "9"


def r2(texto):
    resultado_final = False
    contiene_caracter_no_valido = False
    contador_de_caracteres = 0
    contador_de_guiones = 0

    for car in texto:
        contador_de_caracteres += 1
        if car == "-":
            contador_de_guiones += 1
        if not contiene_caracter_no_valido:
            if not es_mayuscula(car) and not es_numero(car) and car != "-":
                contiene_caracter_no_valido = True

    if not contiene_caracter_no_valido and contador_de_caracteres != contador_de_guiones:
        resultado_final = True

    return resultado_final






#R4

def calculo_de_monto_base(monto_nominal, valor_de_comision):

    comision = 0
    monto_base = 0
    monto_fijo = 100

    if valor_de_comision == 1:
        comision = (monto_nominal // 100) * 9
        monto_base = monto_nominal - comision

    if valor_de_comision == 2:
        if monto_nominal < 500000:
            comision = 0

        if  80000 > monto_nominal >= 50000:
            comision = (monto_nominal // 100) * 5

        monto_base = monto_nominal - comision

    if valor_de_comision == 3:
        if monto_nominal > 25000:
            comision = (monto_nominal // 100) * 6
        monto_base = monto_nominal - (comision + monto_fijo)

    if valor_de_comision == 4:
        if monto_nominal <= 100000:
            monto_base = monto_nominal - 500
        if monto_nominal > 100000:
            monto_base = monto_nominal - 1000


    if valor_de_comision == 5:
        if monto_nominal < 500000:
            comision = 0

        if monto_nominal >= 500000:
            comision = (monto_nominal // 100) * 7

        if comision > 50000:
            comision = 50000
        monto_base = monto_nominal - comision

    return  monto_base

def calculo_monto_final(monto_base,  calculo_impositivo ):
    monto_final = 0
    excedente= 0
    impuesto = 0
    if calculo_impositivo == 1:

        if monto_base > 300000:
            excedente = monto_base - 300000
            impuesto = (excedente // 100) * 25
            monto_final = monto_base - impuesto
    if calculo_impositivo == 2:

        if monto_base < 50000:
            monto_final = monto_base - 50

        if monto_base >=50000:
            monto_final = monto_base - 100
    if calculo_impositivo == 3:
        impuesto= ( monto_base // 100) * 3
        monto_final = monto_base - impuesto

    return monto_final


def principal():
    archivo = open("ordenes25.txt")
    lineas = archivo.readlines()
    archivo.close()

    linea_1 = True
    #R1
    cant_minvalida  = 0

    #R2
    cant_binvalido = 0

    #R3
    cant_oper_validas = 0
    #r4
    suma_mf_validas = 0


    for linea in lineas:
        if linea_1:
            linea_1 = False
            continue

        linea = linea.strip()
        if linea == "":
            continue

        valores = analizar_linea(linea)
        # R1

        moneda = identificador_de_moneda(valores[2])
        if not moneda:
            cant_minvalida +=1

        #R2
        if r2(valores[1]) == True:
            cant_binvalido += 1

        #R3

        monto_base = calculo_de_monto_base(int(valores[3]),int(valores[4]))
        if moneda and r2(valores[1]) == True:
            cant_oper_validas += 1
            # R4
            suma_mf_validas += calculo_monto_final(monto_base, int(valores[5]))


    print(' (r1) - Cantidad de ordenes invalidas - moneda no autorizada:', cant_minvalida)
    print(' (r2) - Cantidad de ordenes invalidas - beneficiario mal identificado:', cant_binvalido)
    print(' (r3) - Cantidad de operaciones validas:', cant_oper_validas)
    print(' (r4) - Suma de montos finales de operaciones validas:', suma_mf_validas)
    #print(' (r5) - Cantidad de ordenes para moneda ARS:', cant_ARS)
    #print(' (r6) - Cantidad de ordenes para moneda USD:', cant_USD)
    #print(' (r7) - Cantidad de ordenes para moneda EUR:', cant_EUR)
    #print(' (r8) - Cantidad de ordenes para moneda GBP:', cant_GBP)
    #print(' (r9) - Cantidad de ordenes para moneda JPN:', cant_JPY)
    #print('(r10) - Codigo de la orden de pago con mayor diferencia nominal - final:', cod_my)
    #print('(r11) - Monto nominal de esa misma orden:', mont_nom_my)
    #print('(r12) - Monto final de esa misma orden:', mont_fin_my)
    #print('(r13) - Nombre del primer beneficiario del archivo:', nom_primer_benef)
    #print('(r14) - Cantidad de veces que apareció ese mismo nombre:', cant_nom_primer_benef)
    #print('(r15) - Porcentaje de operaciones inválidas sobre el total:', porcentaje)
    #print('(r16) - Monto final promedio de las ordenes validas en moneda ARS:', promedio)


principal()
