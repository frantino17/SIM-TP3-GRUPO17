import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import numpy as np
import threading

class SimulationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Simulación de Modelos")
        
        # Crear pestañas
        self.notebook = ttk.Notebook(master)
        self.agencia_frame = ttk.Frame(self.notebook)
        self.venta_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.agencia_frame, text="Agencia de Autos")
        self.notebook.add(self.venta_frame, text="Venta Callejera")
        self.notebook.pack(expand=True, fill='both')
        
        # Configurar widgets para Agencia de Autos
        self.setup_agencia_tab()
        self.setup_venta_tab()
    
    def setup_agencia_tab(self):
        frame = self.agencia_frame
        
        # Campos de entrada
        ttk.Label(frame, text="Número de semanas (n):").grid(row=0, column=0, padx=5, pady=5)
        self.agencia_n = ttk.Entry(frame)
        self.agencia_n.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame, text="Umbral de comisión (y):").grid(row=1, column=0, padx=5, pady=5)
        self.agencia_y = ttk.Entry(frame)
        self.agencia_y.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(frame, text="Fila inicial (j):").grid(row=2, column=0, padx=5, pady=5)
        self.agencia_j = ttk.Entry(frame)
        self.agencia_j.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(frame, text="Número de filas (i):").grid(row=3, column=0, padx=5, pady=5)
        self.agencia_i = ttk.Entry(frame)
        self.agencia_i.grid(row=3, column=1, padx=5, pady=5)
        
        # Botón de simulación
        self.simular_agencia_btn = ttk.Button(frame, text="Simular", command=self.run_agencia_simulation)
        self.simular_agencia_btn.grid(row=4, column=0, columnspan=2, pady=10)
        
        # Resultados
        self.agencia_resultados = ttk.LabelFrame(frame, text="Resultados")
        self.agencia_resultados.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky='ew')
        
        ttk.Label(self.agencia_resultados, text="Comisión promedio:").grid(row=0, column=0)
        self.agencia_promedio = ttk.Label(self.agencia_resultados, text="")
        self.agencia_promedio.grid(row=0, column=1)
        
        ttk.Label(self.agencia_resultados, text="Probabilidad > y:").grid(row=1, column=0)
        self.agencia_probabilidad = ttk.Label(self.agencia_resultados, text="")
        self.agencia_probabilidad.grid(row=1, column=1)
        
        # Tabla de estado
        self.agencia_tabla = ttk.Treeview(self.agencia_resultados, columns=('Semana', 'Vendedor 1', 'Vendedor 2', 'Vendedor 3', 'Vendedor 4'), show='headings')
        self.agencia_tabla.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        
    def setup_venta_tab(self):
        frame = self.venta_frame
        
        # Campos de entrada
        ttk.Label(frame, text="Número de días (N):").grid(row=0, column=0, padx=5, pady=5)
        self.venta_n = ttk.Entry(frame)
        self.venta_n.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame, text="Fila inicial (j):").grid(row=1, column=0, padx=5, pady=5)
        self.venta_j = ttk.Entry(frame)
        self.venta_j.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(frame, text="Número de filas (i):").grid(row=2, column=0, padx=5, pady=5)
        self.venta_i = ttk.Entry(frame)
        self.venta_i.grid(row=2, column=1, padx=5, pady=5)
        
        # Botón de simulación
        self.simular_venta_btn = ttk.Button(frame, text="Simular", command=self.run_venta_simulation)
        self.simular_venta_btn.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Resultados
        self.venta_resultados = ttk.LabelFrame(frame, text="Resultados")
        self.venta_resultados.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky='ew')
        
        ttk.Label(self.venta_resultados, text="Sobrantes promedio:").grid(row=0, column=0)
        self.venta_sobrantes = ttk.Label(self.venta_resultados, text="")
        self.venta_sobrantes.grid(row=0, column=1)
        
        ttk.Label(self.venta_resultados, text="Utilidad promedio:").grid(row=1, column=0)
        self.venta_utilidad = ttk.Label(self.venta_resultados, text="")
        self.venta_utilidad.grid(row=1, column=1)
        
        # Tabla de estado
        self.venta_tabla = ttk.Treeview(self.venta_resultados, columns=('Día', 'Clientes', 'Demanda', 'Sobrantes', 'Utilidad'), show='headings')
        self.venta_tabla.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    
    def run_agencia_simulation(self):
        try:
            n = int(self.agencia_n.get())
            y = float(self.agencia_y.get())
            j = int(self.agencia_j.get())
            i = int(self.agencia_i.get())
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")
            return
        
        if j + i > n:
            messagebox.showerror("Error", "j + i no debe exceder el número de semanas.")
            return
        
        # Deshabilitar botón durante simulación
        self.simular_agencia_btn.config(state='disabled')
        threading.Thread(target=self.simular_agencia, args=(n, y, j, i)).start()
    
    def simular_agencia(self, n, y, j, i):
        total_comision = 0
        count_above = 0
        state_rows = []
        last_row = None
        
        for semana in range(n):
            comisiones = []
            for _ in range(4):  # 4 vendedores
                autos = np.random.choice([0,1,2,3,4], p=[0.2,0.3,0.3,0.15,0.05])
                comision = 0
                for _ in range(autos):
                    tipo = np.random.choice(['compacto','mediano','lujo'], p=[0.5,0.35,0.15])
                    if tipo == 'compacto':
                        comision += 250
                    elif tipo == 'mediano':
                        comision += np.random.choice([400,500], p=[0.4,0.6])
                    else:
                        comision += np.random.choice([1000,1500,2000], p=[0.35,0.4,0.25])
                comisiones.append(comision)
                total_comision += comision
                if comision > y:
                    count_above +=1
            
            # Guardar filas requeridas
            if j <= semana < j + i:
                state_rows.append((semana, comisiones))
            if semana == n -1:
                last_row = (semana, comisiones)
        
        promedio = total_comision / (4 * n)
        probabilidad = count_above / (4 * n)
        
        # Actualizar GUI
        self.master.after(0, self.update_agencia_results, promedio, probabilidad, state_rows, last_row)
        self.master.after(0, lambda: self.simular_agencia_btn.config(state='normal'))
    
    def update_agencia_results(self, promedio, probabilidad, state_rows, last_row):
        self.agencia_promedio.config(text=f"${promedio:.2f}")
        self.agencia_probabilidad.config(text=f"{probabilidad*100:.2f}%")
        
        # Limpiar tabla
        for row in self.agencia_tabla.get_children():
            self.agencia_tabla.delete(row)
        
        # Agregar filas de estado
        for semana, comisiones in state_rows:
            self.agencia_tabla.insert('', 'end', values=(semana, *comisiones))
        
        # Agregar última fila
        if last_row:
            self.agencia_tabla.insert('', 'end', values=(last_row[0], *last_row[1]), tags=('last',))
    
    def run_venta_simulation(self):
        try:
            n = int(self.venta_n.get())
            j = int(self.venta_j.get())
            i = int(self.venta_i.get())
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")
            return
        
        if j + i > n:
            messagebox.showerror("Error", "j + i no debe exceder el número de días.")
            return
        
        self.simular_venta_btn.config(state='disabled')
        threading.Thread(target=self.simular_venta, args=(n, j, i)).start()
    
    def simular_venta(self, n, j, i):
        total_sobrantes = 0
        total_utilidad = 0
        state_rows = []
        last_row = None
        
        for dia in range(n):
            clientes = np.random.randint(10, 31)
            demanda_total = 0
            ingreso = 0
            
            for _ in range(clientes):
                demanda = np.random.choice([1,2,5,6,7,8,10], p=[0.1,0.2,0.4,0.1,0.1,0.05,0.05])
                precio = 100 if demanda in [1,2,5] else 80
                demanda_total += demanda
                ingreso += demanda * precio
            
            if demanda_total > 200:
                sobrantes = 0
                vendidos = 200
            else:
                sobrantes = 200 - demanda_total
                vendidos = demanda_total
            
            costo = 200 * 30
            utilidad = ingreso - costo
            
            total_sobrantes += sobrantes
            total_utilidad += utilidad
            
            if j <= dia < j + i:
                state_rows.append((dia, clientes, demanda_total, sobrantes, utilidad))
            if dia == n -1:
                last_row = (dia, clientes, demanda_total, sobrantes, utilidad)
        
        avg_sobrantes = total_sobrantes / n
        avg_utilidad = total_utilidad / n
        
        self.master.after(0, self.update_venta_results, avg_sobrantes, avg_utilidad, state_rows, last_row)
        self.master.after(0, lambda: self.simular_venta_btn.config(state='normal'))
    
    def update_venta_results(self, sobrantes, utilidad, state_rows, last_row):
        self.venta_sobrantes.config(text=f"{sobrantes:.2f}")
        self.venta_utilidad.config(text=f"${utilidad:.2f}")
        
        for row in self.venta_tabla.get_children():
            self.venta_tabla.delete(row)
        
        for fila in state_rows:
            self.venta_tabla.insert('', 'end', values=fila)
        
        if last_row:
            self.venta_tabla.insert('', 'end', values=last_row, tags=('last',))

if __name__ == "__main__":
    root = tk.Tk()
    app = SimulationApp(root)
    root.mainloop()
