from modelo.clsSprite import clsSprite
class clsFabricaSprite(clsSprite):
    def __init__(self):
        self.sprites = {}  # Dicionário para armazenar sprites criados, pool de flyweigts

    def get_Sprites(self, chave):
        if chave not in self.sprites:
            self.sprites[chave] = clsSprite(chave)  # Cria o sprite se não existir 
        return self.sprites[chave]  # Retorna o sprite existente