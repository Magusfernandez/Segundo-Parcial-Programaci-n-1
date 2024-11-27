import pygame
from funcion_batalla import *
from config import *
import pygame.mixer as mixer


pygame.init()
pygame.mixer.init()

ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
mixer.music.load("juego_b_naval.py\musica_fondo.mp3")
mixer.music.play()
ruido_bomba = mixer.Sound("juego_b_naval.py\\efecto_bomba.mp3")
ruido_bomba.set_volume(0.5)

icono = pygame.image.load("juego_b_naval.py\\logo3.jpg")
pygame.display.set_icon(icono)

pygame.display.set_caption("Batalla Naval")

fondo_principal = pygame.image.load("juego_b_naval.py\\fondo1.jpg")
fondo_principal = pygame.transform.scale(fondo_principal, (ANCHO_VENTANA, ALTO_VENTANA))

fondo = pygame.image.load("juego_b_naval.py\\fondo2.jpg")
fondo = pygame.transform.scale(fondo, (ANCHO_VENTANA, ALTO_VENTANA))

fondo_puntajes = pygame.image.load("juego_b_naval.py\\fondo.jpg")
fondo_puntajes = pygame.transform.scale(fondo_puntajes, (ANCHO_VENTANA, ALTO_VENTANA))

puntos = 0
fuente_puntos = pygame.font.SysFont("Consola", 25, bold = False)
texto_puntos = fuente_puntos.render(f"Puntos: {str(puntos)}", True, BLANCO, None)
ancho_texto_puntos = texto_puntos.get_size()[0] 


imagen_nivel = pygame.image.load("juego_b_naval.py\\nivel.png")
imagen_jugar = pygame.image.load("juego_b_naval.py\\jugar.png")
imagen_puntaje = pygame.image.load("juego_b_naval.py\\ver_puntaje.png")
imagen_salir = pygame.image.load("juego_b_naval.py\\salir.png")
imagen_reiniciar = pygame.image.load("juego_b_naval.py\\reiniciar.png")
imagen_volver = pygame.image.load("juego_b_naval.py\\volver.png")
imagen_facil = pygame.image.load("juego_b_naval.py\\facil.png")
imagen_medio = pygame.image.load("juego_b_naval.py\\medio.png")
imagen_dificil = pygame.image.load("juego_b_naval.py\dificil.png")

imagen_puntos = pygame.image.load("juego_b_naval.py\\fondo_boton.png")

imagen_nivel = pygame.transform.scale(imagen_nivel, (ancho_boton, alto_boton))
imagen_jugar = pygame.transform.scale(imagen_jugar, (ancho_boton, alto_boton))
imagen_puntaje = pygame.transform.scale(imagen_puntaje, (ancho_boton, alto_boton))
imagen_salir = pygame.transform.scale(imagen_salir, (ancho_boton, alto_boton))
imagen_reiniciar = pygame.transform.scale(imagen_reiniciar, (ancho_boton - 60, alto_boton - 20))
imagen_volver = pygame.transform.scale(imagen_volver, (ancho_boton - 60, alto_boton - 20))
imagen_facil = pygame.transform.scale(imagen_facil, (ancho_boton, alto_boton))
imagen_medio = pygame.transform.scale(imagen_medio, (ancho_boton, alto_boton))
imagen_dificil = pygame.transform.scale(imagen_dificil, (ancho_boton, alto_boton))
imagen_puntos = pygame.transform.scale(imagen_puntos, (ancho_boton - 70, alto_boton))

boton_jugar = imagen_jugar.get_rect()
boton_jugar.x = (ANCHO_VENTANA / 2 - ancho_boton / 2)
boton_jugar.y = (ALTO_VENTANA / 6)

boton_nivel = imagen_nivel.get_rect()
boton_nivel.x = (ANCHO_VENTANA / 2 - ancho_boton / 2)
boton_nivel.y = (ALTO_VENTANA / 3)

boton_puntaje = imagen_puntaje.get_rect()
boton_puntaje.x = (ANCHO_VENTANA / 2 - ancho_boton / 2)
boton_puntaje.y = (ALTO_VENTANA / 2)

boton_salir = imagen_salir.get_rect()
boton_salir.x = (ANCHO_VENTANA / 2 - ancho_boton / 2)
boton_salir.y = (ALTO_VENTANA - ALTO_VENTANA / 3)

boton_volver = imagen_reiniciar.get_rect()
boton_volver.x = 755
boton_volver.y = 590

boton_reiniciar = imagen_reiniciar.get_rect()
boton_reiniciar.x = 3
boton_reiniciar.y = 590

boton_facil = imagen_facil.get_rect()
boton_facil.x = (ANCHO_VENTANA / 2 - ancho_boton / 2)
boton_facil.y = (ALTO_VENTANA / 6)

boton_medio = imagen_medio.get_rect()
boton_medio.x = (ANCHO_VENTANA / 2 - ancho_boton / 2)
boton_medio.y = (ALTO_VENTANA / 3)

boton_dificil = imagen_dificil.get_rect()
boton_dificil.x = (ANCHO_VENTANA / 2 - ancho_boton / 2)
boton_dificil.y = (ALTO_VENTANA / 2)


       #Esto quizas haya que convertirlo en funcion

tablero_oculto = inicializar_tablero(dificultad)
colocar_navio(tablero_oculto, "submarino", 4) 
colocar_navio(tablero_oculto, "destructor", 3) 
colocar_navio(tablero_oculto, "crucero", 2) 
colocar_navio(tablero_oculto, "acorazado", 1)
estado_casillas= inicializar_tablero(dificultad)
# matriz_rectangulos

bandera_pantallas = 0
dificultad = 10
corriendo = True

while corriendo == True:

    if bandera_pantallas == 0:
        mixer.music.set_volume(20)
        ventana.blit(fondo_principal, (0, 0))
        ventana.blit(imagen_jugar, boton_jugar)
        ventana.blit(imagen_nivel, boton_nivel)
        ventana.blit(imagen_puntaje, boton_puntaje)
        ventana.blit(imagen_salir, boton_salir)

    elif bandera_pantallas == 1:        #click en boton jugar
        ventana.blit(fondo, (0, 0))
        ventana.blit(imagen_reiniciar, boton_reiniciar)
        ventana.blit(imagen_volver, boton_volver)
        ventana.blit(imagen_puntos, (5, 5))
        ventana.blit(texto_puntos, (centrar_eje_x(ancho_boton - 70, ancho_texto_puntos), 20))

        coordenadas_rect = dibujar_tablero(tablero_oculto)
        
        
    
    elif bandera_pantallas == 2:        #click en boton ver puntajes
        ventana.blit(fondo_puntajes, (0, 0))
        ventana.blit(imagen_volver, boton_volver)


    elif bandera_pantallas == 3:     # boton nivel
        ventana.blit(fondo_puntajes, (0, 0))
        ventana.blit(imagen_facil, boton_facil)
        ventana.blit(imagen_medio, boton_medio)
        ventana.blit(imagen_dificil, boton_dificil)
        ventana.blit(imagen_volver, boton_volver)
            

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            corriendo = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                corriendo = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_mouse = pygame.mouse.get_pos()
            print(pos_mouse)
            if bandera_pantallas == 0:
                if boton_salir.collidepoint(pos_mouse):
                    corriendo = False

                elif boton_jugar.collidepoint(pos_mouse):
                    bandera_pantallas = 1 
                
                elif boton_puntaje.collidepoint(pos_mouse):
                    bandera_pantallas = 2
                
                elif boton_nivel.collidepoint(pos_mouse):
                    bandera_pantallas = 3
        
            elif bandera_pantallas == 1:
                if boton_reiniciar.collidepoint(pos_mouse):   # resetear barcos
                    pass
                elif boton_volver.collidepoint(pos_mouse):
                    bandera_pantallas = 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
            
            elif bandera_pantallas == 2:
                if boton_volver.collidepoint(pos_mouse):
                    bandera_pantallas = 0
            
            elif bandera_pantallas == 3:
                if boton_facil.collidepoint(pos_mouse):
                    bandera_pantallas = 1
                elif boton_medio.collidepoint(pos_mouse):
                    dificultad = 20
                    bandera_pantallas = 1
                elif boton_dificil.collidepoint(pos_mouse):
                    dificultad = 40
                    bandera_pantallas = 1
                    

                elif boton_volver.collidepoint(pos_mouse):
                    bandera_pantallas = 0


 
    pygame.display.flip()

pygame.quit()