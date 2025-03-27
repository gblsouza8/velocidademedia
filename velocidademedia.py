def __init__():
    distancia = int(input("Insira a distância percorrida (em km): "))
    tempo = int(input("Insira o tempo gasto (em h): "))
    velocidadeMedia = distancia / tempo
    print("A sua velocidade média nesse percurso foi: ", velocidadeMedia, " km/h")
    rodarNovamente()
    
def rodarNovamente():
    escolha = input("Deseja calcular outra velocidade média?\nSim: Aperte um.\nNão: Aperta qualquer outra coisa.\n")
    if (escolha == 1):
        __init__()
    else:
        exit
    
__init__()