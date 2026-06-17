import tkinter as tk
from tkinter import messagebox
import os
import sys

from gerador_senhas import gerar_senha


# Caminho do logo
pasta_atual = os.path.dirname(os.path.abspath(sys.argv[0]))
caminho_logo = os.path.join(pasta_atual, "assets", "logo.png")


def gerar():
    tamanho = slider_tamanho.get()
    senha = gerar_senha(
        tamanho,
        var_numeros.get(),
        var_especiais.get()
    )

    entry_senha.delete(0, tk.END)
    entry_senha.insert(0, senha)


def copiar():
    senha = entry_senha.get()

    if not senha:
        messagebox.showwarning("Aviso", "Gere uma senha primeiro.")
        return

    janela.clipboard_clear()
    janela.clipboard_append(senha)

    messagebox.showinfo("Sucesso", "Senha copiada!")


# Janela
janela = tk.Tk()
janela.title("Key Forge")
janela.geometry("420x550")
janela.resizable(False, False)

# Título
tk.Label(janela, text="Key Forge", font=("Segoe UI", 18, "bold")).pack(pady=15)

# Logo
if os.path.exists(caminho_logo):
    img = tk.PhotoImage(file=caminho_logo)
    lbl = tk.Label(janela, image=img)
    lbl.image = img
    lbl.pack()

# Frame opções
frame = tk.LabelFrame(janela, text="Opções")
frame.pack(pady=10, padx=20, fill="x")

tk.Label(frame, text="Tamanho da senha").pack()

slider_tamanho = tk.Scale(frame, from_=6, to=64, orient="horizontal")
slider_tamanho.set(16)
slider_tamanho.pack()

var_numeros = tk.BooleanVar(value=True)
tk.Checkbutton(frame, text="Incluir números", variable=var_numeros).pack(anchor="w")

var_especiais = tk.BooleanVar(value=True)
tk.Checkbutton(frame, text="Incluir especiais", variable=var_especiais).pack(anchor="w")

# Botão gerar
tk.Button(janela, text="Gerar Senha", command=gerar, bg="blue", fg="white").pack(pady=10)

# Entrada senha
entry_senha = tk.Entry(janela, font=("Consolas", 14), justify="center")
entry_senha.pack(pady=5)

# Botão copiar
tk.Button(janela, text="Copiar", command=copiar).pack(pady=5)

janela.mainloop()