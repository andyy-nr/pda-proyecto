from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLineEdit
from vistas.frmInicioSesion import Ui_MainWindow
from controlador.ctrInicio import CtrlFrmMainWindow


class CtrlInicioSesion(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.CtrlMW = CtrlFrmMainWindow()
        self.initControlGui()

    def initControlGui(self):
        self.ui.btn_iniciar_sesion.clicked.connect(self.validarCredenciales)
        self.ui.check_mostrar_contrasena.stateChanged.connect(self.mostrarContrasenia)

    def validarCredenciales(self):
        user = self.ui.txt_usuario.text()
        pwd = self.ui.txt_contrasena.text()

        if user == "anunez" and pwd == "112358!":
            self.openMainWindow()
        else:
            alert = QMessageBox.information(self, 'Alerta', "Usuario y/o clave incorrectos", QMessageBox.Ok)

    def mostrarContrasenia(self):
        if self.ui.check_mostrar_contrasena.isChecked():
            self.ui.txt_contrasena.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.txt_contrasena.setEchoMode(QLineEdit.Password)

    def openMainWindow(self):
        self.CtrlMW.show()
        self.close()