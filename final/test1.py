import sys
from main import simular
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QMessageBox, QLabel, QComboBox
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
        self.table1.setGeometry(QRect(50, 200, 170, 218))  # Posición y tamaño (x, y, ancho, alto)
        self.table1.setColumnWidth(0, 150)

        valores_tabla1 = [0.20, 0.30, 0.30, 0.15, 0.05]
        for fila, valor in enumerate(valores_tabla1):
            self.table1.setItem(fila, 0, QTableWidgetItem(str(valor)))

        # Tabla 2: Tipos de autos y probabilidades
        self.table2 = QTableWidget(3, 1, self)
        self.table2.setHorizontalHeaderLabels(["Probabilidad"])
        self.table2.setVerticalHeaderLabels(["Compacto", "Mediano", "De Lujo"])
        self.table2.setGeometry(QRect(300, 200, 200, 144))  # Posición y tamaño (x, y, ancho, alto)

        probabilidades = [0.50, 0.35, 0.15]
        for fila, probabilidad in enumerate(probabilidades):
            self.table2.setItem(fila, 0, QTableWidgetItem(str(probabilidad)))

        # Tabla 3: Comisiones y probabilidades
        self.table3 = QTableWidget(2, 2, self)
        self.table3.setHorizontalHeaderLabels(["Probabilidad", "Comisión"])
        self.table3.setGeometry(QRect(550, 200, 250, 144))  # Posición y tamaño (x, y, ancho, alto)
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
        self.table4.setGeometry(QRect(850, 200, 250, 144))  # Posición y tamaño (x, y, ancho, alto)
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
        self.inputCantidadSimulaciones.setGeometry(QtCore.QRect(200, 10, 100, 25))  # Posición y tamaño (x, y, ancho, alto)
        self.inputCantidadSimulaciones.setDecimals(0)  # No permitir decimales
        self.inputCantidadSimulaciones.setMinimum(1.0)  # Valor mínimo permitido (1)
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


        # Botón "Simular"
        self.simular_button = QPushButton("Simular", self)
        self.simular_button.setGeometry(QRect(500, 450, 200, 50))  # Posición y tamaño (x, y, ancho, alto)
        self.simular_button.clicked.connect(self.simular)

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
            self.mostrar_error("Tabla 3: Las probabilidades deben ser no negativas y sumar 1. Las comisiones no pueden ser negativas.")
            return

        # Validar tabla 4
        if not self.validar_probabilidades(self.table4, 0, 1) or not self.validar_no_negativas(self.table4, 1):
            self.mostrar_error("Tabla 4: Las probabilidades deben ser no negativas y sumar 1. Las comisiones no pueden ser negativas.")
            return

        # Si todas las validaciones pasan
        self.mostrar_exito("Todas las validaciones se completaron con éxito.")
        simular(self)

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())