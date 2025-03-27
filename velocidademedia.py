def __init__():
    distancia = int(input("Insira a distância percorrida (em km): "))
    tempo = int(input("Insira o tempo gasto (em h): "))
    velocidadeMedia = distancia / tempo
    print("A sua velocidade média nesse percurso foi: ", velocidadeMedia, " km/h")

    
__init__()