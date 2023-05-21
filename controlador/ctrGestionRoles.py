from vistas.frmRoles  import Ui_frmRoles
from datos.Dt_Tbl_rol import Dt_tbl_rol
from PyQt5 import QtWidgets

class CtrlFrmGestionRoles(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmRoles()
        self.ui.setupUi(self)
        self.initControlGui()
    dto = Dt_tbl_rol()

    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.agregarRol)
        self.cargarDatos()

    def limpiarCampos(self):
        self.ui.txt_codigo.setText("")
        self.ui.txt_rol.setText("")

    def cargarDatos(self):
        listaRoles = self.dto.listaRoles()
        i = len(listaRoles)
        self.ui.tbl_roles.setRowCount(i)
        tablerow = 0
        for row in listaRoles:
            self.ui.tbl_roles.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row._id_rol)))
            self.ui.tbl_roles.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row._rol))
            tablerow = tablerow + 1

    def validarVacios(self):
        if self.ui.txt_rol.text() == "":
            return False
        return True

    def agregarRol(self):
        if self.validarVacios():
            rol = self.ui.txt_rol.text()
            estado = 1
            try:
                self.dto.agregarRol(rol, estado)
                self.cargarDatos()
                self.limpiarCampos()
            except Exception as e:
                print(f"Error al agregar rol: {e}")

