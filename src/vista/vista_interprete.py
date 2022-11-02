from PyQt5.QtWidgets import QDialog, QWidget, QPushButton, QHBoxLayout, QGroupBox, QGridLayout, QLabel, QLineEdit, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5 import QtCore

class Ventana_Interprete(QWidget):

    def __init__(self, app):
        super().__init__()
        self.interfaz = app
        #Se establecen las características de la ventana
        self.title = 'Mi música - intérprete'
        self.left = 80
        self.top = 80
        self.width = 500
        self.height = 150
        #Inicializamos la ventana principal
        self.inicializar_ventana()

    def inicializar_ventana(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.distr_interprete = QVBoxLayout()
        self.setLayout(self.distr_interprete)
        
        self.caja_datos = QGroupBox()
        layout_datos = QHBoxLayout()
        self.caja_datos.setLayout(layout_datos)

        etiqueta_interprete = QLabel("Intérprete")
        etiqueta_interprete.setFont(QFont("Times",weight=QFont.Bold))
        layout_datos.addWidget(etiqueta_interprete)
        self.texto_interprete = QLineEdit()
        layout_datos.addWidget(self.texto_interprete)

        self.caja_botones = QGroupBox()
        layout_botones = QHBoxLayout()
        self.caja_botones.setLayout(layout_botones)

        self.boton_guardar = QPushButton("Guardar datos editados")
        self.boton_guardar.clicked.connect(lambda: self.interfaz.guardar_interprete(self.interprete_actual, self.texto_interprete.text()))
        layout_botones.addWidget(self.boton_guardar)

        self.boton_borrar = QPushButton("Borrar")
        self.boton_borrar.clicked.connect(lambda : self.interfaz.eliminar_interprete(self.interprete_actual))
        layout_botones.addWidget(self.boton_borrar)

        self.distr_interprete.addWidget(self.caja_datos)
        self.distr_interprete.addWidget(self.caja_botones)

    def mostrar_interprete(self, n_interprete, interprete):
        self.interprete_actual = n_interprete
        self.texto_interprete.setText(interprete)
