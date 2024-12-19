from PIL import Image, ImageTk
class clsSprite:
    def __init__(self, sprite_path):
        imagem = Image.open(sprite_path)  # Carregando a imagem
        imagem = imagem.resize((6, 6))  # Definindo o tamanho da imagem
        self.sprite = ImageTk.PhotoImage(imagem)  # Convertendo para um formato compatível com tkinter

    def get_sprite(self):
        return self.sprite  # Retorna a imagem convertida para o formato tkinter
