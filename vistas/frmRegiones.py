# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmRegiones.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmRegiones(object):
    def setupUi(self, frmRegiones):
        frmRegiones.setObjectName("frmRegiones")
        frmRegiones.resize(1180, 758)
        frmRegiones.setMaximumSize(QtCore.QSize(16777215, 2000))
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
        frmRegiones.setPalette(palette)
        self.gridLayout = QtWidgets.QGridLayout(frmRegiones)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_regresar = QtWidgets.QPushButton(frmRegiones)
        self.btn_regresar.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_regresar.setMaximumSize(QtCore.QSize(50, 50))
        self.btn_regresar.setStyleSheet("border-style: outset;\n"
"background-color: :#494D5F;\n"
"\n"
"")
        self.btn_regresar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Downloads/IconosPDA/Flecha.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_regresar.setIcon(icon)
        self.btn_regresar.setIconSize(QtCore.QSize(40, 40))
        self.btn_regresar.setObjectName("btn_regresar")
        self.gridLayout.addWidget(self.btn_regresar, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.txt_nombre_region = QtWidgets.QLineEdit(frmRegiones)
        self.txt_nombre_region.setMinimumSize(QtCore.QSize(400, 40))
        self.txt_nombre_region.setText("")
        self.txt_nombre_region.setObjectName("txt_nombre_region")
        self.gridLayout.addWidget(self.txt_nombre_region, 1, 5, 1, 3)
        self.frame = QtWidgets.QFrame(frmRegiones)
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
        self.gridLayout.addWidget(self.frame, 0, 7, 1, 1, QtCore.Qt.AlignRight)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 6, 1, 1)
        self.btn_limpiar = QtWidgets.QPushButton(frmRegiones)
        self.btn_limpiar.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_limpiar.setFont(font)
        self.btn_limpiar.setStyleSheet("border-style: outset;\n"
"background-color: #8458B3;\n"
"color: rgb(235, 232, 235);\n"
"")
        self.btn_limpiar.setObjectName("btn_limpiar")
        self.gridLayout.addWidget(self.btn_limpiar, 5, 7, 1, 1, QtCore.Qt.AlignLeft)
        self.btn_eliminar = QtWidgets.QPushButton(frmRegiones)
        self.btn_eliminar.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_eliminar.setFont(font)
        self.btn_eliminar.setStyleSheet("border-style: outset;\n"
"background-color: #8458B3;\n"
"color: rgb(235, 232, 235);\n"
"")
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.gridLayout.addWidget(self.btn_eliminar, 5, 5, 1, 1)
        self.txt_codigo = QtWidgets.QLineEdit(frmRegiones)
        self.txt_codigo.setMinimumSize(QtCore.QSize(400, 40))
        self.txt_codigo.setObjectName("txt_codigo")
        self.gridLayout.addWidget(self.txt_codigo, 1, 0, 1, 5)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 5, 2, 1, 1)
        self.btn_editar = QtWidgets.QPushButton(frmRegiones)
        self.btn_editar.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_editar.setFont(font)
        self.btn_editar.setStyleSheet("border-style: outset;\n"
"background-color: #8458B3;\n"
"color: rgb(235, 232, 235);\n"
"")
        self.btn_editar.setObjectName("btn_editar")
        self.gridLayout.addWidget(self.btn_editar, 5, 3, 1, 1)
        self.tbl_regiones = QtWidgets.QTableView(frmRegiones)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_regiones.sizePolicy().hasHeightForWidth())
        self.tbl_regiones.setSizePolicy(sizePolicy)
        self.tbl_regiones.setMinimumSize(QtCore.QSize(0, 500))
        self.tbl_regiones.setMaximumSize(QtCore.QSize(16777215, 500))
        self.tbl_regiones.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tbl_regiones.setObjectName("tbl_regiones")
        self.gridLayout.addWidget(self.tbl_regiones, 4, 0, 1, 8)
        self.btn_agregar = QtWidgets.QPushButton(frmRegiones)
        self.btn_agregar.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_agregar.setFont(font)
        self.btn_agregar.setStyleSheet("border-style: outset;\n"
"background-color: #8458B3;\n"
"color: rgb(235, 232, 235);\n"
"")
        self.btn_agregar.setObjectName("btn_agregar")
        self.gridLayout.addWidget(self.btn_agregar, 5, 1, 1, 1, QtCore.Qt.AlignRight)
        self.txt_buscar = QtWidgets.QLineEdit(frmRegiones)
        self.txt_buscar.setMinimumSize(QtCore.QSize(0, 35))
        self.txt_buscar.setText("")
        self.txt_buscar.setObjectName("txt_buscar")
        self.gridLayout.addWidget(self.txt_buscar, 3, 1, 1, 7)
        self.frame_2 = QtWidgets.QFrame(frmRegiones)
        self.frame_2.setMinimumSize(QtCore.QSize(150, 60))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.btn_filtro = QtWidgets.QPushButton(self.frame_2)
        self.btn_filtro.setGeometry(QtCore.QRect(10, 0, 60, 60))
        self.btn_filtro.setMinimumSize(QtCore.QSize(60, 0))
        self.btn_filtro.setMaximumSize(QtCore.QSize(60, 60))
        self.btn_filtro.setStyleSheet("border-style: outset;\n"
"background-color: :#494D5F;\n"
"")
        self.btn_filtro.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Downloads/IconosPDA/Filtro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_filtro.setIcon(icon1)
        self.btn_filtro.setIconSize(QtCore.QSize(70, 70))
        self.btn_filtro.setObjectName("btn_filtro")
        self.btn_buscar = QtWidgets.QPushButton(self.frame_2)
        self.btn_buscar.setGeometry(QtCore.QRect(80, 0, 60, 60))
        self.btn_buscar.setStyleSheet("border-style: outset;\n"
"background-color: :#494D5F;\n"
"\n"
"\n"
"")
        self.btn_buscar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../Downloads/IconosPDA/Lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_buscar.setIcon(icon2)
        self.btn_buscar.setIconSize(QtCore.QSize(70, 70))
        self.btn_buscar.setObjectName("btn_buscar")
        self.gridLayout.addWidget(self.frame_2, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 2, 5, 1, 1)

        self.retranslateUi(frmRegiones)
        QtCore.QMetaObject.connectSlotsByName(frmRegiones)

    def retranslateUi(self, frmRegiones):
        _translate = QtCore.QCoreApplication.translate
        frmRegiones.setWindowTitle(_translate("frmRegiones", "Información de regiones"))
        self.txt_nombre_region.setPlaceholderText(_translate("frmRegiones", "Nombre de la región*"))
        self.lbl_foto.setText(_translate("frmRegiones", "Foto"))
        self.lbl_nombre_usuario.setText(_translate("frmRegiones", "<html><head/><body><p align=\"right\">Nombre de usuario</p></body></html>"))
        self.btn_limpiar.setText(_translate("frmRegiones", "Limpiar"))
        self.btn_eliminar.setText(_translate("frmRegiones", "Eliminar"))
        self.txt_codigo.setPlaceholderText(_translate("frmRegiones", "Código*"))
        self.btn_editar.setText(_translate("frmRegiones", "Editar"))
        self.btn_agregar.setText(_translate("frmRegiones", "Agregar"))
        self.txt_buscar.setPlaceholderText(_translate("frmRegiones", "Buscar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmRegiones = QtWidgets.QWidget()
    ui = Ui_frmRegiones()
    ui.setupUi(frmRegiones)
    frmRegiones.show()
    sys.exit(app.exec_())
