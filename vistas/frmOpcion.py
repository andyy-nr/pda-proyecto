# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmOpcion.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmOpcion(object):
    def setupUi(self, frmOpcion):
        frmOpcion.setObjectName("frmOpcion")
        frmOpcion.resize(1192, 758)
        frmOpcion.setMaximumSize(QtCore.QSize(16777215, 2000))
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
        frmOpcion.setPalette(palette)
        self.gridLayout = QtWidgets.QGridLayout(frmOpcion)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_eliminar = QtWidgets.QPushButton(frmOpcion)
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
        self.txt_codigo = QtWidgets.QLineEdit(frmOpcion)
        self.txt_codigo.setMinimumSize(QtCore.QSize(400, 40))
        self.txt_codigo.setObjectName("txt_codigo")
        self.gridLayout.addWidget(self.txt_codigo, 1, 0, 1, 5)
        self.frame = QtWidgets.QFrame(frmOpcion)
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
        self.gridLayout.addWidget(self.frame, 0, 7, 1, 1, QtCore.Qt.AlignRight)
        self.lineEdit = QtWidgets.QLineEdit(frmOpcion)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 1, 1, 7)
        self.btn_limpiar = QtWidgets.QPushButton(frmOpcion)
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
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 2, 1, 1)
        self.frame_2 = QtWidgets.QFrame(frmOpcion)
        self.frame_2.setMinimumSize(QtCore.QSize(150, 60))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.btn_buscar = QtWidgets.QPushButton(self.frame_2)
        self.btn_buscar.setGeometry(QtCore.QRect(40, 0, 60, 60))
        self.btn_buscar.setStyleSheet("border-style: outset;\n"
"background-color: :#494D5F;\n"
"")
        self.btn_buscar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconos/Lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_buscar.setIcon(icon)
        self.btn_buscar.setIconSize(QtCore.QSize(70, 70))
        self.btn_buscar.setObjectName("btn_buscar")
        self.gridLayout.addWidget(self.frame_2, 3, 0, 1, 1)
        self.txt_opcion = QtWidgets.QLineEdit(frmOpcion)
        self.txt_opcion.setMinimumSize(QtCore.QSize(400, 40))
        self.txt_opcion.setText("")
        self.txt_opcion.setObjectName("txt_opcion")
        self.gridLayout.addWidget(self.txt_opcion, 1, 5, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 2, 5, 1, 1)
        self.btn_agregar = QtWidgets.QPushButton(frmOpcion)
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
        self.btn_editar = QtWidgets.QPushButton(frmOpcion)
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
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 5, 6, 1, 1)
        self.tbl_opcion = QtWidgets.QTableWidget(frmOpcion)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_opcion.sizePolicy().hasHeightForWidth())
        self.tbl_opcion.setSizePolicy(sizePolicy)
        self.tbl_opcion.setMinimumSize(QtCore.QSize(0, 500))
        self.tbl_opcion.setMaximumSize(QtCore.QSize(16777215, 500))
        self.tbl_opcion.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tbl_opcion.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tbl_opcion.setObjectName("tbl_opcion")
        self.tbl_opcion.setColumnCount(2)
        self.tbl_opcion.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_opcion.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_opcion.setHorizontalHeaderItem(1, item)
        self.tbl_opcion.horizontalHeader().setDefaultSectionSize(590)
        self.tbl_opcion.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tbl_opcion, 4, 0, 1, 8)
        self.frame_3 = QtWidgets.QFrame(frmOpcion)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(60, 0, 211, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_regresar = QtWidgets.QPushButton(self.frame_3)
        self.btn_regresar.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.btn_regresar.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_regresar.setStyleSheet("image: url(:/iconos/Flecha.png);\n"
"border-style: outset;\n"
"background-color: #8458B3;")
        self.btn_regresar.setText("")
        self.btn_regresar.setObjectName("btn_regresar")
        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 2)

        self.retranslateUi(frmOpcion)
        QtCore.QMetaObject.connectSlotsByName(frmOpcion)

    def retranslateUi(self, frmOpcion):
        _translate = QtCore.QCoreApplication.translate
        frmOpcion.setWindowTitle(_translate("frmOpcion", "Gestión de Opciones"))
        self.btn_eliminar.setToolTip(_translate("frmOpcion", "Eliminar información de opción"))
        self.btn_eliminar.setText(_translate("frmOpcion", "Eliminar"))
        self.txt_codigo.setPlaceholderText(_translate("frmOpcion", "Código*"))
        self.lbl_nombre_usuario.setText(_translate("frmOpcion", "<html><head/><body><p align=\"right\">Nombre de usuario</p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("frmOpcion", "Buscar"))
        self.btn_limpiar.setToolTip(_translate("frmOpcion", "Limpiar información seleccionada"))
        self.btn_limpiar.setText(_translate("frmOpcion", "Limpiar"))
        self.btn_buscar.setToolTip(_translate("frmOpcion", "Buscar"))
        self.txt_opcion.setPlaceholderText(_translate("frmOpcion", "Opción*"))
        self.btn_agregar.setToolTip(_translate("frmOpcion", "Agregar información de opción"))
        self.btn_agregar.setText(_translate("frmOpcion", "Agregar"))
        self.btn_editar.setToolTip(_translate("frmOpcion", "Editar información de opción"))
        self.btn_editar.setText(_translate("frmOpcion", "Editar"))
        item = self.tbl_opcion.horizontalHeaderItem(0)
        item.setText(_translate("frmOpcion", "Código"))
        item = self.tbl_opcion.horizontalHeaderItem(1)
        item.setText(_translate("frmOpcion", "Opción"))
        self.label.setText(_translate("frmOpcion", "Datos de las opciones"))
from vistas.imagenes import imagenes

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmOpcion = QtWidgets.QWidget()
    ui = Ui_frmOpcion()
    ui.setupUi(frmOpcion)
    frmOpcion.show()
    sys.exit(app.exec_())
