import os
import sys
import tkinter as tk

#obter diretório onde o script está localizado
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
#juntando com o caminho 1 nivel acima
sys.path.append(os.path.join(diretorio_atual, ".."))

#importando a classe 'clsContexto' de 'controle'
from controle.clsContexto import clsContexto


if __name__ == "__main__":
    janela = tk.Tk()
    janela.title("Design Patterns - Flyweight")
    
    # Cria a instância de clsContexto e passa a janela
    contexto = clsContexto(janela)  
    
    # Inicia o loop principal do Tkinter
    janela.mainloop()
