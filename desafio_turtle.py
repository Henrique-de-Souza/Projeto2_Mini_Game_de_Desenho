from turtle import Turtle 

# Inicializar uma Turtle
t = Turtle()

# definir velocidade
t.speed(1)

# defidindo as direções de movimento e mediante a resposta, sua rotação. 
while True:
    print()
    direção = str(input('Para qual direção devo me movimentar? [F/ T] ')).upper().strip()[0]
    print()

    # Se a direção for para frente:
    if direção =='F':  
        print()
        rotacao = str(input('Devo rotacinar para a direita ou esquerda? [E/ D]\n[N] para não rotacionar] ')).upper().strip()[0]

        # se a rotação for para a Esquerda:
        if rotacao == 'E':
            print()
            graus = int(input('Quantos graus devo rotacionar para a esquerda? '))
            t.left(graus)
            print()
            distancia = int(input('Quantos pixels devo andar nessa direção? '))
            t.forward(distancia)

        # se a rotação for para a Direita:
        elif rotacao == 'D':
            print()
            graus = int(input('Quantos graus devo rotacionar para a direita?'))
            t.left(graus)
            print()
            distancia = int(input('Quantos pixels devo andar nessa direção? '))
            t.forward(distancia)

        # Se não houver rotação:
        elif rotacao == 'N':
            print()
            distancia = int(input('Quantos pixels devo andar nessa direção? '))
            t.forward(distancia)
            t.left(0)
   
   # Se a direção for para Trás:
    if direção == 'T':
        print()
        rotacao = str(input('Devo rotacinar para a direita ou esquerda? [E/ D]\n[N para não rotacionar] ')).upper().strip()[0]

        # Se a rotação por para a Esquerda:
        if rotacao == 'E':
            print()
            graus = int(input('Quantos graus devo rotacionar para a esquerda? '))
            t.left(graus)
            print()
            distancia = int(input('Quantos pixels devo andar nessa direção? '))
            print()
            t.backward(distancia)

        # Se a rotação for para a Direita:
        elif rotacao == 'D':
            print()
            graus = int(input('Quantos graus devo rotacionar para a direita? '))
            t.left(graus)
            print()
            distancia = int(input('Quanto devo andar nessa direção? '))
            print()
            t.backward(distancia)

        # Se não houver rotação:
        elif rotacao == 'N':
            print()
            distancia = int(input('Quantos pixels devo andar nessa direção? '))
            t.backward(distancia)
            t.left(0)

    # Opção de recomeçar o mini-game
    print()
    continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        print()
        break
                