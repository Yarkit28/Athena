"""
Interfaz Gráfica de Usuario (GUI) - Athena Finanzas
Construida en Tkinter estándar.
Consume exclusivamente la capa de aplicación (finanzas_app) sin acoplamiento con la capa Core.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

# Asegurar importación del paquete finanzas_app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from finanzas_app import (
    cu_calcular_pago_mensual_prestamo,
    cu_calcular_cantidad_nueva_compuesta,
    cu_calcular_fondo_necesario,
    cu_calcular_tabla_amortizacion,
    ErrorFinancieroApp,
)

class AthenaGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Athena — Sistema Financiero (Misión 3.2)")
        self.geometry("750x550")
        self.minsize(650, 450)
        
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        self._crear_pestana_prestamos()
        self._crear_pestana_interes_compuesto()
        self._crear_pestana_retiro()
        self._crear_pestana_amortizacion()
        
    def _crear_pestana_prestamos(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Préstamos")
        
        ttk.Label(tab, text="Cálculo de Cuota Mensual de Préstamo", font=("Helvetica", 12, "bold")).pack(pady=10)
        
        frame = ttk.LabelFrame(tab, text=" Parámetros del Préstamo ")
        frame.pack(fill="x", padx=15, pady=5)
        
        ttk.Label(frame, text="Monto Principal ($):").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        ent_principal = ttk.Entry(frame)
        ent_principal.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame, text="Tasa Anual Decimal (ej. 0.10 para 10%):").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        ent_tasa = ttk.Entry(frame)
        ent_tasa.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(frame, text="Plazo (Meses):").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        ent_meses = ttk.Entry(frame)
        ent_meses.grid(row=2, column=1, padx=5, pady=5)
        
        txt_resultado = tk.Text(tab, height=8, width=70)
        
        def calcular():
            txt_resultado.delete("1.0", tk.END)
            try:
                res = cu_calcular_pago_mensual_prestamo(
                    principal=ent_principal.get(),
                    tasa_anual_decimal=ent_tasa.get(),
                    meses=ent_meses.get()
                )
                txt_resultado.insert(tk.END, f"=== RESULTADO DEL PRÉSTAMO ===\n")
                txt_resultado.insert(tk.END, f"• Pago Mensual: ${res['pago_mensual']:,.2f}\n")
                txt_resultado.insert(tk.END, f"• Total a Pagar: ${res['total_pagar']:,.2f}\n")
                txt_resultado.insert(tk.END, f"• Total Intereses: ${res['total_intereses']:,.2f}\n")
            except ErrorFinancieroApp as e:
                messagebox.showerror("Error de Aplicación", str(e))
            except Exception as e:
                messagebox.showerror("Error Inesperado", f"Ocurrió un error: {e}")

        btn_calc = ttk.Button(tab, text="Calcular Préstamo", command=calcular)
        btn_calc.pack(pady=10)
        txt_resultado.pack(padx=15, pady=5, fill="both", expand=True)

    def _crear_pestana_interes_compuesto(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Interés Compuesto")
        
        ttk.Label(tab, text="Proyección de Interés Compuesto", font=("Helvetica", 12, "bold")).pack(pady=10)
        
        frame = ttk.LabelFrame(tab, text=" Parámetros ")
        frame.pack(fill="x", padx=15, pady=5)
        
        ttk.Label(frame, text="Monto Inicial ($):").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        ent_principal = ttk.Entry(frame)
        ent_principal.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame, text="Tasa Anual Decimal (ej. 0.08):").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        ent_tasa = ttk.Entry(frame)
        ent_tasa.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(frame, text="Años:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        ent_anios = ttk.Entry(frame)
        ent_anios.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Periodos por año (ej. 12 para mensual):").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        ent_periodos = ttk.Entry(frame)
        ent_periodos.insert(0, "12")
        ent_periodos.grid(row=3, column=1, padx=5, pady=5)
        
        txt_resultado = tk.Text(tab, height=8, width=70)
        
        def calcular():
            txt_resultado.delete("1.0", tk.END)
            try:
                res = cu_calcular_cantidad_nueva_compuesta(
                    cantidad_original=ent_principal.get(),
                    interes=ent_tasa.get(),
                    anios=ent_anios.get(),
                    periodos=ent_periodos.get()
                )
                txt_resultado.insert(tk.END, f"=== RESULTADO PROYECTADO ===\n")
                txt_resultado.insert(tk.END, f"• Monto Final Acumulado: ${res['cantidad_nueva_compuesta']:,.2f}\n")
                txt_resultado.insert(tk.END, f"• Intereses Ganados: ${res['intereses_ganados']:,.2f}\n")
            except ErrorFinancieroApp as e:
                messagebox.showerror("Error de Aplicación", str(e))

        ttk.Button(tab, text="Calcular Proyección", command=calcular).pack(pady=10)
        txt_resultado.pack(padx=15, pady=5, fill="both", expand=True)

    def _crear_pestana_retiro(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Retiro y Libertad Financiera")
        
        ttk.Label(tab, text="Estimación de Fondo Necesario para Retiro", font=("Helvetica", 12, "bold")).pack(pady=10)
        
        frame = ttk.LabelFrame(tab, text=" Datos del Retiro ")
        frame.pack(fill="x", padx=15, pady=5)
        
        ttk.Label(frame, text="Retiro Mensual Deseado ($):").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        ent_retiro = ttk.Entry(frame)
        ent_retiro.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame, text="Rendimiento Anual Estimado (decimal, ej 0.07):").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        ent_rend = ttk.Entry(frame)
        ent_rend.grid(row=1, column=1, padx=5, pady=5)
        
        txt_resultado = tk.Text(tab, height=8, width=70)
        
        def calcular():
            txt_resultado.delete("1.0", tk.END)
            try:
                res = cu_calcular_fondo_necesario(
                    retiro_mensual_deseado=ent_retiro.get(),
                    rendimiento_anual=ent_rend.get()
                )
                txt_resultado.insert(tk.END, f"=== ANÁLISIS DE FONDO PARA RETIRO ===\n")
                txt_resultado.insert(tk.END, f"• Regla del 4%: ${res['fondo_4porciento']:,.2f}\n")
                if res['fondo_preciso'] is not None:
                    txt_resultado.insert(tk.END, f"• Fondo Ajustado a Rendimiento: ${res['fondo_preciso']:,.2f}\n")
            except ErrorFinancieroApp as e:
                messagebox.showerror("Error de Aplicación", str(e))

        ttk.Button(tab, text="Calcular Fondo", command=calcular).pack(pady=10)
        txt_resultado.pack(padx=15, pady=5, fill="both", expand=True)

    def _crear_pestana_amortizacion(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Tabla Amortización")
        
        ttk.Label(tab, text="Simulador de Tabla de Amortización", font=("Helvetica", 12, "bold")).pack(pady=10)
        
        frame = ttk.LabelFrame(tab, text=" Parámetros de Crédito ")
        frame.pack(fill="x", padx=15, pady=5)
        
        ttk.Label(frame, text="Balance Inicial ($):").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        ent_balance = ttk.Entry(frame)
        ent_balance.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame, text="Tasa Anual (%):").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        ent_tasa = ttk.Entry(frame)
        ent_tasa.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(frame, text="Pago Fijo Mensual ($):").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        ent_pago = ttk.Entry(frame)
        ent_pago.grid(row=2, column=1, padx=5, pady=5)
        
        txt_resultado = tk.Text(tab, height=10, width=70)
        
        def calcular():
            txt_resultado.delete("1.0", tk.END)
            try:
                res = cu_calcular_tabla_amortizacion(
                    balance_inicial=ent_balance.get(),
                    tasa_anual=ent_tasa.get(),
                    cargo_recurrente=0,
                    pago_fijo=ent_pago.get(),
                    meses_mostrar=12
                )
                txt_resultado.insert(tk.END, f"Mes | Bal. Inicial | Interés | Pago | Bal. Final\n")
                txt_resultado.insert(tk.END, "-"*55 + "\n")
                for fila in res["tabla"]:
                    txt_resultado.insert(
                        tk.END, 
                        f"{fila['mes']:3d} | ${fila['balance_inicial']:10.2f} | ${fila['interes']:7.2f} | ${fila['pago_total']:7.2f} | ${fila['balance_final']:10.2f}\n"
                    )
                txt_resultado.insert(tk.END, "-"*55 + "\n")
                txt_resultado.insert(tk.END, f"Total Intereses: ${res['total_intereses']:,.2f} | Total Pagado: ${res['total_pagos']:,.2f}\n")
            except ErrorFinancieroApp as e:
                messagebox.showerror("Error de Aplicación", str(e))

        ttk.Button(tab, text="Generar Tabla", command=calcular).pack(pady=10)
        txt_resultado.pack(padx=15, pady=5, fill="both", expand=True)

if __name__ == "__main__":
    app = AthenaGUI()
    app.mainloop()