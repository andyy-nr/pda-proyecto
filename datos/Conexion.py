import sys
import pymysql.cursors


class Conexion:
    _DATABASE = 'Seguridad'
    _USERNAME = 'root'
    _PASSWORD = '112358'
    _HOST = 'localhost'
    _conexion = None
    _cursor = None

    @classmethod
    def getConnection(cls):
        if cls._conexion is None:
            try:
                cls._conexion = pymysql.connect(user=cls._USERNAME,
                                                password=cls._PASSWORD,
                                                host=cls._HOST,
                                                database=cls._DATABASE,
                                                cursorclass=pymysql.cursors.DictCursor)
                print(f'Conexión exitosa a la BD: {cls._DATABASE} & {cls._conexion}')
                return cls._conexion
            except Exception as e:
                print(f'Ocurrio una excepcion {e}')
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def getCursor(cls):
        if cls._cursor is None:

            try:
                cls._cursor = cls.getConnection().cursor()
                print(f'Se abrió correctamente el cursor: {cls._cursor}')
                return cls._cursor
            except Exception as e:
                print(f'Ocurrio un error {e}')
                sys.exit()
        else:
            return cls._cursor

    @classmethod
    def closeConnection(cls):
        if cls._conexion:
            cls._conexion.close()
            cls._conexion = None
            print("Se cerro la conexion")
        else:
            print("No hay conexion que cerrar")

    @classmethod
    def closeCursor(cls):
        if cls._cursor:
            cls._cursor.close()
            cls._cursor = None
            print("Se cerro el cursor")
        else:
            print("No hay cursor que cerrar")


if __name__ == '__main__':
    Conexion.getConnection()
    Conexion.getCursor()
