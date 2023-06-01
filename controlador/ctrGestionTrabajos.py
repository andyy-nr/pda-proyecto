from PyQt5.QtWidgets import QMessageBox

from vistas.frmTrabajo import Ui_frmTrabajo
from datos.jobs import Dt_jobs
from entidades.Jobs import jobs
from PyQt5 import QtWidgets

class CtrlGestionTrabajos(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmTrabajo()
        self.ui.setupUi(self)
        self.initControlGui()
        self.ui.tbl_trabajo.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
    dttr = Dt_jobs()

    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.agregarTrabajo)
        self.ui.btn_limpiar.clicked.connect(self.limpiarCampos)
        self.ui.btn_buscar.clicked.connect(lambda: self.cargarDatos(1))
        self.ui.tbl_trabajo.clicked.connect(self.seleccionarElemento)
        self.ui.txt_buscar.textChanged.connect(self.buscarVacio)
        self.cargarDatos(0)

    def buscarVacio(self):
        if self.ui.txt_buscar.text() == "":
            self.cargarDatos(0)

    def limpiarCampos(self):
        self.ui.txt_codigo.setText("")
        self.ui.txt_nombre_trabajo.setText("")
        self.ui.txt_sal_maximo.setText("")
        self.ui.txt_sal_minimo.setText("")
        self.ui.txt_buscar.setText("")
        self.cargarDatos(0)

    def cargarDatos(self, modo):
        if modo == 1:
            texto = self.ui.txt_buscar.text()
            if texto != "":
                self.ui.txt_buscar.clearSelection()
                listaTrabajo = self.dttr.buscarTrabajo(texto)
            else:
                QMessageBox.about(self, "Error", "No se puede buscar con el campo vacio")
                return
        else:
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
        if self.ui.txt_nombre_trabajo.text() == "":
            return False
        if self.ui.txt_sal_maximo.text() == "":
            return False
        if self.ui.txt_sal_minimo.text() == "":
            return False
        return True

    def seleccionarElemento(self):
        try:
            fila = self.ui.tbl_trabajo.selectedIndexes()[0].row()
            trabajos = self.dttr.buscarTrabajo(self.ui.txt_buscar.text())
            trabajo = trabajos[fila]
            self.ui.txt_codigo.setText(str(trabajo._job_id))
            self.ui.txt_nombre_trabajo.setText(trabajo._job_title)
            self.ui.txt_sal_maximo.setText(str(trabajo._max_salary))
            self.ui.txt_sal_minimo.setText(str(trabajo._min_salary))
        except Exception as e:
            print(e)
        except IndexError as e:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Seleccione un elemento de la tabla")

    def agregarTrabajo(self):
        if self.validarVacios():
            nombre_trabajo = self.ui.txt_nombre_trabajo.text()
            salario_maximo = float(self.ui.txt_sal_maximo.text())
            salario_minimo = float(self.ui.txt_sal_minimo.text())
            trabajo = jobs(job_title=nombre_trabajo, min_salary=salario_minimo, max_salary=salario_maximo)
            try:
                self.dttr.agregarTrabajo(trabajo)
                self.cargarDatos(0)
                self.limpiarCampos()
            except Exception as e:
                print(f"Error al agregar el registro: {e}")
        else:
            print("Error: Campos vacios")


