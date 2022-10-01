import tkinter as t

config = []
class Tela(t.Frame):
    def __init__(self, parent, nome, content):
        t.Frame.__init__(self, parent)
        self.nome = nome
        self.content = content
        t.Label(self, text=self.nome).grid(column=0, row=0, padx=110, pady=5)
        for (index, content) in enumerate(self.content):
            if( content['type'] == 'label' ):
                label = t.Label(self, text=content['text'])
                label.grid(column=content['column'], row=content['row'], padx=110, pady=5)
            elif( content['type'] == 'button' ):
                botao = t.Button(self, text=content['text'], command=content['action'])
                botao.grid(column=content['column'], row=content['row'], padx=110, pady=5)
            