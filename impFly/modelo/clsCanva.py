import tkinter as tk
class clsCanva():
    def __init__(self, janela):
        self.janela = janela
    
    def criar_canvas(self):
        """Criar e retornar o canvas"""
        canvas = tk.Canvas(self.janela, width=1200, height=600, bg="black")
        canvas.pack()
        return canvas