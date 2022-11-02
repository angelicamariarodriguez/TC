
from PyQt5.QtWidgets import QDialog, QWidget, QPushButton, QHBoxLayout, QGroupBox, QGridLayout, QLabel, QLineEdit, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5 import QtCore

class Ventana_Cancion(QWidget):

    def __init__(self, app):
        super().__init__()
        self.interfaz = app
        #Se establecen las características de la ventana
        self.title = 'Mi música - canción'
        self.left = 80
        self.top = 80
        self.width = 500
        self.height = 150
        #Inicializamos la ventana principal
        self.inicializar_ventana()

    def inicializar_ventana(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.distr_cancion = QHBoxLayout()
        self.setLayout(self.distr_cancion)
        
        self.caja_datos = QGroupBox()
        layout_datos = QGridLayout()
        self.caja_datos.setLayout(layout_datos)

        datos = ["Canción", "Duración", "Intérpretes", "Compositor"]
        for i in range(len(datos)):
            etiqueta = QLabel(datos[i])
            etiqueta.setFont(QFont("Times",weight=QFont.Bold))
            etiqueta.setAlignment(QtCore.Qt.AlignCenter)
            layout_datos.addWidget(etiqueta,i,0)

        self.texto_cancion = QLineEdit()
        layout_datos.addWidget(self.texto_cancion, 0, 1)

        self.texto_duracion = QLineEdit()
        layout_datos.addWidget(self.texto_duracion, 1, 1)

        self.texto_interpretes = QLineEdit()
        self.texto_interpretes.setReadOnly(True)
        layout_datos.addWidget(self.texto_interpretes, 2, 1)

        self.texto_compositor = QLineEdit()
        layout_datos.addWidget(self.texto_compositor, 3, 1)

        self.caja_botones = QGroupBox()
        layout_botones = QVBoxLayout()
        self.caja_botones.setLayout(layout_botones)

        self.boton_guardar = QPushButton("Guardar datos editados")
        self.boton_guardar.clicked.connect(lambda: self.interfaz.guardar_cancion(self.cancion_actual, {"Titulo":self.texto_cancion.text(), "Intérpretes":self.texto_interpretes.text(), "Duracion":self.texto_duracion.text(),"Compositor":self.texto_compositor.text()}))
        layout_botones.addWidget(self.boton_guardar)

        self.boton_borrar = QPushButton("Borrar")
        self.boton_borrar.clicked.connect(lambda: self.interfaz.eliminar_cancion(self.cancion_actual))
        layout_botones.addWidget(self.boton_borrar)

        self.boton_adicionar = QPushButton("Adicionar Intérprete")
        #self.boton_adicionar.clicked.connect()
        layout_botones.addWidget(self.boton_adicionar)

        self.boton_lista_canciones = QPushButton("Ver lista de canciones")
        self.boton_lista_canciones.clicked.connect(self.ver_canciones)
        layout_botones.addWidget(self.boton_lista_canciones)

        self.distr_cancion.addWidget(self.caja_datos)
        self.distr_cancion.addWidget(self.caja_botones)
        
    def mostrar_cancion(self, n_cancion, cancion):
        self.cancion_actual = n_cancion
        self.texto_cancion.setText(cancion["Titulo"])
        self.texto_interpretes.setText(cancion["Intérpretes"])
        self.texto_duracion.setText(cancion["Duracion"])
        self.texto_compositor.setText(cancion["Compositor"])

    def ver_canciones(self):
        self.interfaz.mostrar_ventana_lista_canciones()
        self.hide()
