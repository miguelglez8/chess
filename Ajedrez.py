from Fichas import *
from tablaDePuntos import *
from Partida import *
from random import * # importamos random, para generar números aleatorios, que en la práctica generarán movimientos aleatorios
                     # del equipo controlado por la CPU (ya sea el equipo negro o el equipo blanco)

# ESTE ES UN PROGRAMA PRINCIPAL PARA JUGAR AL AJEDREZ, AL QUE AL PRINCIPIO, SE LE PEDIRÁ AL ANFITRIÓN POR TECLADO EL NOMBRE DEL EQUIPO
# CON EL QUE QUIERE JUGAR (BLANCO O NEGRO)

jugador1=[39] # puntos iniciales del jugador del equipo negro
jugador2=[39] # puntos iniciales del jugador del equipo blanco
ganaBlanco=False
ganaNegro=False
ronda=0
print("BIENVENIDO A LA PARTIDA DE AJEDREZ...")
l=crearTableroInicial()
color=str(input("Introduce color con que quieres jugar ('Blanco' o 'Negro'): ")) # introduce el color con el que quieres jugar, el otro será controlado por la CPU
color=color.lower()
while color!="negro" and color!="blanco":
    print("Color introducido erróneo, introduzca Blanco o Negro")
    color=str(input("Introduce color con que quieres jugar ('Blanco' o 'Negro'): "))
    color=color.lower()
if color=="negro":
    while ganaBlanco==False or ganaNegro==False:
        ronda=ronda+1
        copiaTabla=copiaTablero(l)
        turno=comprobarTablero(l,copiaTabla)
        while turno==False:
            xB=randint(0,7) # generamos número aleatorio entre [0,7], esta es la posición del eje x de la ficha elegida aleatoriamente
            yB=randint(0,7) # generamos número aleatorio entre [0,7], esta es la posición del eje y de la ficha elegida aleatoriamente
            iB=randint(0,7) # generamos número aleatorio entre [0,7], esta es la posición del eje x donde la CPU va a mover la ficha elegida aleatoriamente
            jB=randint(0,7) # generamos número aleatorio entre [0,7], esta es la posición del eje x donde la CPU va a mover la ficha elegida aleatoriamente
            condition1=comprobarFichaBlanca(l,xB,yB)
            condition2=comprobarFichaBlanca(l,iB,jB)
            while xB==iB and yB==jB: # mientras la ficha no haya hecho un movimiento no sale del bucle
                xB=randint(0,7) # generamos número aleatorio entre [0,7], esta es la posición del eje x de la ficha elegida aleatoriamente
                yB=randint(0,7) # generamos número aleatorio entre [0,7], esta es la posición del eje y de la ficha elegida aleatoriamente
                iB=randint(0,7) # generamos número aleatorio entre [0,7], esta es la posición del eje x donde la CPU va a mover la ficha elegida aleatoriamente
                jB=randint(0,7) # generamos número aleatorio entre [0,7], esta es la posición del eje x donde la CPU va a mover la ficha elegida aleatoriamente
            while condition1==condition2:
                xB=randint(0,7) # generamos número aleatorio entre [0,7], esta es la posición del eje x de la ficha elegida aleatoriamente
                yB=randint(0,7) # generamos número aleatorio entre [0,7], esta es la posición del eje y de la ficha elegida aleatoriamente
                iB=randint(0,7) # generamos número aleatorio entre [0,7], esta es la posición del eje x donde la CPU va a mover la ficha elegida aleatoriamente
                jB=randint(0,7) # generamos número aleatorio entre [0,7], esta es la posición del eje x donde la CPU va a mover la ficha elegida aleatoriamente
                while xB==iB and yB==jB: # mientras la ficha no haya hecho un movimiento no sale del bucle
                    xB=randint(0,7) # generamos número aleatorio entre [0,7], esta es la posición del eje x de la ficha elegida aleatoriamente
                    yB=randint(0,7) # generamos número aleatorio entre [0,7], esta es la posición del eje y de la ficha elegida aleatoriamente
                    iB=randint(0,7) # generamos número aleatorio entre [0,7], esta es la posición del eje x donde la CPU va a mover la ficha elegida aleatoriamente
                    jB=randint(0,7) # generamos número aleatorio entre [0,7], esta es la posición del eje x donde la CPU va a mover la ficha elegida aleatoriamente
                condition2=comprobarFichaBlanca(l,iB,jB)
                condition1=comprobarFichaBlanca(l,xB,yB)
            moverFichaCPU(l,xB,yB,iB,jB) # la CPU mueve la ficha aleatoria a la posición aleatoria (siempre que las reglas del juego lo permitan)
            turno=comprobarTablero(l,copiaTabla)
        ganaBlanco=jaqueMateBlancoANegro(l)
        copiaTabla=copiaTablero(l)
        turno=comprobarTablero(l,copiaTabla)
        print()
        print("RONDA "+str(ronda)+":")
        print("--------TABLERO--------")
        escribirTablero(l)
        print("--------TABLERO--------")
        while turno==False:
            condition3=False
            condition4=comprobarTablero(l,copiaTabla)
            while condition4==False and condition3==False:
                xN=int(input("Posición x de tu ficha: "))
                yN=int(input("Posición y de tu ficha: "))
                iN=int(input("Posición x a donde quieras llevar tu ficha: "))
                jN=int(input("Posición y a donde quieras llevar tu ficha: "))
                while jN>7 or iN>7 or jN<0 or iN<0:
                    iN=int(input("Posición x a donde quieras llevar tu ficha: "))
                    jN=int(input("Posición y a donde quieras llevar tu ficha: "))
                while yN>7 or xN>7 or yN<0 or xN<0:
                    xN=int(input("Posición x de tu ficha: "))
                    yN=int(input("Posición y de tu ficha: "))
                condition3=comprobarFichaNegra(l,xN,yN)
                if condition3==True:
                    moverFicha(l,xN,yN,iN,jN) # el anfitrión mueve la ficha a la posición (siempre que las reglas del juego lo permitan)
                condition4=comprobarTablero(l,copiaTabla)
            turno=comprobarTablero(l,copiaTabla)
        ganaNegro=jaqueMateNegroABlanco(l)
        ganadorMomentaneoPartida(l,ronda) # generamos fichero
        valorFichas(l,ronda) # generamos fichero
        jugador1.append(contarPuntuacion(l,"EQUIPO NEGRO"))
        jugador2.append(contarPuntuacion(l,"EQUIPO BLANCO"))
        if ganaNegro==True:
            print()
            print("RONDA "+str(ronda)+":")
            print("--------TABLERO--------")
            escribirTablero(l)
            print("--------TABLERO--------")
            print("El equipo NEGRO ha ganado la partida") # el equipo negro gana
            print()
            grafica(jugador1) # dibuja la gráfica del equipo negro
            break # abandonamos el bucle, la partida ha finalizado
        elif ganaBlanco==True:
            print()
            print("RONDA "+str(ronda)+":")
            print("--------TABLERO--------")
            escribirTablero(l)
            print("--------TABLERO--------")
            print("El equipo BLANCO ha ganado la partida") # el equipo blanco gana
            print()
            grafica(jugador2) # dibuja la gráfica del equipo blanco
            break # abandonamos el bucle, la partida ha finalizado
    print("PUNTOS DE CADA JUGADOR EN CADA JUGADA:")
    print()
    lecturaInformacionFichero("valorFichas.txt") # leemos el fichero en el que se ha escrito el ganador de cada jugada de la partida
    print("GANADOR DE CADA JUGADA POR LÍNEAS:")
    print()
    lecturaInformacionFichero("ganadorMomentaneoPartida.txt") # leemos el fichero en el que se ha escrito la puntuación de las fichas de cada equipo por turnos

elif color=="blanco":
    while ganaNegro==False or ganaBlanco==False:
        copiaTabla=copiaTablero(l)
        ronda=ronda+1
        copiaTabla=copiaTablero(l)
        turno=comprobarTablero(l,copiaTabla)
        print()
        print("RONDA "+str(ronda)+":")
        print("--------TABLERO--------")
        escribirTablero(l)
        print("--------TABLERO--------")
        while turno==False:
            condition3=False
            condition4=comprobarTablero(l,copiaTabla)
            while condition4==False and condition3==False:
                xB=int(input("Posición x de tu ficha: "))
                yB=int(input("Posición y de tu ficha: "))
                iB=int(input("Posición x a donde quieras llevar tu ficha: "))
                jB=int(input("Posición y a donde quieras llevar tu ficha: "))
                while jB>7 or iB>7 or jB<0 or iB<0:
                    iB=int(input("Posición x a donde quieras llevar tu ficha: "))
                    jB=int(input("Posición y a donde quieras llevar tu ficha: "))
                while yB>7 or xB>7 or yB<0 or xB<0:
                    xB=int(input("Posición x de tu ficha: "))
                    yB=int(input("Posición y de tu ficha: "))
                condition3=comprobarFichaBlanca(l,xB,yB)
                if condition3==True:
                    moverFicha(l,xB,yB,iB,jB) # el anfitrión mueve la ficha a la posición (siempre que las reglas del juego lo permitan)
                condition4=comprobarTablero(l,copiaTabla)
            turno=comprobarTablero(l,copiaTabla)
        ganaBlanco=jaqueMateBlancoANegro(l)
        copiaTabla=copiaTablero(l)
        turno=comprobarTablero(l,copiaTabla)
        while turno==False:
            xN=randint(0,7) # generamos número aleatorio entre [0,7], esta es la posición del eje x de la ficha elegida aleatoriamente
            yN=randint(0,7) # generamos número aleatorio entre [0,7], esta es la posición del eje y de la ficha elegida aleatoriamente
            iN=randint(0,7) # generamos número aleatorio entre [0,7], esta es la posición del eje x donde la CPU va a mover la ficha elegida aleatoriamente
            jN=randint(0,7) # generamos número aleatorio entre [0,7], esta es la posición del eje x donde la CPU va a mover la ficha elegida aleatoriamente
            condition1=comprobarFichaNegra(l,xN,yN)
            condition2=comprobarFichaNegra(l,iN,jN)
            while xN==iN and yN==jN: # mientras la ficha no haya hecho un movimiento no sale del bucle
                xN=randint(0,7) # generamos número aleatorio entre [0,7], esta es la posición del eje x de la ficha elegida aleatoriamente
                yN=randint(0,7) # generamos número aleatorio entre [0,7], esta es la posición del eje y de la ficha elegida aleatoriamente
                iN=randint(0,7) # generamos número aleatorio entre [0,7], esta es la posición del eje x donde la CPU va a mover la ficha elegida aleatoriamente
                jN=randint(0,7) # generamos número aleatorio entre [0,7], esta es la posición del eje x donde la CPU va a mover la ficha elegida aleatoriamente
            while condition1==condition2:
                xN=randint(0,7) # generamos número aleatorio entre [0,7], esta es la posición del eje x de la ficha elegida aleatoriamente
                yN=randint(0,7) # generamos número aleatorio entre [0,7], esta es la posición del eje y de la ficha elegida aleatoriamente
                iN=randint(0,7) # generamos número aleatorio entre [0,7], esta es la posición del eje x donde la CPU va a mover la ficha elegida aleatoriamente
                jN=randint(0,7) # generamos número aleatorio entre [0,7], esta es la posición del eje x donde la CPU va a mover la ficha elegida aleatoriamente
                while xN==iN and yN==jN: # mientras la ficha no haya hecho un movimiento no sale del bucle
                    xN=randint(0,7) # generamos número aleatorio entre [0,7], esta es la posición del eje x de la ficha elegida aleatoriamente
                    yN=randint(0,7) # generamos número aleatorio entre [0,7], esta es la posición del eje y de la ficha elegida aleatoriamente
                    iN=randint(0,7) # generamos número aleatorio entre [0,7], esta es la posición del eje x donde la CPU va a mover la ficha elegida aleatoriamente
                    jN=randint(0,7) # generamos número aleatorio entre [0,7], esta es la posición del eje x donde la CPU va a mover la ficha elegida aleatoriamente
                condition2=comprobarFichaNegra(l,iN,jN)
                condition1=comprobarFichaNegra(l,xN,yN)
            moverFichaCPU(l,xN,yN,iN,jN) # la CPU mueve la ficha aleatoria a la posición aleatoria (siempre que las reglas del juego lo permitan)
            turno=comprobarTablero(l,copiaTabla)
        ganaNegro=jaqueMateNegroABlanco(l)
        ganadorMomentaneoPartida(l,ronda) # generamos fichero
        valorFichas(l,ronda) # generamos fichero
        jugador1.append(contarPuntuacion(l,"EQUIPO NEGRO"))
        jugador2.append(contarPuntuacion(l,"EQUIPO BLANCO"))
        if ganaNegro==True:
            print()
            print("RONDA "+str(ronda)+":")
            print("--------TABLERO--------")
            escribirTablero(l)
            print("--------TABLERO--------")
            print("El equipo NEGRO ha ganado la partida") # el equipo negro gana
            print()
            grafica(jugador1) # dibuja la gráfica del equipo negro
            break # abandonamos el bucle, la partida ha finalizado
        elif ganaBlanco==True:
            print()
            print("RONDA "+str(ronda)+":")
            print("--------TABLERO--------")
            escribirTablero(l)
            print("--------TABLERO--------")
            print("El equipo BLANCO ha ganado la partida") # el equipo blanco gana
            print()
            grafica(jugador2) # dibuja la gráfica del equipo blanco
            break # abandonamos el bucle, la partida ha finalizado
    print("PUNTOS DE CADA JUGADOR EN CADA JUGADA:")
    print()
    lecturaInformacionFichero("valorFichas.txt") # leemos el fichero en el que se ha escrito el ganador de cada jugada de la partida
    print("GANADOR DE CADA JUGADA POR LÍNEAS:")
    print()
    lecturaInformacionFichero("ganadorMomentaneoPartida.txt") # leemos el fichero en el que se ha escrito la puntuación de las fichas de cada equipo por turnos
