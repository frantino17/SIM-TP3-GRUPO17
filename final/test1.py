import sys
from main import simular
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QMessageBox, QLabel, QComboBox, QHeaderView
)
from PyQt5.QtCore import QRect


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tablas de Probabilidades")
        self.setGeometry(100, 100, 1200, 600)  # Tamaño de la ventana

        # Tabla 1: Probabilidades de venta de autos
        self.table1 = QTableWidget(5, 1, self)  # 5 filas y 1 columna
        self.table1.setHorizontalHeaderLabels(["Pr. venta de autos"])
        self.table1.setVerticalHeaderLabels(["0", "1", "2", "3", "4"])
        self.table1.setEditTriggers(QTableWidget.AllEditTriggers)  # Permitir edición
        self.table1.setGeometry(QRect(320, 10, 170, 218))  # Posición y tamaño (x, y, ancho, alto)
        self.table1.setColumnWidth(0, 150)

        valores_tabla1 = [0.20, 0.30, 0.30, 0.15, 0.05]
        for fila, valor in enumerate(valores_tabla1):
            self.table1.setItem(fila, 0, QTableWidgetItem(str(valor)))

        # Tabla 2: Tipos de autos y probabilidades
        self.table2 = QTableWidget(3, 1, self)
        self.table2.setHorizontalHeaderLabels(["Probabilidad"])
        self.table2.setVerticalHeaderLabels(["Compacto", "Mediano", "De Lujo"])
        self.table2.setGeometry(QRect(510, 10, 200, 144))  # Posición y tamaño (x, y, ancho, alto)

        probabilidades = [0.50, 0.35, 0.15]
        for fila, probabilidad in enumerate(probabilidades):
            self.table2.setItem(fila, 0, QTableWidgetItem(str(probabilidad)))

        # Tabla 3: Comisiones y probabilidades
        self.table3 = QTableWidget(2, 2, self)
        self.table3.setHorizontalHeaderLabels(["Probabilidad", "Comisión"])
        self.table3.setGeometry(QRect(730, 10, 250, 144))  # Posición y tamaño (x, y, ancho, alto)
        self.table3.setColumnWidth(0, 100)

        comision = [400, 500]
        probabilidades = [0.40, 0.60]
        for fila, probabilidad in enumerate(probabilidades):
            self.table3.setItem(fila, 0, QTableWidgetItem(str(probabilidad)))
        for fila, com in enumerate(comision):
            self.table3.setItem(fila, 1, QTableWidgetItem(str(com)))

        # Tabla 4: Comisiones y probabilidades
        self.table4 = QTableWidget(3, 2, self)
        self.table4.setHorizontalHeaderLabels(["Probabilidad", "Comisión"])
        self.table4.setGeometry(QRect(1000, 10, 250, 144))  # Posición y tamaño (x, y, ancho, alto)
        self.table4.setColumnWidth(0, 100)

        comision = [1000, 1500, 2000]
        probabilidades = [0.35, 0.40, 0.25]
        for fila, probabilidad in enumerate(probabilidades):
            self.table4.setItem(fila, 0, QTableWidgetItem(str(probabilidad)))
        for fila, com in enumerate(comision):
            self.table4.setItem(fila, 1, QTableWidgetItem(str(com)))

        self.label = QLabel("Cantidad de semanas (n):", self)
        self.label.setGeometry(QRect(50, 10, 150, 30))
        self.inputCantidadSimulaciones = QtWidgets.QDoubleSpinBox(self)
        self.inputCantidadSimulaciones.setGeometry(
            QtCore.QRect(200, 10, 100, 25))  # Posición y tamaño (x, y, ancho, alto)
        self.inputCantidadSimulaciones.setDecimals(0)  # No permitir decimales
        self.inputCantidadSimulaciones.setMinimum(100)  # Valor mínimo permitido (1)
        self.inputCantidadSimulaciones.setMaximum(1000000000.0)

        self.label1 = QLabel("Mostar desde fila:", self)
        self.label1.setGeometry(QRect(50, 40, 150, 30))
        self.inputFila = QtWidgets.QDoubleSpinBox(self)
        self.inputFila.setGeometry(QtCore.QRect(200, 40, 100, 25))  # Posición y tamaño (x, y, ancho, alto)
        self.inputFila.setDecimals(0)  # No permitir decimales
        self.inputFila.setMinimum(1.0)  # Valor mínimo permitido (1)
        self.inputFila.setMaximum(1000000000.0)

        self.label2 = QLabel("Filas a mostar:", self)
        self.label2.setGeometry(QRect(50, 70, 150, 30))
        self.inputRangoFilas = QtWidgets.QDoubleSpinBox(self)
        self.inputRangoFilas.setGeometry(QtCore.QRect(200, 70, 100, 25))  # Posición y tamaño (x, y, ancho, alto)
        self.inputRangoFilas.setDecimals(0)  # No permitir decimales
        self.inputRangoFilas.setMinimum(1.0)  # Valor mínimo permitido (1)
        self.inputRangoFilas.setMaximum(1000000000.0)

        self.label3 = QLabel("Umbral de comision (y):", self)
        self.label3.setGeometry(QRect(50, 100, 150, 30))
        self.inputUmbral = QtWidgets.QDoubleSpinBox(self)
        self.inputUmbral.setGeometry(QtCore.QRect(200, 100, 100, 25))  # Posición y tamaño (x, y, ancho, alto)
        self.inputUmbral.setDecimals(0)  # No permitir decimales
        self.inputUmbral.setMinimum(0)  # Valor mínimo permitido (0)
        self.inputUmbral.setMaximum(1000000000.0)

        # Botón "Simular"
        self.simular_button = QPushButton("Simular", self)
        self.simular_button.setGeometry(QRect(1600, 250, 200, 50))  # Posición y tamaño (x, y, ancho, alto)
        self.simular_button.clicked.connect(self.simular)

        headers = [
            'Reloj\n(Sem)', 'RND\nV1', 'Ventas\nV1', 'RND\nV2', 'Ventas\nV2',
            'RND\nV3', 'Ventas\nV3', 'RND\nV4', 'Ventas\nV4',
            'RND\nTipo\nAuto\nventa 1 v1', 'Tipo\nAuto v1', 'RND\nComisión\nv1', 'Comisión\nv1',
            'RND\nTipo\nAuto\nventa 2 v1', 'Tipo\nAuto v2', 'RND\nComisión\nv2', 'Comisión\nv2',
            'RND\nTipo\nAuto\nventa 3 v1', 'Tipo\nAuto v3', 'RND\nComisión\nv3', 'Comisión\nv3',
            'RND\nTipo\nAuto\nventa 4 v1', 'Tipo\nAuto v4', 'RND\nComisión\nv4', 'Comisión\nv4',
            'RND\nTipo\nAuto\nventa 1 v2', 'Tipo\nAuto v1', 'RND\nComisión\nv1', 'Comisión\nv1',
            'RND\nTipo\nAuto\nventa 2 v2', 'Tipo\nAuto v2', 'RND\nComisión\nv2', 'Comisión\nv2',
            'RND\nTipo\nAuto\nventa 3 v2', 'Tipo\nAuto v3', 'RND\nComisión\nv3', 'Comisión\nv3',
            'RND\nTipo\nAuto\nventa 4 v2', 'Tipo\nAuto v4', 'RND\nComisión\nv4', 'Comisión\nv4',
            'RND\nTipo\nAuto\nventa 1 v3', 'Tipo\nAuto v1', 'RND\nComisión\nv1', 'Comisión\nv1',
            'RND\nTipo\nAuto\nventa 2 v3', 'Tipo\nAuto v2', 'RND\nComisión\nv2', 'Comisión\nv2',
            'RND\nTipo\nAuto\nventa 3 v3', 'Tipo\nAuto v3', 'RND\nComisión\nv3', 'Comisión\nv3',
            'RND\nTipo\nAuto\nventa 4 v3', 'Tipo\nAuto v4', 'RND\nComisión\nv4', 'Comisión\nv4',
            'RND\nTipo\nAuto\nventa 1 v4', 'Tipo\nAuto v1', 'RND\nComisión\nv1', 'Comisión\nv1',
            'RND\nTipo\nAuto\nventa 2 v4', 'Tipo\nAuto v2', 'RND\nComisión\nv2', 'Comisión\nv2',
            'RND\nTipo\nAuto\nventa 3 v4', 'Tipo\nAuto v3', 'RND\nComisión\nv3', 'Comisión\nv3',
            'RND\nTipo\nAuto\nventa 4 v4', 'Tipo\nAuto v4', 'RND\nComisión\nv4', 'Comisión\nv4',
            'Comision\nTotal\nSemana V1', 'Comision\nTotal\nSemana V2', 'Comision\nTotal\nSemana V3',
            'Comision\nTotal\nSemana V4',
            'Comision\npromedio\nv1', 'Comision\npromedio\nv2', 'Comision\npromedio\nv3', 'Comision\npromedio\nv4',
            'Contador\nSupera\nUmbral v1', 'Contador\nSupera\nUmbral v2', 'Contador\nSupera\nUmbral v3',
            'Contador\nSupera\nUmbral v4',
        ]
        self.tableRes = QTableWidget(0, len(headers), self)
        self.tableRes.setHorizontalHeaderLabels(headers)
        self.tableRes.setGeometry(QRect(0, 300, 2400, 690))  # Posición y tamaño (x, y, ancho, alto)
        self.tableRes.setColumnWidth(0, 40)
        self.tableRes.setColumnWidth(1, 20)
        self.tableRes.setColumnWidth(2, 50)
        self.tableRes.setColumnWidth(3, 20)
        self.tableRes.setColumnWidth(4, 50)
        self.tableRes.setColumnWidth(5, 20)
        self.tableRes.setColumnWidth(6, 50)
        self.tableRes.setColumnWidth(7, 20)
        self.tableRes.setColumnWidth(8, 50)
        self.tableRes.setColumnWidth(8, 50)

        self.tableRes.setColumnWidth(9, 90)
        self.tableRes.setColumnWidth(10, 80)
        self.tableRes.setColumnWidth(11, 70)
        self.tableRes.setColumnWidth(12, 70)
        self.tableRes.setColumnWidth(13, 90)
        self.tableRes.setColumnWidth(14, 80)
        self.tableRes.setColumnWidth(15, 70)
        self.tableRes.setColumnWidth(16, 70)
        self.tableRes.setColumnWidth(17, 90)
        self.tableRes.setColumnWidth(18, 80)
        self.tableRes.setColumnWidth(19, 70)
        self.tableRes.setColumnWidth(20, 70)
        self.tableRes.setColumnWidth(21, 90)
        self.tableRes.setColumnWidth(22, 80)
        self.tableRes.setColumnWidth(23, 70)
        self.tableRes.setColumnWidth(24, 70)

        self.tableRes.setColumnWidth(25, 90)
        self.tableRes.setColumnWidth(26, 80)
        self.tableRes.setColumnWidth(27, 70)
        self.tableRes.setColumnWidth(28, 70)
        self.tableRes.setColumnWidth(29, 90)
        self.tableRes.setColumnWidth(30, 80)
        self.tableRes.setColumnWidth(31, 70)
        self.tableRes.setColumnWidth(32, 70)
        self.tableRes.setColumnWidth(33, 90)
        self.tableRes.setColumnWidth(34, 80)
        self.tableRes.setColumnWidth(35, 70)
        self.tableRes.setColumnWidth(36, 70)
        self.tableRes.setColumnWidth(37, 90)
        self.tableRes.setColumnWidth(38, 80)
        self.tableRes.setColumnWidth(39, 70)
        self.tableRes.setColumnWidth(40, 70)

        self.tableRes.setColumnWidth(41, 90)
        self.tableRes.setColumnWidth(42, 80)
        self.tableRes.setColumnWidth(43, 70)
        self.tableRes.setColumnWidth(44, 70)
        self.tableRes.setColumnWidth(45, 90)
        self.tableRes.setColumnWidth(46, 80)
        self.tableRes.setColumnWidth(47, 70)
        self.tableRes.setColumnWidth(48, 70)
        self.tableRes.setColumnWidth(49, 90)
        self.tableRes.setColumnWidth(50, 80)
        self.tableRes.setColumnWidth(51, 70)
        self.tableRes.setColumnWidth(52, 70)
        self.tableRes.setColumnWidth(53, 90)
        self.tableRes.setColumnWidth(54, 80)
        self.tableRes.setColumnWidth(55, 70)
        self.tableRes.setColumnWidth(56, 70)

        self.tableRes.setColumnWidth(57, 90)
        self.tableRes.setColumnWidth(58, 80)
        self.tableRes.setColumnWidth(59, 70)
        self.tableRes.setColumnWidth(60, 70)
        self.tableRes.setColumnWidth(61, 90)
        self.tableRes.setColumnWidth(62, 80)
        self.tableRes.setColumnWidth(63, 70)
        self.tableRes.setColumnWidth(64, 70)
        self.tableRes.setColumnWidth(65, 90)
        self.tableRes.setColumnWidth(66, 80)
        self.tableRes.setColumnWidth(67, 70)
        self.tableRes.setColumnWidth(68, 70)
        self.tableRes.setColumnWidth(69, 90)
        self.tableRes.setColumnWidth(70, 80)
        self.tableRes.setColumnWidth(71, 70)
        self.tableRes.setColumnWidth(72, 70)

        self.tableRes.setColumnWidth(73, 90)
        self.tableRes.setColumnWidth(74, 90)
        self.tableRes.setColumnWidth(75, 90)
        self.tableRes.setColumnWidth(76, 90)
        self.tableRes.setColumnWidth(77, 90)
        self.tableRes.setColumnWidth(78, 90)
        self.tableRes.setColumnWidth(79, 90)
        self.tableRes.setColumnWidth(80, 90)

        self.label_pv1 = QLabel("Prob que V1 tenga comision mayor a y:", self)
        self.label_pv1.setGeometry(QRect(1270, 10, 200, 30))
        self.label_pv2 = QLabel("Prob que V2 tenga comision mayor a y:", self)
        self.label_pv2.setGeometry(QRect(1270, 40, 200, 30))
        self.label_pv3 = QLabel("Prob que V3 tenga comision mayor a y:", self)
        self.label_pv3.setGeometry(QRect(1270, 70, 200, 30))
        self.label_pv4 = QLabel("Prob que V4 tenga comision mayor a y:", self)
        self.label_pv4.setGeometry(QRect(1270, 100, 200, 30))

        self.label_pv1 = QLabel("", self)
        self.label_pv1.setGeometry(QRect(1470, 10, 200, 30))
        self.label_pv2 = QLabel("", self)
        self.label_pv2.setGeometry(QRect(1470, 40, 200, 30))
        self.label_pv3 = QLabel("", self)
        self.label_pv3.setGeometry(QRect(1470, 70, 200, 30))
        self.label_pv4 = QLabel("", self)
        self.label_pv4.setGeometry(QRect(1470, 100, 200, 30))

        self.label_cpv1 = QLabel("Comision promedio V1:", self)
        self.label_cpv1.setGeometry(QRect(1670, 10, 200, 30))
        self.label_cpv2 = QLabel("Comision promedio V2", self)
        self.label_cpv2.setGeometry(QRect(1670, 40, 200, 30))
        self.label_cpv3 = QLabel("Comision promedio V3", self)
        self.label_cpv3.setGeometry(QRect(1670, 70, 200, 30))
        self.label_cpv4 = QLabel("Comision promedio V4", self)
        self.label_cpv4.setGeometry(QRect(1670, 100, 200, 30))

        self.label_cpv1 = QLabel("", self)
        self.label_cpv1.setGeometry(QRect(1870, 10, 200, 30))
        self.label_cpv2 = QLabel("", self)
        self.label_cpv2.setGeometry(QRect(1870, 40, 200, 30))
        self.label_cpv3 = QLabel("", self)
        self.label_cpv3.setGeometry(QRect(1870, 70, 200, 30))
        self.label_cpv4 = QLabel("", self)
        self.label_cpv4.setGeometry(QRect(1870, 100, 200, 30))

    def simular(self):
        # Validar tabla 1
        if not self.validar_probabilidades(self.table1, 0, 1):
            self.mostrar_error("Tabla 1: Las probabilidades deben ser no negativas y sumar 1.")
            return

        # Validar tabla 2
        if not self.validar_probabilidades(self.table2, 0, 1):
            self.mostrar_error("Tabla 2: Las probabilidades deben ser no negativas y sumar 1.")
            return

        # Validar tabla 3
        if not self.validar_probabilidades(self.table3, 0, 1) or not self.validar_no_negativas(self.table3, 1):
            self.mostrar_error(
                "Tabla 3: Las probabilidades deben ser no negativas y sumar 1. Las comisiones no pueden ser negativas.")
            return

        # Validar tabla 4
        if not self.validar_probabilidades(self.table4, 0, 1) or not self.validar_no_negativas(self.table4, 1):
            self.mostrar_error(
                "Tabla 4: Las probabilidades deben ser no negativas y sumar 1. Las comisiones no pueden ser negativas.")
            return
        
         # Obtener parámetros
        cant_semanas = int(self.inputCantidadSimulaciones.value())
        mostrar_desde = int(self.inputFila.value()) - 1  # Ajuste índice base 0
        filas_a_mostrar = int(self.inputRangoFilas.value())
        
        # Validar rangos de filas
        if mostrar_desde < 0 or mostrar_desde >= cant_semanas:
            self.mostrar_error(f"Fila inicial debe estar entre 1 y {cant_semanas}")
            return
            
        if filas_a_mostrar <=0 or (mostrar_desde + filas_a_mostrar) > cant_semanas:
            self.mostrar_error(f"Rango excede cantidad de semanas ({cant_semanas})")
            return

        # Si todas las validaciones pasan
        self.mostrar_exito("Todas las validaciones se completaron con éxito.")
        vec = simular(self)

        self.cargar_tabla(self.tableRes, vec)
        cant_semanas = int(self.inputCantidadSimulaciones.value())

        porcV1 = vec[0][20][0] / cant_semanas * 100
        porcV2 = vec[0][20][1] / cant_semanas * 100
        porcV3 = vec[0][20][2] / cant_semanas * 100
        porcV4 = vec[0][20][3] / cant_semanas * 100

        self.label_pv1.setText(f"{porcV1:.2f}%")
        self.label_pv2.setText(f"{porcV2:.2f}%")
        self.label_pv3.setText(f"{porcV3:.2f}%")
        self.label_pv4.setText(f"{porcV4:.2f}%")

        cpV1 = vec[0][19][0]
        cpV2 = vec[0][19][1]
        cpV3 = vec[0][19][2]
        cpV4 = vec[0][19][3]

        self.label_cpv1.setText(f"{cpV1:.2f}")
        self.label_cpv2.setText(f"{cpV2:.2f}")
        self.label_cpv3.setText(f"{cpV3:.2f}")
        self.label_cpv4.setText(f"{cpV4:.2f}")

    def validar_probabilidades(self, table, columna, suma_esperada):
        """Validar que las probabilidades no sean negativas y sumen un valor esperado."""
        suma = 0
        for fila in range(table.rowCount()):
            try:
                valor = float(table.item(fila, columna).text())
                if valor < 0:
                    return False
                suma += valor
            except (ValueError, AttributeError):
                return False
        return abs(suma - suma_esperada) < 1e-6

    def validar_no_negativas(self, table, columna):
        """Validar que los valores de una columna sean no negativos."""
        for fila in range(table.rowCount()):
            try:
                valor = float(table.item(fila, columna).text())
                if valor < 0:
                    return False
            except (ValueError, AttributeError):
                return False
        return True

    def mostrar_error(self, mensaje):
        """Mostrar un mensaje de error."""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        msg.setText(mensaje)
        msg.exec_()

    def mostrar_exito(self, mensaje):
        """Mostrar un mensaje de éxito."""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Éxito")
        msg.setText(mensaje)
        msg.exec_()

    def flatten(self, nested_list):
        flat_list = []
        for item in nested_list:
            if isinstance(item, list):
                flat_list.extend(self.flatten(item))
            else:
                flat_list.append(item)
        return flat_list

    def cargar_tabla(self, table, vector):
        table.setRowCount(len(vector))  # Configurar el número de filas
        for fila_idx, fila in enumerate(vector):
            fila_aux = self.flatten(fila)
            for col_idx, valor in enumerate(fila_aux):
                table.setItem(fila_idx, col_idx, QTableWidgetItem(str(valor)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
