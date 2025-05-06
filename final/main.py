from funciones import GeneradorAleatorio


def simular(self):
    # Obtener valores de las tablas
    valores_tabla1 = [self.table1.item(fila, 0).text() for fila in range(self.table1.rowCount())]
    valores_tabla2 = [self.table2.item(fila, 0).text() for fila in range(self.table2.rowCount())]
    valores_tabla3 = [(self.table3.item(fila, 0).text(), self.table3.item(fila, 1).text()) for fila in
                      range(self.table3.rowCount())]
    valores_tabla4 = [(self.table4.item(fila, 0).text(), self.table4.item(fila, 1).text()) for fila in
                      range(self.table4.rowCount())]
    cantidad_semanas = self.inputCantidadSimulaciones.value()
    fila_inicial = self.inputFila.value()
    numero_filas = self.inputRangoFilas.value()
    umbral = float(self.inputUmbral.value())

    mensaje = (
        f"Tabla 1 (Pr. venta de autos): {valores_tabla1}\n"
        f"Tabla 2 (Tipos de autos y probabilidades): {valores_tabla2}\n"
        f"Tabla 3 (Comisiones y probabilidades): {valores_tabla3}\n"
        f"Tabla 4 (Comisiones y probabilidades): {valores_tabla4}\n"
        f"Cantidad de semanas (n): {cantidad_semanas}\n"
        f"Filia inicial: {fila_inicial}\n"
        f"numero de filas: {numero_filas}"
    )

    print(mensaje)

    aleatorio4 = GeneradorAleatorio(19)
    aleatorio3 = GeneradorAleatorio(20)
    aleatorio2 = GeneradorAleatorio(21)
    aleatorio1 = GeneradorAleatorio(22)

    resultado = []

    for i in range(int(cantidad_semanas)):
        if i == 0:
            resultado.append(simular_semana(valores_tabla1, valores_tabla2, valores_tabla3, valores_tabla4, aleatorio1,
                                            aleatorio2, aleatorio3, aleatorio4, i + 1, ["0", "0", "0", "0"],
                                            [0, 0, 0, 0], umbral))
        else:
            resultado.append(simular_semana(valores_tabla1, valores_tabla2, valores_tabla3, valores_tabla4, aleatorio1,
                                            aleatorio2, aleatorio3, aleatorio4, i + 1, resultado[-1][19],
                                            resultado[-1][20], umbral))

    print(resultado)

    return mostrar_rango(int(fila_inicial), int(numero_filas), resultado)


def sumar_comisiones(v1, v2, v3, v4):
    v1 = 0 if (v1 == "-") else float(v1)
    v2 = 0 if (v2 == "-") else float(v2)
    v3 = 0 if (v3 == "-") else float(v3)
    v4 = 0 if (v4 == "-") else float(v4)
    return str(v1 + v2 + v3 + v4)


def contador_umbral(comisiones, contadores, umbral):
    contador1 = contadores[0] if (float(comisiones[0]) <= umbral) else contadores[0] + 1
    contador2 = contadores[1] if (float(comisiones[1]) <= umbral) else contadores[1] + 1
    contador3 = contadores[2] if (float(comisiones[2]) <= umbral) else contadores[2] + 1
    contador4 = contadores[3] if (float(comisiones[3]) <= umbral) else contadores[3] + 1
    contadores = [contador1, contador2, contador3, contador4]
    return contadores


def promedio_ventas_por_semana(ventaSA, ventasS, index):  # SA Semana Anterior S Semana Actual
    comisiones = [(float(ventaSA[i]) * (index - 1) + float(ventasS[i])) / index for i in range(4)]
    return comisiones


def simular_semana(t1, t2, t3, t4, a1, a2, a3, a4, index, comisionesAnt, contadoresAnt, umbral):
    rnd_ventas_v1 = a1.generar_aleatorio()
    ventas_v1 = get_ventas_from_table(t1, rnd_ventas_v1)

    rnd_ventas_v2 = a1.generar_aleatorio()
    ventas_v2 = get_ventas_from_table(t1, rnd_ventas_v2)

    rnd_ventas_v3 = a1.generar_aleatorio()
    ventas_v3 = get_ventas_from_table(t1, rnd_ventas_v3)

    rnd_ventas_v4 = a1.generar_aleatorio()
    ventas_v4 = get_ventas_from_table(t1, rnd_ventas_v4)

    ventas_all = [ventas_v1, ventas_v2, ventas_v3, ventas_v4]

    resultado = [index,
                 [rnd_ventas_v1, ventas_v1, rnd_ventas_v2, ventas_v2, rnd_ventas_v3, ventas_v3, rnd_ventas_v4,
                  ventas_v4]]

    for i in range(len(ventas_all)):
        for j in range(ventas_all[i]):
            obtener_venta(t2, t3, t4, a2, a3, a4)

    for i in range(4):
        for j in range(4):
            if j < ventas_all[i]:
                resultado += [obtener_venta(t2, t3, t4, a2, a3, a4)]
            else:
                resultado += [["-", "-", "-", "-"]]

    comision_semana_v1 = sumar_comisiones(resultado[2][3], resultado[3][3], resultado[4][3], resultado[5][3])
    comision_semana_v2 = sumar_comisiones(resultado[6][3], resultado[7][3], resultado[8][3], resultado[9][3])
    comision_semana_v3 = sumar_comisiones(resultado[10][3], resultado[11][3], resultado[12][3], resultado[13][3])
    comision_semana_v4 = sumar_comisiones(resultado[14][3], resultado[15][3], resultado[16][3], resultado[17][3])

    comisiones = [comision_semana_v1, comision_semana_v2, comision_semana_v3, comision_semana_v4]
    resultado += [comisiones]
    if index == 1:
        comisiones_acumulado = comisiones
    else:
        comisiones_acumulado = promedio_ventas_por_semana(comisionesAnt, comisiones, index)
    resultado += [comisiones_acumulado]

    supera_umbral = contador_umbral(comisiones, contadoresAnt, umbral)
    resultado += [supera_umbral]

    return resultado


def obtener_venta(t2, t3, t4, a2, a3, a4):
    rnd_tipo_auto = a2.generar_aleatorio()
    tipo_auto = get_tipo_auto(t2, rnd_tipo_auto)
    if tipo_auto == 0:
        return [rnd_tipo_auto, "compacto", "-", 250]
    elif tipo_auto == 1:
        rnd_comision_auto = a3.generar_aleatorio()
        return [rnd_tipo_auto, "mediano", rnd_comision_auto, get_comision_auto(t3, rnd_comision_auto)]
    elif tipo_auto == 2:
        rnd_comision_auto = a4.generar_aleatorio()
        return [rnd_tipo_auto, "de lujo", rnd_comision_auto, get_comision_auto(t4, rnd_comision_auto)]
    else:
        Exception("Tipo de auto no válido")


def get_ventas_from_table(tablaVentas, rnd):
    valor_inicial = 0.0
    for i in range(len(tablaVentas)):
        valor_inicial += float(tablaVentas[i])
        if rnd < float(valor_inicial):
            return i


def get_tipo_auto(tablaAutos, rnd):
    valor_inicial = 0.0
    for i in range(len(tablaAutos)):
        valor_inicial += float(tablaAutos[i])
        if rnd < float(valor_inicial):
            return i


def get_comision_auto(tablaComisiones, rnd):
    valor_inicial = 0.0
    for i in range(len(tablaComisiones)):
        valor_inicial += float(tablaComisiones[i][0])
        if rnd < float(valor_inicial):
            return tablaComisiones[i][1]
    return 0


def mostrar_rango(inicial, numero_filas, resultado):
    filas = resultado[inicial - 1:inicial - 1 + numero_filas]
    ultima_fila = resultado[-1]  # Obtener la última fila
    filas.insert(0, ultima_fila)  # Insertar la última fila como la primera
    for i in range(len(filas)):
        print(filas[i])
    return filas

if __name__ == '__main__':
    print("Simulación iniciada")
# aleatorio4 = GeneradorAleatorio(19)
# aleatorio3 = GeneradorAleatorio(20)
# aleatorio2 = GeneradorAleatorio(21)
# aleatorio1 = GeneradorAleatorio(22)
#
# resultado = []
#
# for i in range(100000):
#     resultado.append(simular_semana(['0.2', '0.3', '0.3', '0.15', '0.05'], ['0.5', '0.35', '0.15'],
#                                     [('0.4', '400'), ('0.6', '500')],
#                                     [('0.35', '1000'), ('0.4', '1500'), ('0.25', '2000')], aleatorio1, aleatorio2,
#                                     aleatorio3,
#                                     aleatorio4,i+1))
# # print("final")
# print(resultado)

# mostrar_rango(22, 68, resultado)
