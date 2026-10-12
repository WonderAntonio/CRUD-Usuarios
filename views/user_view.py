from tkinter import *
from tkinter import messagebox

class UserView(Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema CRUD - Python & SQLite")
        self.geometry("350x450")
        self.resizable(False, False)

        # Variables de control
        self.miId = StringVar()
        self.miNombre = StringVar()
        self.miApellido = StringVar()
        self.miPass = StringVar()
        self.miDireccion = StringVar()

        self._crear_menu()
        self._crear_widgets()

    def _crear_menu(self):
        self.barraMenu = Menu(self)
        self.config(menu=self.barraMenu)

        self.bbddMenu = Menu(self.barraMenu, tearoff=0)
        self.barraMenu.add_cascade(label="BBDD", menu=self.bbddMenu)

        self.borrarMenu = Menu(self.barraMenu, tearoff=0)
        self.barraMenu.add_cascade(label="Borrar", menu=self.borrarMenu)

        self.crudMenu = Menu(self.barraMenu, tearoff=0)
        self.barraMenu.add_cascade(label="CRUD", menu=self.crudMenu)

        self.ayudaMenu = Menu(self.barraMenu, tearoff=0)
        self.barraMenu.add_cascade(label="Ayuda", menu=self.ayudaMenu)

    def _crear_widgets(self):
        self.miFrame = Frame(self)
        self.miFrame.pack(padx=20, pady=20)

        # Entradas (Entries)
        self.cuadroID = Entry(self.miFrame, textvariable=self.miId)
        self.cuadroID.grid(row=0, column=1, padx=10, pady=5)

        self.cuadroNombre = Entry(self.miFrame, textvariable=self.miNombre)
        self.cuadroNombre.grid(row=1, column=1, padx=10, pady=5)
        self.cuadroNombre.config(fg="red", justify="right")

        self.cuadroPass = Entry(self.miFrame, textvariable=self.miPass)
        self.cuadroPass.grid(row=2, column=1, padx=10, pady=5)
        self.cuadroPass.config(show="*")

        self.cuadroApellido = Entry(self.miFrame, textvariable=self.miApellido)
        self.cuadroApellido.grid(row=3, column=1, padx=10, pady=5)

        self.cuadroDireccion = Entry(self.miFrame, textvariable=self.miDireccion)
        self.cuadroDireccion.grid(row=4, column=1, padx=10, pady=5)

        self.textoComentario = Text(self.miFrame, width=16, height=5)
        self.textoComentario.grid(row=5, column=1, padx=10, pady=5)

        self.scrollVer = Scrollbar(self.miFrame, command=self.textoComentario.yview)
        self.scrollVer.grid(row=5, column=2, sticky="nsew")
        self.textoComentario.config(yscrollcommand=self.scrollVer.set)

        # Etiquetas (Labels)
        labels_text = ["Id:", "Nombre:", "Password:", "Apellido:", "Direccion:", "Comentarios:"]
        for i, text in enumerate(labels_text):
            Label(self.miFrame, text=text).grid(row=i, column=0, sticky="e", padx=10, pady=5)

        # Botones inferiores
        self.miFrame2 = Frame(self)
        self.miFrame2.pack(pady=10)

        self.botonCrear = Button(self.miFrame2, text="Create")
        self.botonCrear.grid(row=0, column=0, padx=5)

        self.botonLeer = Button(self.miFrame2, text="Read")
        self.botonLeer.grid(row=0, column=1, padx=5)

        self.botonActualizar = Button(self.miFrame2, text="Update")
        self.botonActualizar.grid(row=0, column=2, padx=5)

        self.botonBorrar = Button(self.miFrame2, text="Delete")
        self.botonBorrar.grid(row=0, column=3, padx=5)

    def limpiar_campos(self):
        self.miId.set("")
        self.miNombre.set("")
        self.miPass.set("")
        self.miApellido.set("")
        self.miDireccion.set("")
        self.textoComentario.delete(1.0, END)

    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "info":
            messagebox.showinfo(titulo, mensaje)
        elif tipo == "warning":
            messagebox.showwarning(titulo, mensaje)
        elif tipo == "error":
            messagebox.showerror(titulo, mensaje)
        elif tipo == "question":
            return messagebox.askquestion(titulo, mensaje)