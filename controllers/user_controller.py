from models.database import DatabaseModel
from views.user_view import UserView
from tkinter import END

class UserController:
    def __init__(self, model: DatabaseModel, view: UserView):
        self.model = model
        self.view = view

        # Enlazar menús y botones con las funciones de control
        self.view.bbddMenu.add_command(label="Conectar", command=self.conectar_bd)
        self.view.bbddMenu.add_command(label="Salir", command=self.salir)
        self.view.borrarMenu.add_command(label="Borrar campos", command=self.view.limpiar_campos)

        self.view.botonCrear.config(command=self.crear_registro)
        self.view.botonLeer.config(command=self.leer_registro)
        self.view.botonActualizar.config(command=self.actualizar_registro)
        self.view.botonBorrar.config(command=self.eliminar_registro)

    def conectar_bd(self):
        creada = self.model.crear_tabla()
        if creada:
            self.view.mostrar_mensaje("BBDD", "BBDD creada con éxito")
        else:
            self.view.mostrar_mensaje("Atención!", "La BBDD ya existe", "warning")

    def salir(self):
        valor = self.view.mostrar_mensaje("Salir", "¿Desea salir de la aplicación?", "question")
        if valor == "yes":
            self.view.destroy()

    def crear_registro(self):
        try:
            nombre = self.view.miNombre.get()
            password = self.view.miPass.get()
            apellido = self.view.miApellido.get()
            direccion = self.view.miDireccion.get()
            comentarios = self.view.textoComentario.get("1.0", END).strip()

            self.model.insertar(nombre, password, apellido, direccion, comentarios)
            self.view.mostrar_mensaje("BBDD", "Registro insertado con éxito")
            self.view.limpiar_campos()
        except Exception as e:
            self.view.mostrar_mensaje("Error", f"No se pudo insertar: {e}", "error")

    def leer_registro(self):
        try:
            user_id = self.view.miId.get()
            if not user_id:
                self.view.mostrar_mensaje("Atención", "Ingrese un ID para buscar", "warning")
                return

            resultado = self.model.leer(user_id)
            if not resultado:
                self.view.mostrar_mensaje("Atención", "No se encontró ningún usuario con ese ID", "warning")
                return

            self.view.limpiar_campos()
            for usuario in resultado:
                self.view.miId.set(usuario[0])
                self.view.miNombre.set(usuario[1])
                self.view.miPass.set(usuario[2])
                self.view.miApellido.set(usuario[3])
                self.view.miDireccion.set(usuario[4])
                self.view.textoComentario.insert(1.0, usuario[5])
        except Exception as e:
            self.view.mostrar_mensaje("Error", f"Ocurrió un error al leer: {e}", "error")

    def actualizar_registro(self):
        try:
            user_id = self.view.miId.get()
            if not user_id:
                self.view.mostrar_mensaje("Atención", "Ingrese el ID del usuario a actualizar", "warning")
                return

            nombre = self.view.miNombre.get()
            password = self.view.miPass.get()
            apellido = self.view.miApellido.get()
            direccion = self.view.miDireccion.get()
            comentarios = self.view.textoComentario.get("1.0", END).strip()

            self.model.actualizar(user_id, nombre, password, apellido, direccion, comentarios)
            self.view.mostrar_mensaje("BBDD", "Registro actualizado con éxito")
        except Exception as e:
            self.view.mostrar_mensaje("Error", f"No se pudo actualizar: {e}", "error")

    def eliminar_registro(self):
        try:
            user_id = self.view.miId.get()
            if not user_id:
                self.view.mostrar_mensaje("Atención", "Ingrese un ID para eliminar", "warning")
                return

            self.model.eliminar(user_id)
            self.view.mostrar_mensaje("BBDD", "Registro borrado con éxito")
            self.view.limpiar_campos()
        except Exception as e:
            self.view.mostrar_mensaje("Error", f"No se pudo eliminar: {e}", "error")