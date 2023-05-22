from vistas.frmOpcionRol import Ui_frmOpcionRol
from datos.Dt_Tbl_rol import Dt_tbl_rol
from datos.Dt_Tbl_opcion import Dt_tbl_opcion
from datos.Dt_tbl_rolOpcion import Dt_tbl_rolOpcion
from PyQt5 import QtWidgets

class CtrlGestionRolOpcion(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmOpcionRol()
        self.ui.setupUi(self)
        self.initControlGui()
    dro = Dt_tbl_rolOpcion()
    do = Dt_tbl_opcion()
    dr = Dt_tbl_rol()

    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.agregarRolOpcion)
        self.ui.btn_limpiar.clicked.connect(self.limpiarCampos)
        self.cargarDatos()
        self.cargarCombobox()

    def cargarDatos(self):
        listaRolOpcion = self.dro.listaRolOpcion()
        i = len(listaRolOpcion)
        self.ui.tbl_opcionRol.setRowCount(i)
        tablerow = 0
        for row in listaRolOpcion:
            self.ui.tbl_opcionRol.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row._id_rolOpcion)))
            self.ui.tbl_opcionRol.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row._opcion))
            self.ui.tbl_opcionRol.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row._rol))
            tablerow = tablerow + 1

    def cargarCombobox(self):
        try:
            listaRol = self.dr.listaRoles()
            self.ui.cbox_rol.addItem("Rol*")
            for rol in listaRol:
                self.ui.cbox_rol.addItem(str(rol._rol), int(rol._id_rol))
        except Exception as e:
            print(e)
        try:
            listaOpcion = self.do.listaOpciones()
            self.ui.cbox_opcion.addItem("Opcion*")
            for opcion in listaOpcion:
                self.ui.cbox_opcion.addItem(str(opcion._opcion), int(opcion._id_opcion))
        except Exception as e:
            print(e)

    def validarVacio(self):
        if self.ui.cbox_opcion.currentData() is None:
            return False
        if  self.ui.cbox_rol.currentData() is None:
            return False
        return True

    def limpiarCampos(self):
        self.ui.cbox_rol.setCurrentIndex(0)
        self.ui.cbox_opcion.setCurrentIndex(0)

    def validarNoRepetido(self):
        rolOpcion = self.dro.listaRolOpcion()
        for row in rolOpcion:
            if row._rol == self.ui.cbox_rol.currentText() and row._opcion == self.ui.cbox_opcion.currentText():
                return False
        return True

    def agregarRolOpcion(self):
        if self.validarVacio():
            if not self.validarNoRepetido():
                print("Rol y opcion ya existen")
                return
            rol = self.ui.cbox_rol.currentData()
            opcion = self.ui.cbox_opcion.currentData()
            self.dro.agregarRolOpcion(rol, opcion)
            self.cargarDatos()
        else:
            print("Hay campos vacios")


