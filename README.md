# TecnicasDeProgramacao202120.00221.01-ProjetoN1
Projeto da atividade N1 da aula de Técnicas de Programação
 O código simula um jogo de RPG, no qual o usuário faz parte de uma guilda que está explorando uma dungeon 
 e o usuário deve digitar um número entre 1 e 2 para que ele possa seguir seu caminho dentro do labirinto, e ele funciona inteiramente no console.

O número 1 leva para o caminho vermelho (ou direita), e o número 2 leva para o caminho preto (ou esquerda). 
Ao escolher o caminho vermelho, é somado um número ao número da sala atual, e ao escolher o caminho preto, é somado dois números.

A sala 6 tem somente uma opção, que é o caminho preto.

Caso o usuário siga o caminho preto na sala 8, ele entrará em um local desconhecido e será levado para qualquer sala entre 1 e 5, 
pois esse local é controlado por criaturas místicas que dominam o espaço-tempo.

A sala que o usuário será levado funciona por meio de uma função de uma biblioteca importada (random). 
Assim é possível gerar um número aleatório após a ação do usuário. 

Se a guilda chegar no número 9, ela ganha o jogo.

Caso a guilda leve 7 interações ou mais para chegar na sala 9, ela perde o jogo (cada vez que a guilda escolhe um caminho, é considerada uma interação).
