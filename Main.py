import random

sala = 1
interacoes = 0
while (interacoes < 7 and sala != 9):
    interacoes += 1
    if sala == 6:
        print('Você está na sala 6, aqui há somente um caminho.\n')
        caminho = int(input('[2] - Caminho preto\n'))
        sala += caminho
    elif sala == 10:
        print('Você entrou em um portal, e foi jogado em uma sala aleatória.')
        sala = random.randint(1,5)
    else:
        print('Você está na sala {}.'.format(sala))
        caminho = int(input('[1] - Caminho vermelho\n[2] - Caminho preto\n'))
        sala += caminho

if(sala == 9):
    print('Parabéns, você venceu a Dungeon!')
elif(interacoes == 7):
    print('Sinto muito, você perdeu o jogo :(')