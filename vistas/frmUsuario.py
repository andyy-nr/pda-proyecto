# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmUsuario.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmUsuario(object):
    def setupUi(self, frmUsuario):
        frmUsuario.setObjectName("frmUsuario")
        frmUsuario.resize(1576, 804)
        frmUsuario.setMaximumSize(QtCore.QSize(16777215, 2000))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(229, 234, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(132, 88, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 234, 245))
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
        brush = QtGui.QBrush(QtGui.QColor(132, 88, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 234, 245))
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
        brush = QtGui.QBrush(QtGui.QColor(132, 88, 179))
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
        frmUsuario.setPalette(palette)
        self.gridLayout = QtWidgets.QGridLayout(frmUsuario)
        self.gridLayout.setObjectName("gridLayout")
        self.le_nombre_usuario = QtWidgets.QLineEdit(frmUsuario)
        self.le_nombre_usuario.setMinimumSize(QtCore.QSize(400, 40))
        self.le_nombre_usuario.setObjectName("le_nombre_usuario")
        self.gridLayout.addWidget(self.le_nombre_usuario, 1, 7, 1, 1)
        self.btn_agregar = QtWidgets.QPushButton(frmUsuario)
        self.btn_agregar.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_agregar.setFont(font)
        self.btn_agregar.setStyleSheet("border-style: outset;\n"
"background-color: #8458B3;\n"
"color: rgb(235, 232, 235);")
        self.btn_agregar.setObjectName("btn_agregar")
        self.gridLayout.addWidget(self.btn_agregar, 6, 1, 1, 1, QtCore.Qt.AlignRight)
        self.le_buscar = QtWidgets.QLineEdit(frmUsuario)
        self.le_buscar.setMinimumSize(QtCore.QSize(0, 35))
        self.le_buscar.setText("")
        self.le_buscar.setObjectName("le_buscar")
        self.gridLayout.addWidget(self.le_buscar, 4, 1, 1, 7)
        self.le_email = QtWidgets.QLineEdit(frmUsuario)
        self.le_email.setMinimumSize(QtCore.QSize(400, 40))
        self.le_email.setText("")
        self.le_email.setObjectName("le_email")
        self.gridLayout.addWidget(self.le_email, 2, 0, 1, 4)
        self.tbl_Usuario = QtWidgets.QTableView(frmUsuario)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_Usuario.sizePolicy().hasHeightForWidth())
        self.tbl_Usuario.setSizePolicy(sizePolicy)
        self.tbl_Usuario.setMinimumSize(QtCore.QSize(0, 500))
        self.tbl_Usuario.setMaximumSize(QtCore.QSize(16777215, 500))
        self.tbl_Usuario.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tbl_Usuario.setObjectName("tbl_Usuario")
        self.gridLayout.addWidget(self.tbl_Usuario, 5, 0, 1, 8)
        self.frame_2 = QtWidgets.QFrame(frmUsuario)
        self.frame_2.setMinimumSize(QtCore.QSize(150, 60))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.btn_filtrar = QtWidgets.QPushButton(self.frame_2)
        self.btn_filtrar.setGeometry(QtCore.QRect(10, 0, 60, 60))
        self.btn_filtrar.setMinimumSize(QtCore.QSize(60, 0))
        self.btn_filtrar.setMaximumSize(QtCore.QSize(60, 60))
        self.btn_filtrar.setStyleSheet("border-style: outset;\n"
"background-color:  :#494D5F;\n"
"\n"
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
"background-color:  :#494D5F;\n"
"\n"
"\n"
"")
        self.btn_buscar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/iconos/Lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_buscar.setIcon(icon1)
        self.btn_buscar.setIconSize(QtCore.QSize(70, 70))
        self.btn_buscar.setObjectName("btn_buscar")
        self.gridLayout.addWidget(self.frame_2, 4, 0, 1, 1, QtCore.Qt.AlignRight)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 3, 5, 1, 1)
        self.le_codigo = QtWidgets.QLineEdit(frmUsuario)
        self.le_codigo.setEnabled(False)
        self.le_codigo.setMinimumSize(QtCore.QSize(380, 40))
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
        self.le_codigo.setPalette(palette)
        self.le_codigo.setObjectName("le_codigo")
        self.gridLayout.addWidget(self.le_codigo, 1, 4, 1, 3)
        self.btn_regresar = QtWidgets.QPushButton(frmUsuario)
        self.btn_regresar.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_regresar.setMaximumSize(QtCore.QSize(50, 50))
        self.btn_regresar.setStyleSheet("border-style: outset;\n"
"background-color: #494D5F;\n"
"")
        self.btn_regresar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/iconos/Flecha.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_regresar.setIcon(icon2)
        self.btn_regresar.setIconSize(QtCore.QSize(40, 40))
        self.btn_regresar.setObjectName("btn_regresar")
        self.gridLayout.addWidget(self.btn_regresar, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.le_confirmacion = QtWidgets.QLineEdit(frmUsuario)
        self.le_confirmacion.setMinimumSize(QtCore.QSize(400, 40))
        self.le_confirmacion.setText("")
        self.le_confirmacion.setObjectName("le_confirmacion")
        self.gridLayout.addWidget(self.le_confirmacion, 2, 7, 1, 1)
        self.le_nombres = QtWidgets.QLineEdit(frmUsuario)
        self.le_nombres.setMinimumSize(QtCore.QSize(380, 40))
        self.le_nombres.setObjectName("le_nombres")
        self.gridLayout.addWidget(self.le_nombres, 1, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 6, 6, 1, 1)
        self.frame = QtWidgets.QFrame(frmUsuario)
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
        self.btn_eliminar = QtWidgets.QPushButton(frmUsuario)
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
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 6, 4, 1, 1)
        self.le_apellidos = QtWidgets.QLineEdit(frmUsuario)
        self.le_apellidos.setMinimumSize(QtCore.QSize(380, 40))
        self.le_apellidos.setObjectName("le_apellidos")
        self.gridLayout.addWidget(self.le_apellidos, 1, 2, 1, 2)
        self.btn_editar = QtWidgets.QPushButton(frmUsuario)
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
        self.le_contrasena = QtWidgets.QLineEdit(frmUsuario)
        self.le_contrasena.setMinimumSize(QtCore.QSize(380, 40))
        self.le_contrasena.setObjectName("le_contrasena")
        self.gridLayout.addWidget(self.le_contrasena, 2, 4, 1, 3)
        self.btn_limpiar = QtWidgets.QPushButton(frmUsuario)
        self.btn_limpiar.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_limpiar.setFont(font)
        self.btn_limpiar.setStyleSheet("border-style: outset;\n"
"background-color: #8458B3;\n"
"color: rgb(235, 232, 235);\n"
"")
        self.btn_limpiar.setObjectName("btn_limpiar")
        self.gridLayout.addWidget(self.btn_limpiar, 6, 7, 1, 1, QtCore.Qt.AlignLeft)

        self.retranslateUi(frmUsuario)
        QtCore.QMetaObject.connectSlotsByName(frmUsuario)

    def retranslateUi(self, frmUsuario):
        _translate = QtCore.QCoreApplication.translate
        frmUsuario.setWindowTitle(_translate("frmUsuario", "Información de usuario"))
        self.le_nombre_usuario.setPlaceholderText(_translate("frmUsuario", "Nombre de usuario*"))
        self.btn_agregar.setToolTip(_translate("frmUsuario", "Agregar información de usuario"))
        self.btn_agregar.setText(_translate("frmUsuario", "Agregar"))
        self.le_buscar.setPlaceholderText(_translate("frmUsuario", "Buscar"))
        self.le_email.setPlaceholderText(_translate("frmUsuario", "Email*"))
        self.btn_filtrar.setToolTip(_translate("frmUsuario", "Filtrar por..."))
        self.btn_buscar.setToolTip(_translate("frmUsuario", "Buscar elemento"))
        self.le_codigo.setPlaceholderText(_translate("frmUsuario", "Codigo*"))
        self.le_confirmacion.setPlaceholderText(_translate("frmUsuario", "Confirmacion*"))
        self.le_nombres.setPlaceholderText(_translate("frmUsuario", "Nombres*"))
        self.lbl_nombre_usuario.setText(_translate("frmUsuario", "<html><head/><body><p align=\"right\">Nombre de usuario</p></body></html>"))
        self.btn_eliminar.setToolTip(_translate("frmUsuario", "Eliminar información de usuario´"))
        self.btn_eliminar.setText(_translate("frmUsuario", "Eliminar"))
        self.le_apellidos.setPlaceholderText(_translate("frmUsuario", "Apellidos*"))
        self.btn_editar.setToolTip(_translate("frmUsuario", "Editar información de usuario"))
        self.btn_editar.setText(_translate("frmUsuario", "Editar"))
        self.le_contrasena.setPlaceholderText(_translate("frmUsuario", "Contraseña*"))
        self.btn_limpiar.setToolTip(_translate("frmUsuario", "Limpiar información seleccionada"))
        self.btn_limpiar.setText(_translate("frmUsuario", "Limpiar"))
import imagenes_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmUsuario = QtWidgets.QWidget()
    ui = Ui_frmUsuario()
    ui.setupUi(frmUsuario)
    frmUsuario.show()
    sys.exit(app.exec_())