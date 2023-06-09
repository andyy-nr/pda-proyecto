from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.uic.properties import QtWidgets

from datos.Dt_Tbl_user import Dt_tbl_user
from entidades.Tbl_user import Tbl_user

MAYUSCULAS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T',
              'U', 'V', 'W', 'X', 'Y', 'Z']
MINUSCULAS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's','t',
              'u', 'v', 'w', 'x', 'y', 'z']

class ngUsuarios:
    def __init__(self):
        self.user = Tbl_user()
    dtu = Dt_tbl_user()

    def validarUsuarioRepetido(self, user, user_id=None):
        usuarios = self.dtu.listTodosUsuarios()
        if user_id is None:
            for usuario in usuarios:
                if usuario._user == user._user:
                    return False
                if usuario._email == user._email:
                    return False
            return True
        else:
            for usuario in usuarios:
                if usuario._id_user != user_id: # Para que no se compare consigo mismo y no sirva la validacion
                    if usuario._user == user._user:
                        return False
                    if usuario._email == user._email:
                        return False
                return True

    def contraseniaSegura(self, user):
        widget = QWidget()
        if len(user._pwd_temp) <= 8:
            QMessageBox.warning(widget, "Advertencia", "La contraseña debe tener al menos 8 caracteres", QMessageBox.Ok)
            return False
        if not any(letra.isupper() for letra in user._pwd_temp) and any(letra.islower() for letra in user._pwd_temp):
            QMessageBox.warning(widget, "Advertencia", "La contraseña debe tener al menos un número", QMessageBox.Ok)
            return False
        if not any(letra.isdigit() for letra in user._pwd_temp):
            QMessageBox.warning(widget, "Advertencia", "La contraseña debe tener mayúsculas y minúsculas", QMessageBox.Ok)
            return False
        if not any(letra.isalpha() for letra in user._pwd_temp):
            QMessageBox.warning(widget, "Advertencia", "La contraseña debe tener al menos un caracter especial", QMessageBox.Ok)
            return False
        return True

    def contraseniaCoincide(self, user):
        if user._pwd != user._pwd_temp:
            widget = QWidget()
            QMessageBox.warning(widget, "Advertencia", "Las contraseñas no coinciden", QMessageBox.Ok)
            return False
        return True

    def contraseniaNueva(self, user, contra_vieja):
        if user._pwd != contra_vieja:
            widget = QWidget()
            QMessageBox.warning(widget, "Advertencia", "Ingrese la contrasena anterior correctamente")
            return False
        return True

    def agregarUsuario(self, user):
        if not self.validarUsuarioRepetido(user):
            return False
        if not self.contraseniaCoincide(user):
            return False
        if not self.contraseniaSegura(user):
            return False
        self.dtu.agregarUsuario(user)
        return True

    def modificarUsuario(self, user, contra_vieja, user_id):
        if not self.validarUsuarioRepetido(user, user_id):
            return False
        if user._pwd_temp != "":
            if not self.contraseniaSegura(user):
                return False
            if not self.contraseniaNueva(user, contra_vieja):
                return False
            user._pwd = user._pwd_temp
        self.dtu.editarUsuario(user, user_id)
        return True

