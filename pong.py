#antes he instalado gestor de paquetes de pygame = pip 3
import pygame
"""
  - algo de herencia:

  - color, ancho, alto
  - hay cosas fijas como el color y el tamaño

  - método moverse: solo hacia arriba y hacia abajo
  - método de chocar: límite para no salirse de la pantalla

  - método para interactuar con la pelota???
"""

#me creo una clase Paleta y utilizo clase .Rect que ya me ofrece parámetros base
#necesitaré constructor __init__ para recoger datos de las 2 paletas
class Paleta (pygame.Rect): 
    def __init__():
        super()

class Pong:
    #me genero una pantalla
    _ALTO = 640
    _ANCHO = 480
    _MARGEN_LATERAL = 40

    _ANCHO_PALETA = 5
    _ALTO_PALETA = _ALTO / 5

    #necesito constructor para iniciar pygame 
    def __init__(self):
        print("Construyendo un objeto pong")
        pygame.init()
        # módulo display para control de pantalla y usamos .set_mode (ver uso en documentación)
        self.pantalla = pygame.display.set_mode((self._ANCHO, self._ALTO))
        # variables creadas como propiedad de la class Pong
        self.jugador1 = Paleta(
            self._MARGEN_LATERAL,               # coordenada x (left)
            (self._ALTO-self._ALTO_PALETA)/2,   # coordenada y (top)
            self._ANCHO_PALETA,                 # ancho (width)
            self._ALTO_PALETA)                  # alto (height)

        self.jugador2 = Paleta(
            self._ANCHO-self._MARGEN_LATERAL-self._ANCHO_PALETA,
            (self._ALTO-self._ALTO_PALETA)/2,
            self._ANCHO_PALETA,
            self._ALTO_PALETA)

    #necesito bucle principal que recorrerá todo el rato comprobando mil cosas del juego
    def bucle_principal (self):
        print("Estoy en el bucle principal")
        # bucle: pregunta por eventos + dibuja, dibuja + da la vuelta CONSTANTEMENTE! 
        while True:
            #eventos de librería que dentro del bucle recorro (for) para comprobar si los hay y que no se cuelgue el juego
            #get me devolverá una lista de tipo eventos 
            for evento in pygame. event.get():
                #pregunto si este tipo de evento (keydown)es que he pulsado tecla salir (keyscape), salgo!
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.KEY_SCAPE:
                        return
                        
            #cada vez que haga algo con el juego tendré que pintar la paleta en la posicion correcta
            pygame.draw.rect (self.pantalla, (255, 255,255),self.jugador1)
            pygame.draw.rect (self.pantalla, (255, 255,255),self.jugador2)
            #flip me refresca y me muestra cada cambio que voy haciendo
            pygame.display.flip()
            
# llamo al juego desde la linea de comandos. Recuerdo que __main__ es el módulo principal que cargo 
if __name__ == "__main__":
    juego = Pong()
    juego.bucle_principal()
