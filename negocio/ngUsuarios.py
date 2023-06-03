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

    def validarUsuarioRepetido(self, user):
        usuarios = self.dtu.listTodosUsuarios()
        for usuario in usuarios:
            if usuario._user == user._user:
                return False
            if usuario._email == user._email:
                return False
        return True

    def contraseniaSegura(self, user):
        if len(user._pwd_temp) <= 8:
            print("La contraseña debe tener al menos 8 caracteres")
            #QtWidgets.QMessageBox.warning(self, "Advertencia", "La contraseña debe tener al menos 8 caracteres", QtWidgets.QMessageBox.Ok)
            return False
        if not any(letra.isupper() for letra in user._pwd_temp) and any(letra.islower() for letra in user._pwd_temp):
            print("La contrase;a debe tener al menos una mayuscula y una minuscula")
            #QtWidgets.QMessageBox.warning(self, "Advertencia", "La contraseña debe tener al menos un número", QtWidgets.QMessageBox.Ok)
            return False
        if not any(letra.isdigit() for letra in user._pwd_temp):
            print("La contrase;a debe tener al menos un numero")
            #QtWidgets.QMessageBox.warning(self, "Advertencia", "La contraseña debe tener mayúsculas y minúsculas", QtWidgets.QMessageBox.Ok)
            return False
        if not any(letra.isalpha() for letra in user._pwd_temp):
            print("La contrase;a debe tener al menos un caracter especial")
            #QtWidgets.QMessageBox.warning(self, "Advertencia", "La contraseña debe tener al menos un caracter especial", QtWidgets.QMessageBox.Ok)
            return False
        return True

    def contraseniaCoincide(self, user):
        if user._pwd != user._pwd_temp:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Las contraseñas no coinciden", QtWidgets.QMessageBox.Ok)
            return False
        return True



    def contraseniaNueva(self, user, contra_vieja):
        if user._pwd != contra_vieja:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Ingrese la contrasena anterior correctamente")
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

    def modificarUsuario(self, user, contra_vieja, id):
        if not self.contraseniaSegura(user):
            return False
        if not self.contraseniaNueva(user, contra_vieja):
            return False
        user._pwd = user._pwd_temp
        self.dtu.editarUsuario(user, id)
        return True


