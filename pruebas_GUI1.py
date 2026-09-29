import tkinter as tk
from tkinter import ttk 
from finanzas_core import intereses as inter
from cli import input_helpers as ih

class Aplicacion(tk.Tk):
    #Ventana principal
    def __init__(self):
        super().__init__()
        self.title("GUI Básica Finanzas")
        self.geometry("800x450+250+100")
        self.minsize(400,225)
        self.configure(bg = "pale green")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=3)
        self.rowconfigure(1, weight=1)
        self.entrada = Entrada(self)
        self.entrada.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.salida = Salida(self)
        self.salida.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        self.entrada.al_producir(self.salida.mostrar)
        print("App arrancada")

class Entrada(ttk.Frame):
    #Entrada de datos
    def __init__(self, parent):
        super().__init__(parent)
        self.callbacks = []
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.entryo = ttk.Entry(self)
        self.entryo.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        self.entryn = ttk.Entry(self)
        self.entryn.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
        self.entryo.bind("<Return>", self.verificar)
        self.entryn.bind("<Return>", self.verificar)
        self.labelo = ttk.Label(self, text="Ingrese el valor original")
        self.labelo.grid(row=1, column=0)
        self.labeln = ttk.Label(self, text="Ingrese el valor resultante")
        self.labeln.grid(row=1, column=1)
        self.error_m = ttk.Label(self, text="Ha ingresado un valor incorrecto")
        self.error_m.grid(row=0, column=0, columnspan=2)
        self.error_m.grid_remove()
        self.boton = ttk.Button(self, text= "Calcular", command=self.verificar)
        self.boton.grid(row=2, column=2)
        print("Entrada creada")

    def al_producir(self, callback):
        self.callbacks.append(callback)
        print("Llamada a B")

    def verificar(self, _event=None):
        original = self.entryo.get()
        nuevo = self.entryn.get()
        print("Valores ajustados")
        if ih.validar_numero(original) & ih.validar_numero(nuevo):
            self.computar(float(original), float(nuevo))
            if self.error_m.winfo_ismapped():
                self.error_m.grid_remove()
            self.entryo.focus_set()
            print("Valor aceptado")
        else:
            self.error_m.grid()
            if not ih.validar_numero(original):
                self.entryo.focus_set()
                print("Valor original rechazado")
            else:
                self.entryn.focus_set()
                print("Valor nuevo rechazado")

    def computar(self, original, nuevo):
        resultado = inter.calcular_valor_interes(original, nuevo)
        print("Resultado calculado")
        for cb in self.callbacks:
            cb(resultado)
        

class Salida(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.label = ttk.Label(self, text="Resultado: ")
        self.label.grid(row=0, column=0)
        self.result = ttk.Label(self, text = "")
        self.result.grid(row=0, column= 1, padx=5, pady=5)
        self.result.grid_remove()
        print("Salida creada")

    def mostrar(self, valor):
        self.result.config(text=str(valor) + " Total de intereses")
        self.result.grid()
        print("Mostrando resultado")


app = Aplicacion()
app.mainloop()