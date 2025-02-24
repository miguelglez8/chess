import matplotlib.pyplot as plt # importamos la librería externa Matplotlib para dibujar gráficos de la partida

# FUNCIÓN QUE SE UTILIZA EN EL MÓDULO AJEDREZ PARA DIBUJAR UN GRÁFICO, CON LOS PUNTOS DEL GANADOR DE LA PARTIDA EN CADA JUGADA

def grafica(l):
    """Se le pasa una lista con los puntos del jugador y crea una gráfica con los puntos por turno"""
    plt.plot(l)
    plt.ylabel('puntos')
    plt.xlabel('turno')
    plt.show()
