import tkinter as tk
from tkinter import messagebox

# Função para calcular o frete
def calcular_frete():
    try:
        peso = float(entry_peso.get())
        distancia = float(entry_distancia.get())

        if peso <= 0 or distancia <= 0:
            messagebox.showerror("Erro","Os valores devem ser maiores que zero.")
            return
        
        # Simulação : valor base + taxa por km + taxa por kg
        valor_base = 10.00
        taxa_por_km = 0.05 # R$ 0,05 por Km
        taxa_por_kg = 1.50 # R$1,50 por kg

        custo = valor_base + (distancia * taxa_por_km) + (peso * taxa_por_kg)

        label_resultado.config(
            text=f"Frete estimado: R$ {custo:.2f}"
        )

    except ValueError:
        messagebox.showerror("Error", "Digite valores numéricos válidos.")

# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora de Frete")
janela.geometry("300x250")
janela.resizable(False, False)

# Título
titulo = tk.Label(janela, text="Calculadora de Frete", font=("Arial", 14, "bold"))
titulo.pack(pady=10)

# Peso
frame_peso = tk.Frame(janela)
frame_peso.pack(pady=5)
tk.Label(frame_peso, text="Peso (kg): ").grid(row=0, column=0, padx=5)
entry_peso = tk.Entry(frame_peso, width=10)
entry_peso.grid(row=0, column=1)

# Distância
frame_distancia = tk.Frame(janela)
frame_distancia.pack(pady=5)
tk.Label(frame_distancia, text="Distância (km):").grid(row=0, column=0, padx=5)
entry_distancia = tk.Entry(frame_distancia, width=10)
entry_distancia.grid(row=0, column=1)

# Botão de Cálculo
btn_calcular = tk.Button(
    janela, text="Calcular", command=calcular_frete,
    bg="#4caf50", fg="white", width=12
)
btn_calcular.pack(pady=10)

# Resultado
label_resultado = tk.Label(janela, text="", font=("Arial", 12))
label_resultado.pack(pady=10)

# Rodar o App
janela.mainloop()