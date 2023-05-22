import sys
from PyQt5 import QtWidgets, QtCore
from controlador.ctrInicioSesion import CtrlInicioSesion
from datos.Dt_Tbl_user import Dt_tbl_user
from controlador.ctrPrimerUsuario import CtrlPrimerUsuario


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    du = Dt_tbl_user()
    usuarios = du.listUsuarios()
    if not usuarios:
        crearUsuario = CtrlPrimerUsuario()
        crearUsuario.show()
    else:
        frm = CtrlInicioSesion()
        frm.show()
    sys.exit(app.exec_())



