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
            for rol in listaRol:
                self.ui.cbox_rol.addItem(str(rol._rol), int(rol._id_rol))
        except Exception as e:
            print(e)
        try:
            listaOpcion = self.do.listaOpciones()
            for opcion in listaOpcion:
                self.ui.cbox_opcion.addItem(str(opcion._opcion), int(opcion._id_opcion))
        except Exception as e:
            print(e)

    def agregarRolOpcion(self):
        rol = self.ui.cbox_rol.currentData()
        opcion = self.ui.cbox_opcion.currentData()
        self.dro.agregarRolOpcion(rol, opcion)
        self.cargarDatos()

