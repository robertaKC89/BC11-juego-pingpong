#antes he instalado gestor de paquetes de pygame = pip 3
from typing_extensions import Self
import pygame
"""
  - algo de herencia:

  - color, ancho, alto
  - hay cosas fijas como el color y el tamaño

  - método moverse: solo hacia arriba y hacia abajo
  - método de chocar: límite para no salirse de la pantalla

  - método para interactuar con la pelota???
"""
#defino todo esto como variable global. Así podré acceder tanto desde classes Pong como Paleta
ALTO_PALETA = 40
ANCHO_PALETA = 5

ANCHO = 640
ALTO = 480
MARGEN_LATERAL = 40

TAMANYO_PELOTA = 6

#me creo una clase Paleta y heredará de clase .Rect que ya me ofrece parámetros base
#necesitaré constructor __init__ para recoger datos de las 2 paletas
class Paleta (pygame.Rect):
    #defino estas 2 constantes para que me quede muy claro cuando llame a dirección
    ARRIBA = True
    ABAJO = False
    #me genero mi constructor de Paleta propio
    def __init__(self, x, y):
        #llamo al constructor de la class superior con __init__ que hereda Paleta de .Rect
        super(Paleta, self).__init__(x, y, ANCHO_PALETA, ALTO_PALETA)
        #necesito introducir velocidad para saber espacio que va a moverse
        self.velocidad = 5
    #a parte de velocidad necesito saber dirección 
    def muevete(self, direccion):
        if direccion == self.ARRIBA:
            self.y = self.y - self.velocidad
            if self.y < 0:
                self.y = 0
        else:
            self.y = self.y + self.velocidad
            if self.y > ALTO - ALTO_PALETA:
                self.y = ALTO - ALTO_PALETA

class Pong:
    #necesito constructor para iniciar pygame 
    def __init__(self):
        print("Construyendo un objeto pong")
        pygame.init()
        # módulo display para control de pantalla y usamos .set_mode (ver uso en documentación)
        self.pantalla = pygame.display.set_mode((self._ANCHO, self._ALTO))
        # variables creadas como propiedad de la class Pong
        self.jugador1 = Paleta(
            MARGEN_LATERAL,               # coordenada x (left)
            (ALTO-ALTO_PALETA)/2)         # coordenada y (top)

        self.jugador2 = Paleta(
            ANCHO-MARGEN_LATERAL-ANCHO_PALETA,
            (ALTO-ALTO_PALETA)/2)

    #necesito bucle principal que recorrerá todo el rato comprobando mil cosas del juego
    def bucle_principal (self):
        print("Estoy en el bucle principal")
        # bucle: pregunta por eventos + dibuja, dibuja + da la vuelta CONSTANTEMENTE o SALIDA! 
        while True:
            #eventos de librería que dentro de bucle recorro (for) para comprobar si hay y que no se cuelgue el juego
            #get me devolverá una lista de tipo eventos 
            for evento in pygame. event.get():
                #pregunto si este tipo de evento (keydown)es que he pulsado tecla salir (keyscape), salgo!
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.KEY_SCAPE:
                        print ('adiós, te has escapado')
                        return
                if evento.type == pygame.QUIT:
                    return
            #......
            estado_teclas = pygame.key.get_pressed()
            if estado_teclas[pygame.K_a]:
                self.jugador1.muevete(Paleta.ARRIBA)
            if estado_teclas[pygame.K_z]:
                self.jugador1.muevete(Paleta.ABAJO)
            if estado_teclas[pygame.K_UP]:
                self.jugador2.muevete(Paleta.ARRIBA)
            if estado_teclas[pygame.K_DOWN]:
                self.jugador2.muevete(Paleta.ABAJO)
            #pinto la red del campo 
            pygame.draw.line(self.pantalla, (255, 255, 255), (self._ANCHO/2, 0), (self._ANCHO/2, self._ALTO))
            #cada vez que haga algo con el juego tendré que pintar la paleta en la posicion correcta
            pygame.draw.rect (self.pantalla, (255, 255,255),self.jugador1)
            pygame.draw.rect (self.pantalla, (255, 255,255),self.jugador2)
            #flip me refresca y me muestra cada cambio que voy haciendo en la pantalla
            pygame.display.flip()
            
# llamo al juego desde la linea de comandos. Recuerdo que __main__ es el módulo principal que cargo 
if __name__ == "__main__":
    juego = Pong()
    juego.bucle_principal()
