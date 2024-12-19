import tkinter as tk   
import random
from modelo.clsCanva import clsCanva  # Importa a classe concreta que implementa a interface
from modelo.clsFabricaSprite import clsFabricaSprite
class clsContexto:
    def __init__(self, janela):
        #Controles
        self.FabricaSprite = clsFabricaSprite()  #criando uma instância da fábrica de sprites
        self.contador_iteracoes = 0
        self.contador = 0
        self.loop_ativo = False #controle do botao de controle
        #Elementos da tela
        self.janela = janela
        self.canvas = clsCanva(self.janela).criar_canvas()  #criando o canvas através da classe concreta
        self.mensagem = tk.Label(janela, text="Contador de Imagens: "+str(self.contador))
        self.mensagem.pack(pady=5)
        self.mensagem1 = tk.Label(janela, text="Contador de Iterações: "+str(self.contador_iteracoes))
        self.mensagem1.pack(pady=5)
        self.botao = self.criar_botao() #criar o botão de controle
    
    def incrementa(self):
        self.contador+=4 
        self.contador_iteracoes+=1 
        self.mensagem1.config(text="Contador de Iterações: "+str(self.contador_iteracoes))
        self.mensagem.config(text="Contador de Imagens: "+str(self.contador))
    
    def gerar_sprites(self):
        """Gerar sprites enquanto o loop estiver ativo"""
        if self.loop_ativo:
            intrinsic_state = "../img/cinirin.png"  # Caminho da imagem shared state(estado compartilhado)
            extrinsic_x, extrinsic_y =  random.randint(0, 1200), random.randint(0, 600) #posições aleatórias para o sprite
            #O PULO DO GATO TA AQUI
            sprite = self.FabricaSprite.get_Sprites(intrinsic_state)  #obtém ou cria o sprite da fábrica
            
            #cria a imagem no canvas unindo a parte intrinseca(compartilahada), com a parte extrinseca(particular)
            self.canvas.create_image(extrinsic_x, extrinsic_y, image=sprite.get_sprite())  
            
            self.mais_pesos()
            
            self.incrementa()#incrementa os contadores

            self.canvas.after(10, self.gerar_sprites)
    
    def criar_botao(self):
        """Criar e retornar o botão que alterna o loop"""
        botao = tk.Button(self.janela, text="Iniciar", command=self.alternar_loop)
        botao.pack()
        return botao
    
    def alternar_loop(self):
        """Alternar o estado do loop e gerar sprites"""
        self.loop_ativo = not self.loop_ativo  # Alterna entre True e False
        
        if self.loop_ativo:
            self.botao.config(text="Parar")
            self.gerar_sprites()
        else:
            self.botao.config(text="Iniciar")
    
    def mais_pesos(self):
        intrinsic_state2 = "../img/peso.png"
        intrinsic_state3 = "../img/ubuntu.png"  # Caminho da imagem shared state(estado compartilhasdi)
        intrinsic_state4 = "../img/lactea.png"  # Caminho da imagem shared state(estado compartilhasdi)
        
        sprite2 = self.FabricaSprite.get_Sprites(intrinsic_state2)
        sprite3 = self.FabricaSprite.get_Sprites(intrinsic_state3)  # Obtém ou cria o sprite da fábrica
        sprite4 = self.FabricaSprite.get_Sprites(intrinsic_state4)
        
        self.canvas.create_image(random.randint(0, 1200), random.randint(0, 600), image=sprite2.get_sprite())  # Cria a imagem no canvas
        self.canvas.create_image(random.randint(0, 1200), random.randint(0, 600), image=sprite3.get_sprite())
        self.canvas.create_image(random.randint(0, 1200), random.randint(0, 600), image=sprite4.get_sprite())  # Cria a imagem no canvas