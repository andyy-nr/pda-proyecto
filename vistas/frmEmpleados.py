# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmEmpleados.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from vistas.imagenes import imagenes

class Ui_frmEmpleados(object):
    def setupUi(self, frmEmpleados):
        frmEmpleados.setObjectName("frmEmpleados")
        frmEmpleados.resize(1438, 850)
        frmEmpleados.setMaximumSize(QtCore.QSize(16777215, 2000))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(229, 234, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 189, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(132, 88, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 234, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(73, 77, 95))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(132, 88, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 245, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 232, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(132, 88, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 234, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 189, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(132, 88, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 234, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(73, 77, 95))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(132, 88, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 245, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 232, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(132, 88, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 189, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(73, 77, 95))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(73, 77, 95))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 145, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 245, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 232, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(132, 88, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        frmEmpleados.setPalette(palette)
        self.gridLayout = QtWidgets.QGridLayout(frmEmpleados)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_2 = QtWidgets.QFrame(frmEmpleados)
        self.frame_2.setMinimumSize(QtCore.QSize(150, 60))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.btn_filtrar = QtWidgets.QPushButton(self.frame_2)
        self.btn_filtrar.setGeometry(QtCore.QRect(10, 0, 60, 60))
        self.btn_filtrar.setMinimumSize(QtCore.QSize(60, 0))
        self.btn_filtrar.setMaximumSize(QtCore.QSize(60, 60))
        self.btn_filtrar.setStyleSheet("border-style: outset;\n"
"background-color: :#494D5F;\n"
"")
        self.btn_filtrar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconos/Filtro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_filtrar.setIcon(icon)
        self.btn_filtrar.setIconSize(QtCore.QSize(70, 70))
        self.btn_filtrar.setObjectName("btn_filtrar")
        self.btn_buscar = QtWidgets.QPushButton(self.frame_2)
        self.btn_buscar.setGeometry(QtCore.QRect(80, 0, 60, 60))
        self.btn_buscar.setStyleSheet("border-style: outset;\n"
"background-color: :#494D5F;\n"
"")
        self.btn_buscar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/iconos/Lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_buscar.setIcon(icon1)
        self.btn_buscar.setIconSize(QtCore.QSize(70, 70))
        self.btn_buscar.setObjectName("btn_buscar")
        self.gridLayout.addWidget(self.frame_2, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        self.cbox_departamento = QtWidgets.QComboBox(frmEmpleados)
        self.cbox_departamento.setMinimumSize(QtCore.QSize(400, 40))
        self.cbox_departamento.setObjectName("cbox_departamento")
        self.gridLayout.addWidget(self.cbox_departamento, 3, 6, 1, 4)
        self.t = QtWidgets.QTableView(frmEmpleados)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t.sizePolicy().hasHeightForWidth())
        self.t.setSizePolicy(sizePolicy)
        self.t.setMinimumSize(QtCore.QSize(0, 500))
        self.t.setMaximumSize(QtCore.QSize(16777215, 500))
        self.t.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.t.setObjectName("t")
        self.gridLayout.addWidget(self.t, 6, 0, 1, 10)
        self.txt_apellidos = QtWidgets.QLineEdit(frmEmpleados)
        self.txt_apellidos.setMinimumSize(QtCore.QSize(400, 40))
        self.txt_apellidos.setObjectName("txt_apellidos")
        self.gridLayout.addWidget(self.txt_apellidos, 1, 3, 1, 3)
        self.txt_buscar = QtWidgets.QLineEdit(frmEmpleados)
        self.txt_buscar.setMinimumSize(QtCore.QSize(0, 35))
        self.txt_buscar.setText("")
        self.txt_buscar.setObjectName("txt_buscar")
        self.gridLayout.addWidget(self.txt_buscar, 5, 1, 1, 9)
        self.btn_editar = QtWidgets.QPushButton(frmEmpleados)
        self.btn_editar.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_editar.setFont(font)
        self.btn_editar.setStyleSheet("border-style: outset;\n"
"background-color: #8458B3;\n"
"color: rgb(235, 232, 235);\n"
"\n"
"")
        self.btn_editar.setObjectName("btn_editar")
        self.gridLayout.addWidget(self.btn_editar, 7, 3, 1, 1)
        self.date_fecha_contratacion = QtWidgets.QDateEdit(frmEmpleados)
        self.date_fecha_contratacion.setMinimumSize(QtCore.QSize(400, 40))
        self.date_fecha_contratacion.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 1, 1), QtCore.QTime(0, 0, 0)))
        self.date_fecha_contratacion.setCalendarPopup(True)
        self.date_fecha_contratacion.setObjectName("date_fecha_contratacion")
        self.gridLayout.addWidget(self.date_fecha_contratacion, 2, 3, 1, 3)
        self.frame = QtWidgets.QFrame(frmEmpleados)
        self.frame.setMinimumSize(QtCore.QSize(400, 50))
        self.frame.setMaximumSize(QtCore.QSize(400, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lbl_foto = QtWidgets.QLabel(self.frame)
        self.lbl_foto.setGeometry(QtCore.QRect(350, 0, 50, 50))
        self.lbl_foto.setMinimumSize(QtCore.QSize(50, 50))
        self.lbl_foto.setMaximumSize(QtCore.QSize(50, 50))
        self.lbl_foto.setText("")
        self.lbl_foto.setPixmap(QtGui.QPixmap(":/iconos/JAPI1.png"))
        self.lbl_foto.setScaledContents(True)
        self.lbl_foto.setObjectName("lbl_foto")
        self.lbl_nombre_usuario = QtWidgets.QLabel(self.frame)
        self.lbl_nombre_usuario.setGeometry(QtCore.QRect(120, 10, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_nombre_usuario.setFont(font)
        self.lbl_nombre_usuario.setObjectName("lbl_nombre_usuario")
        self.gridLayout.addWidget(self.frame, 0, 9, 1, 1)
        self.txt_nombres = QtWidgets.QLineEdit(frmEmpleados)
        self.txt_nombres.setMinimumSize(QtCore.QSize(400, 40))
        self.txt_nombres.setObjectName("txt_nombres")
        self.gridLayout.addWidget(self.txt_nombres, 1, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 7, 4, 1, 1)
        self.btn_regresar = QtWidgets.QPushButton(frmEmpleados)
        self.btn_regresar.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_regresar.setMaximumSize(QtCore.QSize(50, 50))
        self.btn_regresar.setStyleSheet("border-style: outset;\n"
"background-color: :#494D5F;\n"
"\n"
"")
        self.btn_regresar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/iconos/Flecha.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_regresar.setIcon(icon2)
        self.btn_regresar.setIconSize(QtCore.QSize(40, 40))
        self.btn_regresar.setObjectName("btn_regresar")
        self.gridLayout.addWidget(self.btn_regresar, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.txt_salario = QtWidgets.QLineEdit(frmEmpleados)
        self.txt_salario.setMinimumSize(QtCore.QSize(400, 40))
        self.txt_salario.setObjectName("txt_salario")
        self.gridLayout.addWidget(self.txt_salario, 3, 0, 1, 3)
        self.btn_eliminar = QtWidgets.QPushButton(frmEmpleados)
        self.btn_eliminar.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_eliminar.setFont(font)
        self.btn_eliminar.setStyleSheet("border-style: outset;\n"
"background-color: #8458B3;\n"
"color: rgb(235, 232, 235);\n"
"")
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.gridLayout.addWidget(self.btn_eliminar, 7, 5, 1, 1)
        self.cbox_trabajo = QtWidgets.QComboBox(frmEmpleados)
        self.cbox_trabajo.setMinimumSize(QtCore.QSize(400, 40))
        self.cbox_trabajo.setObjectName("cbox_trabajo")
        self.gridLayout.addWidget(self.cbox_trabajo, 2, 6, 1, 4)
        self.btn_agregar = QtWidgets.QPushButton(frmEmpleados)
        self.btn_agregar.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_agregar.setFont(font)
        self.btn_agregar.setStyleSheet("border-style: outset;\n"
"background-color: #8458B3;\n"
"color: rgb(235, 232, 235);\n"
"")
        self.btn_agregar.setObjectName("btn_agregar")
        self.gridLayout.addWidget(self.btn_agregar, 7, 1, 1, 1, QtCore.Qt.AlignRight)
        self.txt_telefono = QtWidgets.QLineEdit(frmEmpleados)
        self.txt_telefono.setMinimumSize(QtCore.QSize(400, 40))
        self.txt_telefono.setObjectName("txt_telefono")
        self.gridLayout.addWidget(self.txt_telefono, 2, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 7, 6, 1, 1)
        self.txt_correo = QtWidgets.QLineEdit(frmEmpleados)
        self.txt_correo.setMinimumSize(QtCore.QSize(400, 40))
        self.txt_correo.setObjectName("txt_correo")
        self.gridLayout.addWidget(self.txt_correo, 1, 6, 1, 4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 7, 2, 1, 1)
        self.cbox_gerente = QtWidgets.QComboBox(frmEmpleados)
        self.cbox_gerente.setMinimumSize(QtCore.QSize(400, 40))
        self.cbox_gerente.setObjectName("cbox_gerente")
        self.gridLayout.addWidget(self.cbox_gerente, 3, 3, 1, 3)
        self.btn_limpiar = QtWidgets.QPushButton(frmEmpleados)
        self.btn_limpiar.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_limpiar.setFont(font)
        self.btn_limpiar.setStyleSheet("border-style: outset;\n"
"background-color: #8458B3;\n"
"color: rgb(235, 232, 235);\n"
"")
        self.btn_limpiar.setObjectName("btn_limpiar")
        self.gridLayout.addWidget(self.btn_limpiar, 7, 7, 1, 1)

        self.retranslateUi(frmEmpleados)
        QtCore.QMetaObject.connectSlotsByName(frmEmpleados)

    def retranslateUi(self, frmEmpleados):
        _translate = QtCore.QCoreApplication.translate
        frmEmpleados.setWindowTitle(_translate("frmEmpleados", "Información de empleados"))
        frmEmpleados.setToolTip(_translate("frmEmpleados", "Eliminar información de empleado"))
        self.btn_filtrar.setToolTip(_translate("frmEmpleados", "Filtrar por..."))
        self.btn_buscar.setToolTip(_translate("frmEmpleados", "Buscar"))
        self.cbox_departamento.setPlaceholderText(_translate("frmEmpleados", "Departamento*"))
        self.txt_apellidos.setPlaceholderText(_translate("frmEmpleados", "Apellidos*"))
        self.txt_buscar.setPlaceholderText(_translate("frmEmpleados", "Buscar"))
        self.btn_editar.setToolTip(_translate("frmEmpleados", "Editar información de empleado"))
        self.btn_editar.setText(_translate("frmEmpleados", "Editar"))
        self.lbl_nombre_usuario.setText(_translate("frmEmpleados", "<html><head/><body><p align=\"right\">Nombre de usuario</p></body></html>"))
        self.txt_nombres.setPlaceholderText(_translate("frmEmpleados", "Nombres*"))
        self.txt_salario.setPlaceholderText(_translate("frmEmpleados", "Salario*"))
        self.btn_eliminar.setText(_translate("frmEmpleados", "Eliminar"))
        self.cbox_trabajo.setPlaceholderText(_translate("frmEmpleados", "Trabajo*"))
        self.btn_agregar.setToolTip(_translate("frmEmpleados", "Agregar información de empleado"))
        self.btn_agregar.setText(_translate("frmEmpleados", "Agregar"))
        self.txt_telefono.setPlaceholderText(_translate("frmEmpleados", "Telefono*"))
        self.txt_correo.setPlaceholderText(_translate("frmEmpleados", "Correo Electronico*´"))
        self.cbox_gerente.setPlaceholderText(_translate("frmEmpleados", "Gerente*"))
        self.btn_limpiar.setToolTip(_translate("frmEmpleados", "Limpiar información seleccionada"))
        self.btn_limpiar.setText(_translate("frmEmpleados", "Limpiar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmEmpleados = QtWidgets.QWidget()
    ui = Ui_frmEmpleados()
    ui.setupUi(frmEmpleados)
    frmEmpleados.show()
    sys.exit(app.exec_())