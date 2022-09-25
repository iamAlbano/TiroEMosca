import functools
import tkinter as t
import sys

class Menu(t.Frame):
    def __init__(self, parent, *subtelas):
        t.Frame.__init__(self, parent)
        self.current_frame = self
        t.Label(self, text="Tiro e mosca!").grid(column=0, row=0, padx=50, pady=15)
        for (index, subtela) in enumerate(subtelas):
            t.Button(self, text=subtela.nome, command=functools.partial(self.muda_tela, subtela)).grid(column=0, row=index+1, padx=150, pady=10)
            t.Button(subtela, text='Voltar', command=functools.partial(self.muda_tela, self)).grid(column=0, row=len(subtela.content)+1, padx=50, pady=10)
        t.Button( self, text='Sair', command=sys.exit ).grid(column=0, row=len(subtelas)+1, padx=50, pady=10)


    def muda_tela(self, qual):
        self.current_frame.grid_forget()
        qual.grid(column=0, row=0, padx=20, pady=20)
        self.current_frame = qual
    