from vistas.frmRegiones import Ui_frmRegiones
from datos.regions import Dt_Regions
from PyQt5 import QtWidgets


class CtrlGestionRegiones(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmRegiones()
        self.ui.setupUi(self)
        self.initControlGui()
    dtu = Dt_Regions()

    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.limpiarCampos)
        self.cargarDatos()

    def limpiarCampos(self):
        self.ui.txt_codigo.setText("")
        self.ui.txt_nombre_region.setText("")


    def cargarDatos(self):
        listaRegiones = self.dtu.listaRegiones()
        i = len(listaRegiones)
        self.ui.tbl_regiones.setRowCount(i)
        tablerow = 0
        for row in listaRegiones:
            self.ui.tbl_regiones.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row._region_id)))
            self.ui.tbl_regiones.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row._region_name))
            tablerow = tablerow + 1