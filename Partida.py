# FUNCIÓN QUE CREA EL TABLERO CON TODAS LAS FICHAS AL PRINCIPIO DE LA PARTIDA,
# EL EQUIPO NEGRO LE CORRESPONDRÁ A LA CPU, Y NOSOTROS SIEMPRE JUGAREMOS CON EL EQUIPO BLANCO.

# LAS FICHAS DEL EQUIPO BLANCO SE ENCUENTRAN INICIALMENTEEN LAS POSICIONES DE LAS FILAS 6 Y 7,
# MIENTRAS QUE LAS DEL EQUIPO NEGRO ESTÁN EN LAS FILAS 0 Y 1.

from Fichas import *

def crearTableroInicial():
    """función que crea el tablero de ajedrez con todas las
    fichas del principio de la partida, y lo devuelve"""
    tablero=[]
    for i in range(8):
        tablero.append(["--"]*8) # creamos una matriz que simula a un tablero de ajedrez con 8 filas y 8 columnas, con valor inicial "--" (casilla blanca)
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if i==1:
                tablero[i][j] = "PN" # ponemos el peón negro en la casilla indicada
            elif i==6:
                tablero[i][j] = "PB" # ponemos el peón blanco en la casilla indicada
            elif i==0 and (j==0 or j==7):
                tablero[i][j] = "TN" # ponemos la torre negra en la casilla indicada
            elif  i==7 and (j==0 or j==7):
                tablero[i][j] = "TB" # ponemos la torre blanca en la casilla indicada
            elif i==0 and (j==1 or j==6):
                tablero[i][j] = "CN" # ponemos el caballo negro en la casilla indicada
            elif i==7 and (j==1 or j==6):
                tablero[i][j] = "CB" # ponemos el caballo blanco en la casilla indicada
            elif i==0 and (j==2 or j==5):
                tablero[i][j] = "AN" # ponemos el alfíl negro en la casilla indicada
            elif i==7 and (j==2 or j==5):
                tablero[i][j] = "AB" # ponemos el alfíl blanco en la casilla indicada
            elif i==0 and j==4:
                tablero[i][j] = "RN" # ponemos la dama negra en la casilla indicada
            elif i==7 and j==4:
                tablero[i][j] = "RB" # ponemos la dama blanca en la casilla indicada
            elif i==0 and j==3:
                tablero[i][j] = "DN" # ponemos el rey negro en la casilla indicada
            elif i==7 and j==3:
                tablero[i][j] = "DB" # ponemos el rey blanco en la casilla indicada
            elif (i%2==0 and j%2!=0) or (i%2!=0 and j%2==0):
                tablero[i][j] = "  " # espacios en blanco en la casilla (casilla negra)
    return tablero # devolvemos el tablero inicial de la partida

# ESTA FUNCIÓN NOS SERVIRÁ PARA SABER QUIEN ESTÁ GANANDO LA PARTIDA EN CUALQUIER MOMENTO DE ELLA, IRÁ GANANDO EN LA
# PARTIDA AQUEL EQUIPO CUYO VALOR DE SUS FICHAS SEA SUPERIOR AL OTRO

def contarPuntuacion(tablero,equipo):
    """función que recibe el tablero con las fichas  y el nombre del
    equipo que queremos saber el valor de las fichas y devuelve la suma del valor
    de dicho equipo (sin el valor del rey)"""
    fichas_negro=["PN","TN","CN","AN","DN"]
    fichas_blanco=["PB","TB","CB","AB","DB"]
    count=0
    if equipo == "EQUIPO NEGRO" or equipo == "EN": # elegimos el equipo negro
        for i in range(len(tablero)):
            for j in range(len(tablero[i])): # si encontramos alguna ficha que pertenezca al equipo negro, añadimos su vcalor a la variable count
                if tablero[i][j] == fichas_negro[0]:
                    count=count+1 # valor del peón
                elif tablero[i][j] == fichas_negro[1]:
                    count=count+5 # valor de la torre
                elif tablero[i][j] == fichas_negro[2]:
                    count=count+3 # valor del caballo
                elif tablero[i][j] == fichas_negro[3]:
                    count=count+3 # valor del alfíl
                elif tablero[i][j] == fichas_negro[4]:
                    count=count+9 # valor de la dama
    elif equipo == "EQUIPO BLANCO" or equipo == "EB": # elegimos el equipo blanco
        for i in range(len(tablero)):
            for j in range(len(tablero[i])): # si encontramos alguna ficha que pertenezca al equipo blanco, añadimos su vcalor a la variable count
                if tablero[i][j] == fichas_blanco[0]:
                    count=count+1 # valor del peón
                elif tablero[i][j] == fichas_blanco[1]:
                    count=count+5 # valor de la torre
                elif tablero[i][j] == fichas_blanco[2]:
                    count=count+3 # valor del caballo
                elif tablero[i][j] == fichas_blanco[3]:
                    count=count+3 # valor del alfíl
                elif tablero[i][j] == fichas_blanco[4]:
                    count=count+9 # valor de la dama
    return count # devuelve el valor de las fichas del equipo indicado

# AQUÍ TENEMOS OTRA FUNCIÓN QUE MUESTRA POR PANTALLA EL TABLERO, PARA VER COMO ESTÁ LA PARTIDA

def escribirTablero(tablero):
    """función que recibe como parámetro el tablero con las fichas, y muestra por pantalla
    su contenido"""
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            print(tablero[i][j],end=" ") # vamos mostrando por pantalla cada elemento de la matriz
        print()

# LA SIGUIENTE FUNCIÓN TENDRÁ LA FUNCIONALIDAD DE CREAR UN FICHERO CON LOS DATOS DE CADA PARTIDA, ESTO ES LA PUNTUACIÓN DE LAS FICHAS DE CADA JUGADOR
# EN CADA JUGADA HASTA QUE UN EQUIPO CONSIGA LA VICTORIA

def valorFichas(tablero,ronda):
    """función que recibe el tablero y la ronda de la partida, y va apuntando en el fichero, que crea la función, (llamado: "valorFichas.txt") el valor de las fichas de cada jugador en cada ronda de la partida,
    este fichero lo guarda en la misma carpeta que el fichero .py"""
    fichero=open("valorFichas.txt","a") # creamos un fichero vacío para ir escribiendo datos
    # dependiendo de como vaya la partida, escribirá una cosa u otra...
    fichero.write("RONDA "+str(ronda)+":"+"\n")
    fichero.write("VALOR FICHAS EQUIPO NEGRO: "+str(contarPuntuacion(tablero,"EN"))+" puntos."+"\n")
    fichero.write("VALOR FICHAS EQUIPO BLANCO: "+str(contarPuntuacion(tablero,"EB"))+" puntos."+"\n")
    if jaqueMateBlancoANegro(tablero)==True: # si el equipo blanco ha ganado...
        fichero.write("El equipo BLANCO ha ganado la partida en la ronda "+str(ronda)+"."+"\n")
    elif jaqueMateNegroABlanco(tablero)==True: # si el equipo negro ha ganado...
        fichero.write("El equipo NEGRO ha ganado la partida en la ronda "+str(ronda)+"."+"\n")
    fichero.write("\n")
    fichero.close()  # cerrramos el fichero

# UTILIZAREMOS ESTA FUNCIÓN PARA VERIFICAR QUIEN ESTÁ GANANDO LA PARTIDA EN CADA TURNO, Y LO APUNTAMOS EN UN FICHERO QUE CREA LA FUNCIÓN

def ganadorMomentaneoPartida(tablero,ronda):
    """función que recibe el tablero de la partida y la ronda de la partida, y va apuntando en un fichero (que crea la función, llamado: "ganadorMomentaneoPartida.txt")
    quien va ganando en la partida dependiendo de cada turno de ella"""
    fichero=open("ganadorMomentaneoPartida.txt","a") # creamos un fichero vacío para ir escribiendo datos
    # dependiendo de como vaya la partida, escribirá una cosa u otra...
    if contarPuntuacion(tablero,"EN") > contarPuntuacion(tablero,"EB"):
        fichero.write("RONDA "+str(ronda)+": "+"El jugador del equipo NEGRO va ganando al equipo blanco."+"\n")
    elif contarPuntuacion(tablero,"EN") < contarPuntuacion(tablero,"EB"):
        fichero.write("RONDA "+str(ronda)+": "+"El jugador del equipo BLANCO va ganando al equipo negro."+"\n")
    else:
        fichero.write("RONDA "+str(ronda)+": "+"Hay un EMPATE técnico entre ambos contrincantes."+"\n")
    if jaqueMateBlancoANegro(tablero)==True: # si el equipo blanco ha ganado...
        fichero.write("El equipo BLANCO ha ganado la partida en la ronda "+str(ronda)+"."+"\n")
    elif jaqueMateNegroABlanco(tablero)==True: # si el equipo negro ha ganado...
        fichero.write("El equipo NEGRO ha ganado la partida en la ronda "+str(ronda)+"."+"\n")
    fichero.close() # cerrramos el fichero

# ESTA ES UNA FUNCIÓN AUXILIAR, CUYA UNICA FUNCION ES LA DE LECTURA DE FICHEROS CON INFORMACIÓN COMO
# LA PUNTUACIÓN DE CADA FICHA Y LA NOMENCLATURA EN EL TABLERO DE TODAS LAS FICHAS

def lecturaInformacionFichero(nombre_fichero):
    """recibe el nombre de un fichero e imprime por pantalla toda su información"""
    fichero=open(nombre_fichero,"r") # abrimos el fichero para leerlo
    for linea in fichero: # recorremos el fichero por líneas
        linea=linea.strip()
        print(linea)
    fichero.close() # cerramos el fichero
    # esta función se podría utilizar (al finalizar la partida), por ejemplo, para leer por pantalla el fichero "ganadorMomentaneoPartida.txt" o "valorFichas.txt"
    # que crea la función ganadorMomentaneoPartida(tablero) o valorFichas(tablero) en nuestra carpeta

# SON FUNCIONES QUE DETERMINAN, SEGÚN CADA FUNCIÓN, SI UN EQUIPO LE HA HECHO JACKE MATE AL OTRO, ES DECIR, SI UN EQUIPO YA HA GANADO A OTRO O NO, DE ESTA FORMA TERMINARÍA LA PARTIDA

def jaqueMateBlancoANegro(tablero):
    """recibe el tablero y retorna true si el equipo blanco a hecho 'jacke mate'
    al equipo negro y false si por el contrario todavia no ha ganado"""
    condition=True
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == "RN":
                condition = False # si encuentra el rey negro en el tablero, entonces no se ha producido "jaque mate" para el equipo negro
    # fin del bucle, no ha encontrado el rey negro, "jaque mate"
    return condition

def jaqueMateNegroABlanco(tablero):
    """recibe el tablero y retorna true si el equipo negro a hecho 'jacke mate'
    al equipo blanco y false si por el contrario todavia no ha ganado"""
    condition=True
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == "RB":
                condition = False # si encuentra el rey blanco en el tablero, entonces no se ha producido "jaque mate" para el equipo blanco
    # fin del bucle, no ha encontrado el rey blanco, "jaque mate"
    return condition

# FUNCIÓN QUE PERMITE MOVER UNA FICHA (CONTROLADA POR NOSOTROS) DESDE UNA POSICIÓN A OTRA, SIEMPRE QUE LO PERMITAN LAS NORMAS DEL JUEGO

def moverFicha(l,x,y,i,j):
    """función que recibe el tablero y mueve la ficha del equipo anfitrión en la lista según los
    valores introducidos siendo (x,y) la posición de la ficha que se quiere mover
    e (i,j) la posición a donde se quiere mover"""
    if 'B' in l[y][x] and 'B' in l[j][i]:
        print("No puede moverse la ficha a la posición introducida") # no podemos mover una ficha blanca a una posición donde hay otra ficha blanca
    if 'N' in l[y][x] and 'N' in l[j][i]:
        print("No puede moverse la ficha a la posición introducida") # no podemos mover una ficha negra a una posición donde hay otra ficha negra
    elif l[y][x]=="PB" or l[y][x]=="PN":
        peon(l,x,y,i,j) # mueve el peón seleccionado a la posición indicada (blanco o negro)
    elif l[y][x]=="TB" or l[y][x]=="TN":
        torre(l,x,y,i,j) # mueve la torre seleccionada a la posición indicada (blanco o negro)
    elif l[y][x]=="CB" or l[y][x]=="CN":
        caballo(l,x,y,i,j) # mueve el caballo seleccionado a la posición indicada (blanco o negro)
    elif l[y][x]=="AB" or l[y][x]=="AN":
        alfil(l,x,y,i,j) # mueve el alfil seleccionado a la posición indicada (blanco o negro)
    elif l[y][x]=="DB" or l[y][x]=="DN":
        dama(l,x,y,i,j) # mueve la dama seleccionada a la posición indicada (blanco o negro)
    elif l[y][x]=="RB" or l[y][x]=="RN":
        rey(l,x,y,i,j) # mueve el rey seleccionado a la posición indicada (blanco o negro)

# FUNCIÓN QUE PERMITE MOVER UNA FICHA (CONTROLADA POR LA CPU) DESDE UNA POSICIÓN A OTRA, SIEMPRE QUE LO PERMITAN LAS NORMAS DEL JUEGO

def moverFichaCPU(l,x,y,i,j):
    """función que recibe el tablero y mueve la ficha de la CPU en la lista según los
    valores introducidos siendo (x,y) la posición de la ficha que se quiere mover
    e (i,j) la posición a donde se quiere mover"""
    if ('B' in l[y][x] and not 'B' in l[j][i]) or ('N' in l[y][x] and not 'N' in l[j][i]): # podemos mover una ficha de un color a una posición donde hay otra ficha del otro color
        if l[y][x]=="PB" or l[y][x]=="PN":
            peonCPU(l,x,y,i,j) # mueve el peón seleccionado a la posición indicada (blanco o negro)
        elif l[y][x]=="TB" or l[y][x]=="TN":
            torreCPU(l,x,y,i,j) # mueve la torre seleccionada a la posición indicada (blanco o negro)
        elif l[y][x]=="CB" or l[y][x]=="CN":
            caballoCPU(l,x,y,i,j) # mueve el caballo seleccionado a la posición indicada (blanco o negro)
        elif l[y][x]=="AB" or l[y][x]=="AN":
            alfilCPU(l,x,y,i,j) # mueve el alfil seleccionado a la posición indicada (blanco o negro)
        elif l[y][x]=="DB" or l[y][x]=="DN":
            damaCPU(l,x,y,i,j) # mueve la dama seleccionada a la posición indicada (blanco o negro)
        elif l[y][x]=="RB" or l[y][x]=="RN":
            reyCPU(l,x,y,i,j) # mueve el rey seleccionado a la posición indicada (blanco o negro)

# FUNCIONES QUE COMPRUEBA SI LA FICHA ESCOGIDA SE CORRESPONDE CON CADA COLOR

def comprobarFichaBlanca(l,x,y):
    """Recibe el tablero y la posición de la ficha, y comprueba que la ficha escogida es blanca, si es blanca
    devuelve True y si no lo es devuelve False"""
    if l[y][x]=="PB" or l[y][x]=="DB" or l[y][x]=="RB" or l[y][x]=="AB" or l[y][x]=="TB" or l[y][x]=="CB":
        return True # se corresponde con la ficha blanca
    else:
        return False # no se corresponde con la ficha blanca

def comprobarFichaNegra(l,x,y):
    """Recibe el tablero y la posición de la ficha, y comprueba que la ficha escogida es negra, si es negra
    devuelve True y si no lo es devuelve False"""
    if l[y][x]=="PN" or l[y][x]=="DN" or l[y][x]=="RN" or l[y][x]=="AN" or l[y][x]=="TN" or l[y][x]=="CN":
        return True # se corresponde con la ficha negra
    else:
        return False # no se corresponde con la ficha negra

# LA FUNCIONALIDAD DE ESTA FUNCIÓN ES LA DE DEVOLVER UNA COPIA DEL TABLERO RECIBIDO COMO PARÁMETRO

def copiaTablero(l):
    """Función que copia el tablero y devuelve la copia"""
    lsal=crearTableroInicial()
    for i in range(0,8):
        for j in range(0,8):
            lsal[i][j]=l[i][j] # asignamos la posición (i,j) del tablero a la copia
    return lsal # devolvemos la copia

# ESTA ES UNA FUNCIÓN QUE SE UTILIZA PARA COMPROBAR SI EL TABLERO HA SIDO MODIFICADO RESPECTO AL TURNO ANTERIOR

def comprobarTablero(l,copia):
    """Función que recibe el tablero y la copia y comprueba si el tablero ha cambiado respecto al
    turno anterior, devuelve True si ha cambiado y False si no lo
    ha hecho"""
    for i in range(0,8):
        for j in range(0,8):
            if l[i][j]==copia[i][j]:
                continue
            else:
                return True # el tablero ha cambiado
    return False # el tablero no ha cambiado
