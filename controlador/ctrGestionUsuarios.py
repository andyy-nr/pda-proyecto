from vistas.frmUsuario import Ui_frmUsuario
from datos.Dt_Tbl_user import Dt_tbl_user
from PyQt5 import QtWidgets


class CtrlFrmGestionUser(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmUsuario()
        self.ui.setupUi(self)
        self.initControlGui()
    dtu = Dt_tbl_user()

    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.limpiarCampos)
        self.cargarDatos()

    def limpiarCampos(self):
        self.ui.le_codigo.setText("")
        self.ui.le_nombres.setText("")
        self.ui.le_nombre_usuario.setText("")
        self.ui.le_apellidos.setText("")
        self.ui.le_email.setText("")
        self.ui.le_contrasena.setText("")
        self.ui.le_confirmacion.setText("")

    def cargarDatos(self):
        listUsuario = self.dtu.listUsuarios()
        i = len(listUsuario)
        self.ui.tbl_Usuario.setRowCount(i)
        tablerow = 0
        for row in listUsuario:
            self.ui.tbl_Usuario.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row._id_user)))
            self.ui.tbl_Usuario.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row._user))
            self.ui.tbl_Usuario.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row._pwd))
            self.ui.tbl_Usuario.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row._nombres))
            self.ui.tbl_Usuario.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row._apellidos))
            self.ui.tbl_Usuario.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row._email))
            self.ui.tbl_Usuario.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row._pwd_temp))
            self.ui.tbl_Usuario.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row._estado)))
            tablerow = tablerow + 1