import tkinter as tk

window = tk.Tk()

label = tk.Label(window, text="Meu primeiro Texto!!!")
label.pack()

window.mainloop()

mensagem = tk.Label(
    text="Olá Mundo",
    foreground='green',
    background='blue',
    width=10,
    height=10
)

mensagem.pack()
