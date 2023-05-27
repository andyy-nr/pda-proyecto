from vistas.frmOpcion import Ui_frmOpcion
from PyQt5 import QtWidgets
from datos.Dt_Tbl_opcion import Dt_tbl_opcion


class CtrlFrmGestionOpcion(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmOpcion()
        self.ui.setupUi(self)
        self.initControlGui()
    dto = Dt_tbl_opcion() # Instancia de la clase Dt_tbl_opcion

    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.agregarOpcion)
        self.ui.btn_regresar.clicked.connect(self.close)
        self.ui.btn_limpiar.clicked.connect(self.limpiarCampos)
        self.ui.btn_buscar.clicked.connect(lambda: self.cargarDatos(1))
        self.cargarDatos(0)

    def limpiarCampos(self):
        self.ui.txt_codigo.setText("")
        self.ui.txt_opcion.setText("")
        self.ui.btn_buscar.setText("")
        self.cargarDatos(0)

    def cargarDatos(self, modo):
        if modo == 1: # Buscar
            texto = self.ui.txt_buscar.text()
            if texto != "":
                listaOpciones = self.dto.buscarOpcion(texto)
            else:
                QtWidgets.QMessageBox.warning(self, "Advertencia", "Ingrese un texto para buscar")
                return
        else: # Cargar todos los datos
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

    def validarNoRepetido(self):
        listaOpciones = self.dto.listaOpciones()
        for row in listaOpciones:
            if self.ui.txt_opcion.text() == row._opcion:
                return False
        return True

    def agregarOpcion(self):
        if self.validarVacios():
            if not self.validarNoRepetido():
                print("Opcion repetida")
                return
            opcion = self.ui.txt_opcion.text()
            estado = 1
            try:
                self.dto.agregarOpcion(opcion, estado)
                self.cargarDatos(0)
                self.limpiarCampos()
            except Exception as e:
                print(f"Error al agregar opcion: {e}")
        else:
            print("Campos vacios")
