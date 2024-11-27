import pygame
import random
from config import *
AZUL = (34, 69, 179)


pygame.init()

def inicializar_tablero(dificultad:int)->list:
    '''
    Inicializa una matriz vacia y la retorna.
    '''
    matriz = []
    for _ in range(dificultad):
        fila = [0] * dificultad
        matriz += [fila] 

    return matriz

def mostrar_matriz(matriz:list)->None:
    '''
    Funcion: mostrar una matriz 
    Parametro: recibe por parametro una matriz y la muestra
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j],  end=" ")
        print("")

def dibujar_matriz(dificultad:int, ventana, espaciado:int): #Arreglar
    pos_inicio = 200
    pos_y = 55
    for _ in range(dificultad + 1):
        pygame.draw.line(ventana, BLANCO, (pos_inicio, 55), (pos_inicio, 555))
        pos_inicio += espaciado
    for _ in range(dificultad + 1):
        pygame.draw.line(ventana, BLANCO, (200, pos_y), (700, pos_y))
        pos_y += espaciado

# def dibujar_matriz(dificultad:int, ventana, espaciado:int): #Arreglar
#     '''
#     dibuja una matriz 
#     recibe como parametro la dificultad(que depende de la dificultad cambia el tamaño de la matriz),
#     la superficie donde se dibujara, y el espaciado
#     '''
#     pos_inicio = 200
#     pos_y = 55
#     for _ in range(dificultad + 1):
#         pygame.draw.line(ventana, BLANCO, (pos_inicio, 55), (pos_inicio, 555), width=1)
#         pos_inicio += espaciado
#     for _ in range(dificultad + 1):
#         pygame.draw.line(ventana, BLANCO, (200, pos_y), (700, pos_y), width=1)
#         pos_y += espaciado

def colocar_navio(matriz:list, tipo_navio:str, cantidad:int):
    """
    Recibe una matriz, un tipo de navio (submarino, destructor, crucero o acorazado)
    y la cantidad de navios que se quiere colocar.
    """

    match tipo_navio:
        case "submarino":
            largo = 1
        case "destructor":
            largo = 2
        case "crucero":
            largo = 3
        case "acorazado":
            largo = 4

    contador_colocados = 0

    while contador_colocados < cantidad:

        fila_inicial = random.randint(0, len(matriz) - (largo))
        columna_inicial = random.randint(0, len(matriz[0]) - (largo))
        orientacion = random.choice(["H", "V"])

        if validar_casilleros(matriz, fila_inicial, columna_inicial, largo, orientacion) == True:
            contador_colocados += 1
            for _ in range(largo):

                matriz[fila_inicial][columna_inicial] = largo

                if orientacion == "H":
                    columna_inicial += 1
                else:
                    fila_inicial += 1
    
def validar_casilleros(matriz:list,fila:int, columna:int, largo:int, orientacion:str):
    """
    recibe una matriz, una fila, una columna, el largo del objeto que se quiere colocar
    y la orientacion del objeto ("H"/"V")
    verifica que todos los espacios necesarios sean del valor 0 y devuelve true.
    si algun casillero es distinto a 0 devuelve false.
    """
    bandera_vacio = True
    contador = 0
    if orientacion == "H" and (columna + largo) < len(matriz[0]):
        while contador < largo:
            if matriz[fila][columna] != 0:
                bandera_vacio = False
                break

            columna += 1
            contador += 1

    if orientacion == "V" and (fila + largo) < len(matriz):
        while contador < largo:
            if matriz[fila][columna] != 0:
                bandera_vacio = False
                break

            fila += 1
            contador += 1
    
    return bandera_vacio


def dibujar_tablero(ventana, matriz, estado_casillas, tam_celda, pos_centrado):
    """
    Dibuja el tablero basado en el estado visual de las casillas.
    
    Parámetros:
    - ventana: la ventana de Pygame.
    - matriz: la matriz lógica oculta.
    - estado_casillas: la matriz de estado visual.
    - tam_celda: tamaño de las celdas del tablero.
    - pos_centrado: posición centrada del tablero.
    
    Retorna:
    - matriz_rectangulos: matriz de rectángulos de Pygame.
    """


    matriz_rectangulos = []
    for i, fila in enumerate(matriz):
        fila_rectangulos = []
        for j, _ in enumerate(fila):
            # Coordenadas del rectángulo
            x = pos_centrado[0] + j * tam_celda
            y = pos_centrado[1] + i * tam_celda

            # Determinar el color según el estado
            if estado_casillas[i][j] == 0:  # No disparado
                color = NEGRO
            elif estado_casillas[i][j] == -1:  # Agua
                color = AZUL
            elif estado_casillas[i][j] == 1:  # Nave dañada
                color = (255, 255, 0)  # Amarillo
            elif estado_casillas[i][j] == 2:  # Nave hundida
                color = ROJO

            # Dibujar rectángulo
            rect = pygame.draw.rect(ventana, color, (x, y, tam_celda - 2, tam_celda - 2))
            fila_rectangulos.append(rect)

        matriz_rectangulos.append(fila_rectangulos)

    return matriz_rectangulos


def centrar_eje_x(ancho_fondo, ancho_colocar):

    centro_fondo = ancho_fondo //2
    centro_colocar = ancho_colocar//2

    eje_x_centrado = centro_fondo - centro_colocar

    return eje_x_centrado

def detectar_click(matriz:list)->list:
    mouse_pos = []
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(matriz)):
                for j in range(len(matriz[0])):
                    pos_mouse = pygame.mouse.get_pos()
                    mouse_pos[i][j] = pos_mouse
    return mouse_pos




