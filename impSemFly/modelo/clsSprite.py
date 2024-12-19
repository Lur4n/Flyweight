from PIL import Image, ImageTk
import random

class clsSprite:
    def __init__(self, sprite_path):
        # Gera posições aleatórias
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)
        self.imagem = Image.open(sprite_path)#carregando a imagem a partir de um path
        self.imagem = self.imagem.resize((75, 75))#definindo o tamanho da imagem
        self.sprite = ImageTk.PhotoImage(self.imagem)#convertendo para um formato compatível com tkinter

    def get_sprite(self):
        return self.sprite  #retornando a imagem convertida para o formato tkinter

    def get_posicao(self):
        return self.x, self.y #retornando a posição do sprite

    