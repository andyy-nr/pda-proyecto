from PyQt5.QtWidgets import QMessageBox

from vistas.frmTrabajo import Ui_frmTrabajo
from datos.jobs import Dt_jobs
from PyQt5 import QtWidgets

class CtrlGestionTrabajos(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmTrabajo()
        self.ui.setupUi(self)
        self.initControlGui()
    dttr = Dt_jobs()

    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.agregarTrabajo)
        self.ui.btn_limpiar.clicked.connect(self.limpiarCampos)
        self.cargarDatos()

    def limpiarCampos(self):
        self.ui.txt_codigo.setText("")
        self.ui.txt_nombre_trabajo.setText("")
        self.ui.txt_sal_maximo.setText("")
        self.ui.txt_sal_minimo.setText("")

    def cargarDatos(self):
        listaTrabajo = self.dttr.listaTrabajos()
        i = len(listaTrabajo)
        self.ui.tbl_trabajo.setRowCount(i)
        tablerow = 0
        for row in listaTrabajo:
            self.ui.tbl_trabajo.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row._job_id)))
            self.ui.tbl_trabajo.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row._job_title))
            self.ui.tbl_trabajo.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row._min_salary)))
            self.ui.tbl_trabajo.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row._max_salary)))
            tablerow = tablerow + 1

    def validarVacios(self):
        if self.ui.txt_codigo.text() == "":
            return False
        if self.ui.txt_nombre_trabajo.text() == "":
            return False
        if self.ui.txt_sal_maximo.text() == "":
            return False
        if self.ui.txt_sal_minimo.text() == "":
            return False
        return True

    def agregarTrabajo(self):
        if self.validarVacios():
            id_trabajo = int(self.ui.txt_codigo.text())
            nombre_trabajo = self.ui.txt_nombre_trabajo.text()
            salario_maximo = float(self.ui.txt_sal_maximo.text())
            salario_minimo = float(self.ui.txt_sal_minimo.text())
            try:
                self.dttr.agregarTrabajo(id_trabajo, nombre_trabajo, salario_maximo, salario_minimo)
                self.cargarDatos()
                self.limpiarCampos()
            except Exception as e:
                print(f"Error al agregar el registro: {e}")
        else:
            print("Error: Campos vacios")


