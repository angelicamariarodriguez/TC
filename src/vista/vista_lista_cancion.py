
from PyQt5.QtWidgets import QDialog, QWidget, QPushButton, QHBoxLayout, QGroupBox, QGridLayout, QLabel, QLineEdit, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5 import QtCore

class Ventana_Lista_Canciones(QWidget):

    def __init__(self, app):
        super().__init__()
        self.interfaz = app
        #Se establecen las características de la ventana
        self.title = 'Mi música - canciones'
        self.left = 80
        self.top = 80
        self.width = 500
        self.height = 150
        #Inicializamos la ventana principal
        self.inicializar_ventana()

    def inicializar_ventana(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.distr_album = QVBoxLayout()
        self.setLayout(self.distr_album)

        self.caja_titulos = QGroupBox()
        layout_titulos = QGridLayout()
        self.caja_titulos.setLayout(layout_titulos)

        titulos = ["Título de la canción", "Intérpretes", "Duración", "Acciones"]
        for i in range(len(titulos)):
            etiqueta = QLabel(titulos[i])
            etiqueta.setFont(QFont("Times",weight=QFont.Bold))
            etiqueta.setAlignment(QtCore.Qt.AlignCenter)
            layout_titulos.addWidget(etiqueta,0,i)

        self.caja_canciones = QGroupBox()
        layout_canciones = QGridLayout()
        self.caja_canciones.setLayout(layout_canciones)

        self.boton_nuevo = QPushButton("Nuevo")
        self.boton_nuevo.clicked.connect(self.mostrar_dialogo_nueva_cancion)

        self.distr_album.addWidget(self.caja_titulos)
        self.distr_album.addWidget(self.caja_canciones)
        self.distr_album.addWidget(self.boton_nuevo)

    def crear_campo_texto(self, texto, edit=True):
        campo = QLineEdit(texto)
        if not edit:
            campo.setReadOnly(True)
        return campo

    def limpiar_canciones(self):
        while self.caja_canciones.layout().count():
            child = self.caja_canciones.layout().takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def mostrar_canciones(self, canciones):
        self.limpiar_canciones()
        self.botones = []
        for i in range(len(canciones)):
            texto_titulo = QLineEdit(canciones[i]["Titulo"])
            texto_titulo.setReadOnly(True)
            self.caja_canciones.layout().addWidget(texto_titulo,i+1,0)

            texto_interpretes = QLineEdit(canciones[i]["Intérpretes"])
            texto_interpretes.setReadOnly(True)
            self.caja_canciones.layout().addWidget(texto_interpretes,i+1,1)
            
            texto_duracion = QLineEdit(canciones[i]["Duracion"])
            texto_duracion.setReadOnly(True)
            self.caja_canciones.layout().addWidget(texto_duracion,i+1,2)
            
            self.botones.append(QPushButton("Ver"))
            self.botones[i].clicked.connect(lambda estado, x=i: self.ver_cancion(x))
            self.caja_canciones.layout().addWidget(self.botones[i],i+1,3)

    def limpiar_canciones(self):
        while self.caja_canciones.layout().count():
            child = self.caja_canciones.layout().takeAt(0)
            if child.widget():
                child.widget().deleteLater()
    
    def ver_cancion(self, n_boton):
        self.interfaz.mostrar_ventana_cancion(n_boton)
        self.hide()


    def mostrar_dialogo_nueva_cancion(self):
            self.dialogo_nueva_cancion = QDialog(self)
            
            layout = QGridLayout()
            self.dialogo_nueva_cancion.setLayout(layout)

            lab1 = QLabel("Título")
            txt1 = QLineEdit()
            layout.addWidget(lab1,0,0)
            layout.addWidget(txt1,0,1)

            lab2 = QLabel("Duracion")
            txt2 = QLineEdit()
            layout.addWidget(lab2,1,0)
            layout.addWidget(txt2,1,1)

            lab3 = QLabel("Compositor")
            txt3 = QLineEdit()
            layout.addWidget(lab3,2,0)
            layout.addWidget(txt3,2,1)

            butAceptar = QPushButton("Aceptar")
            butCancelar = QPushButton("Cancelar")
            
            layout.addWidget(butAceptar,4,0)
            layout.addWidget(butCancelar,4,1)
            
            butAceptar.clicked.connect(lambda: self.interfaz.crear_cancion( {"Titulo":txt1.text(),"Interpretes":"", "Minutos":txt2.text().split(":")[0],"Segundos":txt2.text().split(":")[-1],"Compositor":txt3.text()}))
            butCancelar.clicked.connect(lambda: self.dialogo_nueva_cancion.close())

            self.dialogo_nueva_cancion.setWindowTitle("Añadir nuevo album")
            self.dialogo_nueva_cancion.exec_()