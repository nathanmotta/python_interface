import tkinter as tk
from tkinter import messagebox


def sair():
    print("Saindo")
    exit(0)


def exibe():
    nome = entrada.get()
    print(nome)
    messagebox.showinfo("Seu nome:", nome)


def teste():
    print("Segunda função")
    messagebox.showinfo("Função 2", "Duas funções chamadas em sequência")


tela = tk.Tk()
tela.title("Menu")
frame = tk.Frame(tela, width=50)

entrada = tk.Entry(fg='yellow', bg='blue')
botao_sair = tk.Button(tela, text="SAIR", command=sair)
botao_exibe = tk.Button(tela, text="Exibe", command=exibe)
botao_exibe_2 = tk.Button(tela, text="Chama 2 Funções",
                          command=lambda: [exibe(), teste()])

mensagem = tk.Label(
    text="Olá Mundo",
    foreground='green',
    background='black',
    width=10,
    height=10,
)

mensagem.pack()
botao_exibe.pack()
botao_exibe_2.pack()
botao_sair.pack()
frame.pack()
entrada.pack()

tela.mainloop()
