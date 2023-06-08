# ESTE MÓDULO PYTHON ESTÁ COMPUESTO SOLO Y EXCLUSIVAMENTE POR FUNCIONES QUE PERMITEN MOVER LAS FICHAS DEL
# TABLERO DE AJEDREZ SIEMPRE QUE LAS REGLAS DEL JUEGO LO PERMITAN

def ceroUno(l,x,y): # Se llama ceroUno porque antes las casillas se representaban con ceros y unos
    """Función que recibe el tablero y dibuja las casillas blancas y negras, simulando un tablero de ajedrez"""
    if (x+1+y+1)%2==0:
        l[y][x]="--" # dibuja casilla blanca (simulando a un tablero real)
    else:
        l[y][x]="  " # dibuja casilla negra (simulando a un tablero real)

def RetrocesoPeon(l,x,y,i,j):
    """Función que recibe el tablero y comprueba que los peones sigan la dirección que deben seguir"""
    if i>=8 or j>=8 or x>=8 or y>=8:
        return True
    elif l[y][x]=="PN" and y>=j:
        return True
    elif l[y][x]=="PB" and y<=j:
        return True

# ESTAS FUNCIONES SIRVEN PARA MOVER FICHAS QUE POSEEMOS NOSOTROS (EQUIPO ANFITRIÓN), SI TENEMOS EL EQUIPO BLANCO SE MUEVEN FICHAS BLANCAS, Y SI SOMOS DEL NEGRO
# PUES PARA MOVER FICHAS NEGRAS

def torre(l,x,y,i,j):
    """Función que recibe el tablero y mueve la torre en la posición (x,y)
    a la posición (i,j) si cumple las normas del juego"""
    t=l[y][x]
    condition= True
    if i>=8 or j>=8 or x>=8 or y>=8:
        print("Posición erronea") # no se puede mover una ficha fuera del tablero
        return l
    elif x==i:
        if j<y:
            m=-1
        else:
            m=1
        for k in range(y+m,j,m):
            if l[k][x]!="--" and l[k][x]!="  ":
                condition= False
        if condition:
            l[j][i]=t # asignamos la ficha a mover con la casilla elegida del tablero
            ceroUno(l,x,y) # rellenamos la casilla en la que estaba la ficha por "--" o "  ", como si fueran casillas blancas o negras
        else:
            print("No puede moverse la ficha a la posición introducida")
    elif y==j:
        if i<x:
            m=-1
        else:
            m=1
        for k in range(x+m,i,m):
            if l[y][k]!="--" and l[y][k]!="  ":
                condition= False
        if condition:
            l[j][i]=t # asignamos la ficha a mover con la casilla elegida del tablero
            ceroUno(l,x,y) # rellenamos la casilla en la que estaba la ficha por "--" o "  ", como si fueran casillas blancas o negras
        else:
            print("No puede moverse la ficha a la posición introducida")
    else:
        print("Movimiento no válido")

def peon(l,x,y,i,j):
    """Función que recibe el tablero y mueve el peón en la posición (x,y)
    a la posición (i,j) si cumple las normas del juego"""
    p=l[y][x]
    if RetrocesoPeon(l,x,y,i,j):
        print("Movimiento no válido")
    elif i>=8 or j>=8 or x>=8 or y>=8:
        print("Posición erronea") # no se puede mover una ficha fuera del tablero
    elif x!=i:
        if abs(x-i)==1 and abs(y-j)==1:
            if l[j][i]!="--" and l[j][i]!="  ":
                l[j][i]=p # asignamos la ficha a mover con la casilla elegida del tablero
                ceroUno(l,x,y) # rellenamos la casilla en la que estaba la ficha por "--" o "  ", como si fueran casillas blancas o negras
            else:
                print("No puede moverse la ficha a la posición introducida")
        else:
            print("Movimiento no válido")
    elif abs(y-j)==1:
        if j>y:
            m=-1
        else:
            m=1
        for k in range(j,y,m):
            if l[k][x] == "--" or l[k][x] == "  ":
                l[j][i]=p # asignamos la ficha a mover con la casilla elegida del tablero
                ceroUno(l,x,y) # rellenamos la casilla en la que estaba la ficha por "--" o "  ", como si fueran casillas blancas o negras
            else:
                print("No puede moverse la ficha a la posición introducida")
    else:
        print("Movimiento no válido")

def caballo(l,x,y,i,j):
    """Función que recibe el tablero y mueve el caballo en la posición (x,y)
    a la posición (i,j) si cumple las normas del juego"""
    c=l[y][x]
    if i>=8 or j>=8 or x>=8 or y>=8:
        print("Posición erronea") # no se puede mover una ficha fuera del tablero
        return l
    else:
        if (x+2==i and y+1==j) or (x+2==i and y-1==j) or (x-2==i and y+1==j) or (x-2==i and y-1==j) or (x+1==i and y+2==j) or (x+1==i and y-2==j) or (x-1==i and y+2==j) or (x-1==i and y-2==j):
            l[j][i]=c # asignamos la ficha a mover con la casilla elegida del tablero
            ceroUno(l,x,y) # rellenamos la casilla en la que estaba la ficha por "--" o "  ", como si fueran casillas blancas o negras
        else:
            print("No puede moverse la ficha a la posición introducida")

def rey(l,x,y,i,j):
    """Función que recibe el tablero y mueve el rey en la posición (x,y)
    a la posición (i,j) si cumple las normas del juego"""
    r=l[y][x]
    if i>=8 or j>=8 or x>=8 or y>=8:
        print("Posición erronea") # no se puede mover una ficha fuera del tablero
        return l
    elif abs(x-i)>1 or abs(y-j)>1:
        print("Movimiento no valido")
    else:
        l[j][i]=r # asignamos la ficha a mover con la casilla elegida del tablero
        ceroUno(l,x,y) # rellenamos la casilla en la que estaba la ficha por "--" o "  ", como si fueran casillas blancas o negras

def alfil(l,x,y,i,j):
    """Función que recibe el tablero y mueve el alfil en la posición (x,y)
    a la posición (i,j) si cumple las normas del juego"""
    a=l[y][x]
    if i>=8 or j>=8 or x>=8 or y>=8:
        print("Posición erronea") # no se puede mover una ficha fuera del tablero
        return l
    elif abs(i-x)!=abs(y-j):
        print("Movimiento no valido")
    else:
        if x>i:
            n=-1
        else:
            n=1
        if y>j:
            m=-1
        else:
            m=1
        condition = True
        for k in range(abs(y-j)-1):
            if l[y+m][x+n]!="--" and l[y+m][x+n]!="  ":
                condition = False
            if m<0:
                m=m-1
            else:
                m=m+1
            if n<0:
                n=n-1
            else:
                n=n+1
        if condition:
            l[j][i]=a # asignamos la ficha a mover con la casilla elegida del tablero
            ceroUno(l,x,y) # rellenamos la casilla en la que estaba la ficha por "--" o "  ", como si fueran casillas blancas o negras
        else:
            print("No puede moverse la ficha a la posición introducida")

def dama(l,x,y,i,j):
    """Función que recibe el tablero y mueve a la dama en la posición (x,y)
    a la posición (i,j) si cumple las normas del juego"""
    d=l[y][x]
    condition=True
    if i>=8 or j>=8 or x>=8 or y>=8:
        print("Posición erronea") # no se puede mover una ficha fuera del tablero
        return l
    elif x==i:
        if j<y:
            m=-1
        else:
            m=1
        for k in range(y+m,j,m):
            if l[k][x]!="--" and l[k][x]!="  ":
                condition= False
        if condition:
            l[j][i]=d # asignamos la ficha a mover con la casilla elegida del tablero
            ceroUno(l,x,y) # rellenamos la casilla en la que estaba la ficha por "--" o "  ", como si fueran casillas blancas o negras
        else:
            print("No puede moverse la ficha a la posición introducida")
    elif y==j:
        if i<x:
            m=-1
        else:
            m=1
        for k in range(x+m,i,m):
            if l[y][k]!="--" and l[y][k]!="  ":
                condition= False
        if condition:
            l[j][i]=d # asignamos la ficha a mover con la casilla elegida del tablero
            ceroUno(l,x,y) # rellenamos la casilla en la que estaba la ficha por "--" o "  ", como si fueran casillas blancas o negras
        else:
            print("No puede moverse la ficha a la posición introducida")
    elif abs(i-x)==abs(y-j):
        if x>i:
            n=-1
        else:
            n=1
        if y>j:
            m=-1
        else:
            m=1
        condition = True
        for k in range(abs(y-j)-1):
            if l[y+m][x+n]!="--" and l[y+m][x+n]!="  ":
                condition = False
            if m<0:
                m=m-1
            else:
                m=m+1
            if n<0:
                n=n-1
            else:
                n=n+1
        if condition:
            l[j][i]=d # asignamos la ficha a mover con la casilla elegida del tablero
            ceroUno(l,x,y) # rellenamos la casilla en la que estaba la ficha por "--" o "  ", como si fueran casillas blancas o negras
        else:
            print("No puede moverse la ficha a la posición introducida")
    else:
        print("Movimiento no valido")

# ESTAS FUNCIONES SERÁN UTLIZADAS PARA MOVER LAS FICHAS QUE CONTROLA LA CPU, YA SEA EL EQUIPO BLANCO O EL NEGERO, DEPENDE DE CUAL NO ELIJAMOS

def torreCPU(l,x,y,i,j):
    """Función que recibe el tablero y mueve la torre de la CPU en la posición (x,y)
    a la posición (i,j) si cumple las normas del juego"""
    t=l[y][x]
    condition= True
    if i>=8 or j>=8 or x>=8 or y>=8:
        return l
    elif x==i:
        if j<y:
            m=-1
        else:
            m=1
        for k in range(y+m,j,m):
            if l[k][x]!="--" and l[k][x]!="  ":
                condition= False
        if condition:
            l[j][i]=t # asignamos la ficha a mover con la casilla elegida del tablero
            ceroUno(l,x,y) # rellenamos la casilla en la que estaba la ficha por "--" o "  ", como si fueran casillas blancas o negras
    elif y==j:
        if i<x:
            m=-1
        else:
            m=1
        for k in range(x+m,i,m):
            if l[y][k]!="--" and l[y][k]!="  ":
                condition= False
        if condition:
            l[j][i]=t # asignamos la ficha a mover con la casilla elegida del tablero
            ceroUno(l,x,y) # rellenamos la casilla en la que estaba la ficha por "--" o "  ", como si fueran casillas blancas o negras


def peonCPU(l,x,y,i,j):
    """Función que recibe el tablero y mueve el peón de la CPU en la posición (x,y)
    a la posición (i,j) si cumple las normas del juego"""
    p=l[y][x]
    if RetrocesoPeon(l,x,y,i,j):
        return l
    elif x!=i:
        if abs(x-i)==1 and abs(y-j)==1:
            if l[j][i]!="--" and l[j][i]!="  ":
                l[j][i]=p # asignamos la ficha a mover con la casilla elegida del tablero
                ceroUno(l,x,y) # rellenamos la casilla en la que estaba la ficha por "--" o "  ", como si fueran casillas blancas o negras
    elif abs(y-j)==1:
        if j>y:
            m=-1
        else:
            m=1
        for k in range(j,y,m):
            if l[k][x] == "--" or l[k][x] == "  ":
                l[j][i]=p # asignamos la ficha a mover con la casilla elegida del tablero
                ceroUno(l,x,y) # rellenamos la casilla en la que estaba la ficha por "--" o "  ", como si fueran casillas blancas o negras

def caballoCPU(l,x,y,i,j):
    """Función que recibe el tablero y mueve el caballo de la CPU en la posición (x,y)
    a la posición (i,j) si cumple las normas del juego"""
    c=l[y][x]
    if i>=8 or j>=8 or x>=8 or y>=8:
        return l
    else:
        if (x+2==i and y+1==j) or (x+2==i and y-1==j) or (x-2==i and y+1==j) or (x-2==i and y-1==j) or (x+1==i and y+2==j) or (x+1==i and y-2==j) or (x-1==i and y+2==j) or (x-1==i and y-2==j):
            l[j][i]=c # asignamos la ficha a mover con la casilla elegida del tablero
            ceroUno(l,x,y) # rellenamos la casilla en la que estaba la ficha por "--" o "  ", como si fueran casillas blancas o negras

def reyCPU(l,x,y,i,j):
    """Función que recibe el tablero y mueve el rey de la CPU en la posición (x,y)
    a la posición (i,j) si cumple las normas del juego"""
    r=l[y][x]
    if i>=8 or j>=8 or x>=8 or y>=8:
        return l
    elif abs(x-i)>1 or abs(y-j)>1:
        return l
    else:
        l[j][i]=r # asignamos la ficha a mover con la casilla elegida del tablero
        ceroUno(l,x,y) # rellenamos la casilla en la que estaba la ficha por "--" o "  ", como si fueran casillas blancas o negras

def alfilCPU(l,x,y,i,j):
    """Función que recibe el tablero y mueve el alfil de la CPU en la posición (x,y)
    a la posición (i,j) si cumple las normas del juego"""
    a=l[y][x]
    if i>=8 or j>=8 or x>=8 or y>=8:
        return l
    elif abs(i-x)!=abs(y-j):
        return l
    else:
        if x>i:
            n=-1
        else:
            n=1
        if y>j:
            m=-1
        else:
            m=1
        condition = True
        for k in range(abs(y-j)-1):
            if l[y+m][x+n]!="--" and l[y+m][x+n]!="  ":
                condition = False
            if m<0:
                m=m-1
            else:
                m=m+1
            if n<0:
                n=n-1
            else:
                n=n+1
        if condition:
            l[j][i]=a # asignamos la ficha a mover con la casilla elegida del tablero
            ceroUno(l,x,y) # rellenamos la casilla en la que estaba la ficha por "--" o "  ", como si fueran casillas blancas o negras

def damaCPU(l,x,y,i,j):
    """Función que recibe el tablero y mueve a la dama de la CPU en la posición (x,y)
    a la posición (i,j) si cumple las normas del juego"""
    d=l[y][x]
    condition=True
    if i>=8 or j>=8 or x>=8 or y>=8:
        return l
    elif x==i:
        if j<y:
            m=-1
        else:
            m=1
        for k in range(y+m,j,m):
            if l[k][x]!="--" and l[k][x]!="  ":
                condition= False
        if condition:
            l[j][i]=d # asignamos la ficha a mover con la casilla elegida del tablero
            ceroUno(l,x,y) # rellenamos la casilla en la que estaba la ficha por "--" o "  ", como si fueran casillas blancas o negras
    elif y==j:
        if i<x:
            m=-1
        else:
            m=1
        for k in range(x+m,i,m):
            if l[y][k]!="--" and l[y][k]!="  ":
                condition= False
        if condition:
            l[j][i]=d # asignamos la ficha a mover con la casilla elegida del tablero
            ceroUno(l,x,y) # rellenamos la casilla en la que estaba la ficha por "--" o "  ", como si fueran casillas blancas o negras
    elif abs(i-x)==abs(y-j):
        if x>i:
            n=-1
        else:
            n=1
        if y>j:
            m=-1
        else:
            m=1
        condition = True
        for k in range(abs(y-j)-1):
            if l[y+m][x+n]!="--" and l[y+m][x+n]!="  ":
                condition = False
            if m<0:
                m=m-1
            else:
                m=m+1
            if n<0:
                n=n-1
            else:
                n=n+1
        if condition:
            l[j][i]=d # asignamos la ficha a mover con la casilla elegida del tablero
            ceroUno(l,x,y) # rellenamos la casilla en la que estaba la ficha por "--" o "  ", como si fueran casillas blancas o negras
