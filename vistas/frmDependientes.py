# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmDependientes.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmDependientes(object):
    def setupUi(self, frmDependientes):
        frmDependientes.setObjectName("frmDependientes")
        frmDependientes.resize(1276, 841)
        frmDependientes.setMaximumSize(QtCore.QSize(16777215, 2000))
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
        frmDependientes.setPalette(palette)
        self.gridLayout = QtWidgets.QGridLayout(frmDependientes)
        self.gridLayout.setObjectName("gridLayout")
        self.txt_buscar = QtWidgets.QLineEdit(frmDependientes)
        self.txt_buscar.setMinimumSize(QtCore.QSize(0, 35))
        self.txt_buscar.setText("")
        self.txt_buscar.setObjectName("txt_buscar")
        self.gridLayout.addWidget(self.txt_buscar, 4, 1, 1, 7)
        self.limpiar = QtWidgets.QPushButton(frmDependientes)
        self.limpiar.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.limpiar.setFont(font)
        self.limpiar.setStyleSheet("border-style: outset;\n"
"background-color: #8458B3;\n"
"color: rgb(235, 232, 235);\n"
"")
        self.limpiar.setObjectName("limpiar")
        self.gridLayout.addWidget(self.limpiar, 6, 7, 1, 1, QtCore.Qt.AlignLeft)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 4, 1, 1)
        self.frame = QtWidgets.QFrame(frmDependientes)
        self.frame.setMinimumSize(QtCore.QSize(400, 50))
        self.frame.setMaximumSize(QtCore.QSize(400, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lbl_foto = QtWidgets.QLabel(self.frame)
        self.lbl_foto.setGeometry(QtCore.QRect(350, 0, 50, 50))
        self.lbl_foto.setMinimumSize(QtCore.QSize(50, 50))
        self.lbl_foto.setMaximumSize(QtCore.QSize(50, 50))
        self.lbl_foto.setObjectName("lbl_foto")
        self.lbl_nombre_usuario = QtWidgets.QLabel(self.frame)
        self.lbl_nombre_usuario.setGeometry(QtCore.QRect(120, 10, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_nombre_usuario.setFont(font)
        self.lbl_nombre_usuario.setObjectName("lbl_nombre_usuario")
        self.gridLayout.addWidget(self.frame, 0, 7, 1, 1)
        self.btn_agregar = QtWidgets.QPushButton(frmDependientes)
        self.btn_agregar.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_agregar.setFont(font)
        self.btn_agregar.setStyleSheet("border-style: outset;\n"
"background-color: #8458B3;\n"
"color: rgb(235, 232, 235);\n"
"")
        self.btn_agregar.setObjectName("btn_agregar")
        self.gridLayout.addWidget(self.btn_agregar, 6, 1, 1, 1, QtCore.Qt.AlignRight)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 6, 6, 1, 1)
        self.frame_2 = QtWidgets.QFrame(frmDependientes)
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
        icon.addPixmap(QtGui.QPixmap("../../Downloads/IconosPDA/Filtro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_filtrar.setIcon(icon)
        self.btn_filtrar.setIconSize(QtCore.QSize(70, 70))
        self.btn_filtrar.setObjectName("btn_filtrar")
        self.btn_buscar = QtWidgets.QPushButton(self.frame_2)
        self.btn_buscar.setGeometry(QtCore.QRect(80, 0, 60, 60))
        self.btn_buscar.setStyleSheet("border-style: outset;\n"
"background-color: :#494D5F;\n"
"\n"
"")
        self.btn_buscar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Downloads/IconosPDA/Lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_buscar.setIcon(icon1)
        self.btn_buscar.setIconSize(QtCore.QSize(70, 70))
        self.btn_buscar.setObjectName("btn_buscar")
        self.gridLayout.addWidget(self.frame_2, 4, 0, 1, 1)
        self.btn_eliminar = QtWidgets.QPushButton(frmDependientes)
        self.btn_eliminar.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_eliminar.setFont(font)
        self.btn_eliminar.setStyleSheet("border-style: outset;\n"
"background-color: #8458B3;\n"
"color: rgb(235, 232, 235);\n"
"")
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.gridLayout.addWidget(self.btn_eliminar, 6, 5, 1, 1)
        self.txt_nombres = QtWidgets.QLineEdit(frmDependientes)
        self.txt_nombres.setMinimumSize(QtCore.QSize(400, 40))
        self.txt_nombres.setObjectName("txt_nombres")
        self.gridLayout.addWidget(self.txt_nombres, 1, 3, 1, 3)
        self.txt_relacion = QtWidgets.QLineEdit(frmDependientes)
        self.txt_relacion.setMinimumSize(QtCore.QSize(400, 40))
        self.txt_relacion.setObjectName("txt_relacion")
        self.gridLayout.addWidget(self.txt_relacion, 2, 0, 1, 3)
        self.txt_apellidos = QtWidgets.QLineEdit(frmDependientes)
        self.txt_apellidos.setMinimumSize(QtCore.QSize(400, 40))
        self.txt_apellidos.setObjectName("txt_apellidos")
        self.gridLayout.addWidget(self.txt_apellidos, 1, 6, 1, 2)
        self.btn_regresar = QtWidgets.QPushButton(frmDependientes)
        self.btn_regresar.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_regresar.setMaximumSize(QtCore.QSize(50, 50))
        self.btn_regresar.setStyleSheet("border-style: outset;\n"
"background-color: :#494D5F;\n"
"")
        self.btn_regresar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../Downloads/IconosPDA/back-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_regresar.setIcon(icon2)
        self.btn_regresar.setIconSize(QtCore.QSize(40, 40))
        self.btn_regresar.setObjectName("btn_regresar")
        self.gridLayout.addWidget(self.btn_regresar, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.btn_editar = QtWidgets.QPushButton(frmDependientes)
        self.btn_editar.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_editar.setFont(font)
        self.btn_editar.setStyleSheet("border-style: outset;\n"
"background-color: #8458B3;\n"
"color: rgb(235, 232, 235);\n"
"")
        self.btn_editar.setObjectName("btn_editar")
        self.gridLayout.addWidget(self.btn_editar, 6, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 6, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 3, 1, 1, 1)
        self.txt_codigo = QtWidgets.QLineEdit(frmDependientes)
        self.txt_codigo.setMinimumSize(QtCore.QSize(400, 40))
        self.txt_codigo.setObjectName("txt_codigo")
        self.gridLayout.addWidget(self.txt_codigo, 1, 0, 1, 3)
        self.tbl_dependientes = QtWidgets.QTableView(frmDependientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_dependientes.sizePolicy().hasHeightForWidth())
        self.tbl_dependientes.setSizePolicy(sizePolicy)
        self.tbl_dependientes.setMinimumSize(QtCore.QSize(0, 500))
        self.tbl_dependientes.setMaximumSize(QtCore.QSize(16777215, 500))
        self.tbl_dependientes.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tbl_dependientes.setObjectName("tbl_dependientes")
        self.gridLayout.addWidget(self.tbl_dependientes, 5, 0, 1, 8)
        self.txt_empleados = QtWidgets.QLineEdit(frmDependientes)
        self.txt_empleados.setMinimumSize(QtCore.QSize(400, 40))
        self.txt_empleados.setObjectName("txt_empleados")
        self.gridLayout.addWidget(self.txt_empleados, 2, 3, 1, 3)

        self.retranslateUi(frmDependientes)
        QtCore.QMetaObject.connectSlotsByName(frmDependientes)

    def retranslateUi(self, frmDependientes):
        _translate = QtCore.QCoreApplication.translate
        frmDependientes.setWindowTitle(_translate("frmDependientes", "Información de dependientes"))
        self.txt_buscar.setPlaceholderText(_translate("frmDependientes", "Buscar"))
        self.limpiar.setText(_translate("frmDependientes", "Limpiar"))
        self.lbl_foto.setText(_translate("frmDependientes", "Foto"))
        self.lbl_nombre_usuario.setText(_translate("frmDependientes", "<html><head/><body><p align=\"right\">Nombre de usuario</p></body></html>"))
        self.btn_agregar.setText(_translate("frmDependientes", "Agregar"))
        self.btn_eliminar.setText(_translate("frmDependientes", "Eliminar"))
        self.txt_nombres.setPlaceholderText(_translate("frmDependientes", "Nombres*"))
        self.txt_relacion.setPlaceholderText(_translate("frmDependientes", "Relacion*"))
        self.txt_apellidos.setPlaceholderText(_translate("frmDependientes", "Apellidos*"))
        self.btn_editar.setText(_translate("frmDependientes", "Editar"))
        self.txt_codigo.setPlaceholderText(_translate("frmDependientes", "Codigo*"))
        self.txt_empleados.setPlaceholderText(_translate("frmDependientes", "Empleados*"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmDependientes = QtWidgets.QWidget()
    ui = Ui_frmDependientes()
    ui.setupUi(frmDependientes)
    frmDependientes.show()
    sys.exit(app.exec_())
