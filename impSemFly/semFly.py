import tkinter as tk
from modelo.clsSprite import clsSprite

# Criar a janela principal
janela = tk.Tk()
janela.title("Design Duff - Sem o dito cujo Flyweight (;")

contador = 0  # Contador global
contador_iteracoes = 0  # Contador global

# Lista para armazenar referências aos sprites
sprites = []

# Canvas para exibir os sprites
canvas = tk.Canvas(janela, width=800, height=500, bg="white")
canvas.pack()

# Label para exibir o contador
mensagem = tk.Label(janela, text="Contador de Imagens: "+str(contador))
mensagem.pack(pady=5)
mensagem1 = tk.Label(janela, text="Contador de Iterações: "+str(contador_iteracoes))
mensagem1.pack(pady=5)

# Variável de controle para alternar o estado do loop
loop_ativo = False

def alternar_loop():
    global loop_ativo
    loop_ativo = not loop_ativo  # Alterna entre True e False
    if loop_ativo:
        botao.config(text="Parar")
        gerar_sprites()
    else:
        botao.config(text="Iniciar")

# Botão para alternar o loop
botao = tk.Button(janela, text="Iniciar", command=alternar_loop)
botao.pack()

# Função para incrementar o contador e atualizar a label
def incrementa(): 
    global contador_iteracoes
    global contador
    contador_iteracoes += 1
    contador += 4
    mensagem1.config(text="Contador de Iterações: "+str(contador_iteracoes))
    mensagem.config(text="Contador de Imagens: "+str(contador))

# Função para gerar sprites enquanto o loop estiver ativo
def gerar_sprites():
    global loop_ativo
    # global contador_iteracoes
    # if contador_iteracoes == 10:
    #     loop_ativo = not loop_ativo        

    if loop_ativo:
        # Criar uma nova instância do sprite
        sprite_obj = clsSprite("./img/peso.png")
        
        x, y = sprite_obj.get_posicao()  # Pega a posição do sprite

        sprite = sprite_obj.get_sprite()  # Pega a imagem convertida para o formato tkinter
        sprites.append(sprite)  # Mantém uma referência ao sprite

        # Adicionar o sprite ao canvas
        canvas.create_image(x, y, image=sprite, anchor="nw")

        mais_peso()

        incrementa()  # Atualiza o contador

        # Faz a função gerar_sprites se repetir a cada 10ms
        canvas.after(10, gerar_sprites)

def mais_peso():
    sprite_obj = clsSprite("./img/ubuntu.png")
    sprites.append(sprite_obj.get_sprite())
    canvas.create_image(sprite_obj.get_posicao(), image=sprite_obj.get_sprite(), anchor="nw")
    
    sprite_obj = clsSprite("./img/cinirin.png")
    sprites.append(sprite_obj.get_sprite())
    canvas.create_image(sprite_obj.get_posicao(), image=sprite_obj.get_sprite(), anchor="nw")
    
    sprite_obj = clsSprite("./img/lactea.png")
    sprites.append(sprite_obj.get_sprite())
    canvas.create_image(sprite_obj.get_posicao(), image=sprite_obj.get_sprite(), anchor="nw")

# Iniciar a aplicação
janela.mainloop()
