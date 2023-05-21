from vistas.frmOpcion import Ui_frmOpcion
from PyQt5 import QtWidgets
from datos.Dt_Tbl_opcion import Dt_tbl_opcion


class CtrlFrmGestionOpcion(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmOpcion()
        self.ui.setupUi(self)
        self.initControlGui()
    dto = Dt_tbl_opcion()

    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.agregarOpcion)
        self.cargarDatos()

    def limpiarCampos(self):
        self.ui.txt_codigo.setText("")
        self.ui.txt_opcion.setText("")

    def cargarDatos(self):
        listaOpciones = self.dto.listaOpciones()
        i = len(listaOpciones)
        self.ui.tbl_opcion.setRowCount(i)
        tablerow = 0
        for row in listaOpciones:
            self.ui.tbl_opcion.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row._id_opcion)))
            self.ui.tbl_opcion.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row._opcion))
            tablerow = tablerow + 1

    def validarVacios(self):
        if self.ui.txt_opcion.text() == "":
            return False
        return True

    def agregarOpcion(self):
        if self.validarVacios():
            opcion = self.ui.txt_opcion.text()
            estado = 1
            try:
                self.dto.agregarOpcion(opcion, estado)
                self.cargarDatos()
                self.limpiarCampos()
            except Exception as e:
                print(f"Error al agregar opcion: {e}")
        else:
            print("Campos vacios")
