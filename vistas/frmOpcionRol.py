# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmOpcionRol.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from vistas.imagenes import imagenes

class Ui_frmOpcionRol(object):
    def setupUi(self, frmOpcionRol):
        frmOpcionRol.setObjectName("frmOpcionRol")
        frmOpcionRol.resize(1386, 758)
        frmOpcionRol.setMaximumSize(QtCore.QSize(16777215, 2000))
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
        frmOpcionRol.setPalette(palette)
        self.gridLayout = QtWidgets.QGridLayout(frmOpcionRol)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(frmOpcionRol)
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
        self.lbl_foto.setTextFormat(QtCore.Qt.PlainText)
        self.lbl_foto.setPixmap(QtGui.QPixmap(":/iconos/fotoUsuario.png"))
        self.lbl_foto.setScaledContents(True)
        self.lbl_foto.setObjectName("lbl_foto")
        self.lbl_nombre_usuario = QtWidgets.QLabel(self.frame)
        self.lbl_nombre_usuario.setGeometry(QtCore.QRect(120, 10, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_nombre_usuario.setFont(font)
        self.lbl_nombre_usuario.setObjectName("lbl_nombre_usuario")
        self.gridLayout.addWidget(self.frame, 0, 7, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 2, 5, 1, 1)
        self.cbox_rol = QtWidgets.QComboBox(frmOpcionRol)
        self.cbox_rol.setMinimumSize(QtCore.QSize(400, 40))
        self.cbox_rol.setObjectName("cbox_rol")
        self.gridLayout.addWidget(self.cbox_rol, 1, 6, 1, 2)
        self.txt_codigo = QtWidgets.QLineEdit(frmOpcionRol)
        self.txt_codigo.setEnabled(False)
        self.txt_codigo.setMinimumSize(QtCore.QSize(400, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(235, 232, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 232, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 232, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.txt_codigo.setPalette(palette)
        self.txt_codigo.setObjectName("txt_codigo")
        self.gridLayout.addWidget(self.txt_codigo, 1, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 3, 1, 1)
        self.btn_eliminar = QtWidgets.QPushButton(frmOpcionRol)
        self.btn_eliminar.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_eliminar.setFont(font)
        self.btn_eliminar.setStyleSheet("border-style: outset;\n"
"background-color: #8458B3;\n"
"color: rgb(235, 232, 235);\n"
"")
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.gridLayout.addWidget(self.btn_eliminar, 5, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 5, 5, 1, 1)
        self.btn_agregar = QtWidgets.QPushButton(frmOpcionRol)
        self.btn_agregar.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_agregar.setFont(font)
        self.btn_agregar.setStyleSheet("border-style: outset;\n"
"background-color: #8458B3;\n"
"color: rgb(235, 232, 235);\n"
"\n"
"")
        self.btn_agregar.setObjectName("btn_agregar")
        self.gridLayout.addWidget(self.btn_agregar, 5, 2, 1, 1)
        self.cbox_opcion = QtWidgets.QComboBox(frmOpcionRol)
        self.cbox_opcion.setMinimumSize(QtCore.QSize(400, 40))
        self.cbox_opcion.setObjectName("cbox_opcion")
        self.gridLayout.addWidget(self.cbox_opcion, 1, 3, 1, 3)
        self.frame_2 = QtWidgets.QFrame(frmOpcionRol)
        self.frame_2.setMinimumSize(QtCore.QSize(150, 60))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_2.setStyleSheet("border-style: outset;\n"
"background-color: :#494D5F;\n"
"\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.btn_buscar = QtWidgets.QPushButton(self.frame_2)
        self.btn_buscar.setGeometry(QtCore.QRect(40, 0, 60, 60))
        self.btn_buscar.setStyleSheet("border-style: outset;\n"
"background-color: :#494D5F;\n"
"\n"
"")
        self.btn_buscar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconos/Lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_buscar.setIcon(icon)
        self.btn_buscar.setIconSize(QtCore.QSize(70, 70))
        self.btn_buscar.setObjectName("btn_buscar")
        self.gridLayout.addWidget(self.frame_2, 3, 0, 1, 1)
        self.btn_limpiar = QtWidgets.QPushButton(frmOpcionRol)
        self.btn_limpiar.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_limpiar.setFont(font)
        self.btn_limpiar.setStyleSheet("border-style: outset;\n"
"background-color: #8458B3;\n"
"color: rgb(235, 232, 235);\n"
"")
        self.btn_limpiar.setObjectName("btn_limpiar")
        self.gridLayout.addWidget(self.btn_limpiar, 5, 6, 1, 1)
        self.txt_buscar = QtWidgets.QLineEdit(frmOpcionRol)
        self.txt_buscar.setMinimumSize(QtCore.QSize(0, 35))
        self.txt_buscar.setText("")
        self.txt_buscar.setObjectName("txt_buscar")
        self.gridLayout.addWidget(self.txt_buscar, 3, 1, 1, 7)
        self.label = QtWidgets.QLabel(frmOpcionRol)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.tbl_opcionRol = QtWidgets.QTableWidget(frmOpcionRol)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_opcionRol.sizePolicy().hasHeightForWidth())
        self.tbl_opcionRol.setSizePolicy(sizePolicy)
        self.tbl_opcionRol.setMinimumSize(QtCore.QSize(0, 500))
        self.tbl_opcionRol.setMaximumSize(QtCore.QSize(16777215, 500))
        self.tbl_opcionRol.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tbl_opcionRol.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tbl_opcionRol.setObjectName("tbl_opcionRol")
        self.tbl_opcionRol.setColumnCount(3)
        self.tbl_opcionRol.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_opcionRol.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_opcionRol.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_opcionRol.setHorizontalHeaderItem(2, item)
        self.tbl_opcionRol.horizontalHeader().setDefaultSectionSize(456)
        self.tbl_opcionRol.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tbl_opcionRol, 4, 0, 1, 8)

        self.retranslateUi(frmOpcionRol)
        QtCore.QMetaObject.connectSlotsByName(frmOpcionRol)

    def retranslateUi(self, frmOpcionRol):
        _translate = QtCore.QCoreApplication.translate
        frmOpcionRol.setWindowTitle(_translate("frmOpcionRol", "Gestión de Opción-Rol"))
        self.lbl_nombre_usuario.setText(_translate("frmOpcionRol", "<html><head/><body><p align=\"right\">Nombre de usuario</p></body></html>"))
        self.cbox_rol.setPlaceholderText(_translate("frmOpcionRol", "Rol*"))
        self.txt_codigo.setPlaceholderText(_translate("frmOpcionRol", "Código*"))
        self.btn_eliminar.setToolTip(_translate("frmOpcionRol", "Eliminar información de opción-rol"))
        self.btn_eliminar.setText(_translate("frmOpcionRol", "Eliminar"))
        self.btn_agregar.setToolTip(_translate("frmOpcionRol", "Agregar información de opción-rol"))
        self.btn_agregar.setText(_translate("frmOpcionRol", "Agregar"))
        self.cbox_opcion.setPlaceholderText(_translate("frmOpcionRol", "Opción*"))
        self.btn_buscar.setToolTip(_translate("frmOpcionRol", "Buscar"))
        self.btn_limpiar.setToolTip(_translate("frmOpcionRol", "Limpiar información seleccionada"))
        self.btn_limpiar.setText(_translate("frmOpcionRol", "Limpiar"))
        self.txt_buscar.setPlaceholderText(_translate("frmOpcionRol", "Buscar"))
        self.label.setText(_translate("frmOpcionRol", "Datos de Opción-Rol"))
        item = self.tbl_opcionRol.horizontalHeaderItem(0)
        item.setText(_translate("frmOpcionRol", "Código"))
        item = self.tbl_opcionRol.horizontalHeaderItem(1)
        item.setText(_translate("frmOpcionRol", "Opción"))
        item = self.tbl_opcionRol.horizontalHeaderItem(2)
        item.setText(_translate("frmOpcionRol", "Rol"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmOpcionRol = QtWidgets.QWidget()
    ui = Ui_frmOpcionRol()
    ui.setupUi(frmOpcionRol)
    frmOpcionRol.show()
    sys.exit(app.exec_())
