import sqlite3

class DatabaseModel:
    def __init__(self, db_name="Usuarios.db"):
        self.db_name = db_name

    def conectar(self):
        return sqlite3.connect(self.db_name)

    def crear_tabla(self):
        conexion = self.conectar()
        cursor = conexion.cursor()
        try:
            cursor.execute('''
                CREATE TABLE DATOSUSUARIOS (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    NOMBRE_USUARIO VARCHAR(50),
                    PASSWORD VARCHAR(50),
                    APELLIDO VARCHAR(50),
                    DIRECCION VARCHAR(50),
                    COMENTARIOS VARCHAR(100)
                )
            ''')
            conexion.commit()
            return True
        except sqlite3.OperationalError:
            return False
        finally:
            conexion.close()

    def insertar(self, nombre, password, apellido, direccion, comentarios):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO DATOSUSUARIOS VALUES (NULL, ?, ?, ?, ?, ?)",
            (nombre, password, apellido, direccion, comentarios)
        )
        conexion.commit()
        conexion.close()

    def leer(self, user_id):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=?", (user_id,))
        resultado = cursor.fetchall()
        conexion.close()
        return resultado

    def actualizar(self, user_id, nombre, password, apellido, direccion, comentarios):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE DATOSUSUARIOS 
            SET NOMBRE_USUARIO=?, PASSWORD=?, APELLIDO=?, DIRECCION=?, COMENTARIOS=? 
            WHERE ID=?
        """, (nombre, password, apellido, direccion, comentarios, user_id))
        conexion.commit()
        conexion.close()

    def eliminar(self, user_id):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=?", (user_id,))
        conexion.commit()
        conexion.close()