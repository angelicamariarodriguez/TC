 
from PyQt5.QtWidgets import QDialog, QWidget, QPushButton, QHBoxLayout, QGroupBox, QGridLayout, QLabel, QLineEdit, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5 import QtCore
        
class Ventana_Lista_Interpretes(QWidget):

    def __init__(self, app):
        super().__init__()
        self.interfaz = app
        #Se establecen las características de la ventana
        self.title = 'Mi música - intérpretes'
        self.left = 80
        self.top = 80
        self.width = 500
        self.height = 150
        #Inicializamos la ventana principal
        self.inicializar_ventana()

    def inicializar_ventana(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.distr_lista_interpretes = QVBoxLayout()
        self.setLayout(self.distr_lista_interpretes)
        
        self.caja_titulos = QGroupBox()
        layout_titulos = QGridLayout()
        self.caja_titulos.setLayout(layout_titulos)


        layout_titulos.addWidget(self.crear_etiqueta("Intérpretes", bold=True),0,0)
        layout_titulos.addWidget(self.crear_etiqueta("Acciones", bold=True),0,1)

        self.caja_interpretes = QGroupBox()
        layout_interpretes = QGridLayout()
        self.caja_interpretes.setLayout(layout_interpretes)

        self.boton_nuevo = QPushButton("Nuevo")
        self.boton_nuevo.clicked.connect(self.mostrar_dialogo_nuevo_interprete)
        
        self.distr_lista_interpretes.addWidget(self.caja_titulos)
        self.distr_lista_interpretes.addWidget(self.caja_interpretes)
        self.distr_lista_interpretes.addWidget(self.boton_nuevo)

    def crear_etiqueta(self, texto, bold=False):
        etiqueta = QLabel(texto)
        if bold:
            etiqueta.setFont(QFont("Times",weight=QFont.Bold))
            etiqueta.setAlignment(QtCore.Qt.AlignCenter)
        return etiqueta

    def crear_campo_texto(self, texto, edit=True):
        campo = QLineEdit(texto)
        if not edit:
            campo.setReadOnly(True)
        return campo

    def limpiar_interpretes(self):
        while self.caja_interpretes.layout().count():
            child = self.caja_interpretes.layout().takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def mostrar_interpretes(self, interpretes):
        self.limpiar_interpretes()
        self.botones = []
        for i in range(len(interpretes)):
            self.caja_interpretes.layout().addWidget(self.crear_campo_texto(interpretes[i], edit=False),i+1,0)
            self.botones.append(QPushButton("Ver"))
            self.botones[i].clicked.connect(lambda estado, x=i: self.ver_interprete(x))
            self.caja_interpretes.layout().addWidget(self.botones[i],i+1,3)

    def ver_interprete(self, n_interprete):
        self.interfaz.mostrar_ventana_interprete(n_interprete)
        self.hide()

    def mostrar_dialogo_nuevo_interprete(self):
        self.dialogo_nuevo_interprete = QDialog(self)

        layout = QGridLayout()
        self.dialogo_nuevo_interprete.setLayout(layout)

        lab1 = QLabel("Nombre")
        txt1 = QLineEdit()
        layout.addWidget(lab1,0,0)
        layout.addWidget(txt1,0,1)
        
        butAceptar = QPushButton("Aceptar")
        butCancelar = QPushButton("Cancelar")

        layout.addWidget(butAceptar,4,0)
        layout.addWidget(butCancelar,4,1)

        butAceptar.clicked.connect(lambda: self.crear_interprete(txt1.text()))
        butCancelar.clicked.connect(lambda: self.dialogo_nuevo_interprete.close())

        self.dialogo_nuevo_interprete.setWindowTitle("Añadir nuevo interprete")
        self.dialogo_nuevo_interprete.exec_()

    def crear_interprete(self, nuevo_interprete):
        self.interfaz.crear_interprete(nuevo_interprete)
        self.dialogo_nuevo_interprete.close()
