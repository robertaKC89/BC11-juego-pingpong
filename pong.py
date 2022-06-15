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
#defino todo esto como variable global. Así podré acceder tanto desde classes Pong como desde Paleta
ALTO_PALETA = 40
ANCHO_PALETA = 5

ANCHO = 640
ALTO = 480
MARGEN_LATERAL = 40

TAMANYO_PELOTA = 6

#me creo una clase Paleta y heredará de clase .Rect que ya me ofrece parámetros base
#necesitaré constructor __init__ para recoger datos de las 2 paletas
class Paleta (pygame.Rect):
    #defino estas 2 constantes para que me quede muy claro cuando se pase desde el bucle
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
            #la y es la posición de un rectángulo en Pygame
            self.y = self.y - self.velocidad
            if self.y < 0:
                self.y = 0
        else:
            self.y = self.y + self.velocidad
            #xk la posición y marca la parte superior
            if self.y > ALTO - ALTO_PALETA:
                self.y = ALTO - ALTO_PALETA

class Pong:
    #necesito constructor para iniciar pygame 
    def __init__(self):
        print("Construyendo un objeto pong")
        pygame.init()
        # módulo display para control de pantalla y usamos .set_mode (ver uso en documentación)
        self.pantalla = pygame.display.set_mode((ANCHO,ALTO))
        # variables creadas como propiedad de la class Pong
        self.jugador1 = Paleta(
            MARGEN_LATERAL,               # coordenada x (left)
            (ALTO-ALTO_PALETA)/2)         # coordenada y (top)

        self.jugador2 = Paleta(
            ANCHO-MARGEN_LATERAL-ANCHO_PALETA,
            (ALTO-ALTO_PALETA)/2)

    #necesito bucle principal que recorrerá todo el rato comprobando mil cosas del juego
    #bucle: pregunta por eventos + dibuja, dibuja + da la vuelta CONSTANTEMENTE o SALIDA!
    def bucle_principal (self):
        salir = False
        while not salir:
            #eventos de librería que dentro de bucle recorro (for) para comprobar si hay y que no se cuelgue el juego
            #get me devolverá una lista de tipo eventos
            for evento in pygame.event.get():
                #pregunto si este evento (keydown)es que he pulsado tecla salir (keyscape), salgo!
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        print("Adiós, te has escapado")
                        salir = True
                    if evento.key == pygame.K_r:
                        print("Iniciamos nueva partida")
                        self.marcador.inicializar()
                if evento.type == pygame.QUIT:
                    salir = True 

            #petición para saber qué teclas estoy pulsando
            #funcion get_pressed de pygame que devuelve lista con booleans segun estado de cada tecla
            estado_teclas = pygame.key.get_pressed()
            # elemplo: si estado_teclas está en índice.K_a se mueve
            if estado_teclas[pygame.K_a]:
                self.jugador1.muevete(Paleta.ARRIBA)
            if estado_teclas[pygame.K_z]:
                self.jugador1.muevete(Paleta.ABAJO)
            if estado_teclas[pygame.K_UP]:
                self.jugador2.muevete(Paleta.ARRIBA)
            if estado_teclas[pygame.K_DOWN]:
                self.jugador2.muevete(Paleta.ABAJO)

            #pinto la red del campo
            #con fill me borra y rellena de los espacios no usados  
            self.pantalla.fill(C_NEGRO)
            pygame.draw.line(self.pantalla, C_BLANCO, (ANCHO/2, 0), (ANCHO/2, ALTO))
            pygame.draw.rect(self.pantalla, C_BLANCO, self.jugador1)
            pygame.draw.rect(self.pantalla, C_BLANCO, self.jugador2)
            pygame.draw.rect(self.pantalla, C_BLANCO, self.pelota)

            #refresco de pantalla
            pygame.display.flip()
            self.clock.tick(FPS)
            
# llamo al juego desde la linea de comandos. Recuerdo que __main__ es el módulo principal que cargo 
if __name__ == "__main__":
    juego = Pong()
    juego.bucle_principal()
