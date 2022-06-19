from cgitb import text
from random import randint
from typing import TextIO
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
#defino todo esto como parámetros/variables de config.para poder usarlos donde haga falta
ALTO_PALETA = 40
ANCHO_PALETA = 5
VELOCIDAD_PALA = 5

ANCHO = 640
ALTO = 480
MARGEN_LATERAL = 40

TAMANYO_PELOTA = 6
VEL_MAX_PELOTA = 5

C_NEGRO = (0, 0, 0)
C_BLANCO = (255, 255, 255)

FPS = 60

PUNTOS_PARTIDA = 3

#me creo una clase Paleta y heredará de class .Rect que ya me ofrece parámetros base
#necesitaré constructor __init__ para recoger datos de las 2 paletas
class Paleta(pygame.Rect):
    #defino estas 2 constantes para que me quede claro el 'muevete' cuando se pase desde el bucle
    ARRIBA = True
    ABAJO = False
    #me genero mi constructor de Paleta propio
    def __init__(self, x, y):
        #llamo al constructor de la class superior con __init__ que hereda Paleta de .Rect
        super(Paleta, self).__init__(x, y, ANCHO_PALETA, ALTO_PALETA)
        #necesito introducir velocidad para saber espacio que va a moverse
        self.velocidad = VELOCIDAD_PALA
        
    #a parte de velocidad necesito saber dirección
    def muevete(self, direccion):
        if direccion == self.ARRIBA:
            #la y es una propiedad/posición de un rectángulo en Pygame
            self.y = self.y - self.velocidad
            if self.y < 0: 
                self.y = 0
        else:
            self.y = self.y + self.velocidad
            #si la posicion es mayor que el alto de pantalla - alto de paleta se lo asigno otra vez
            if self.y > ALTO - ALTO_PALETA:
                self.y = ALTO - ALTO_PALETA

#pongo .Rect para ver la similitud con la class Paleta
class Pelota(pygame.Rect):
    #1ºcreo mi propio constructor
    def __init__(self):
        super(Pelota, self).__init__(
            (ANCHO-TAMANYO_PELOTA)/2, (ALTO-TAMANYO_PELOTA)/2,
            TAMANYO_PELOTA, TAMANYO_PELOTA
        )

        # velocidad_x_valor_valido = False
        # while not velocidad_x_valor_valido:
        #     self.velocidad_x = randint(-VEL_MAX_PELOTA, VEL_MAX_PELOTA)
        #     velocidad_x_valor_valido = self.velocidad_x != 0

        #1º de doy valor a la velocidad_x con la variable
        self.velocidad_x = 0
        while self.velocidad_x == 0:
            self.velocidad_x = randint(-VEL_MAX_PELOTA, VEL_MAX_PELOTA)

        self.velocidad_y = randint(-VEL_MAX_PELOTA, VEL_MAX_PELOTA)

    def muevete(self):
        self.x = self.x + self.velocidad_x
        self.y = self.y + self.velocidad_y
        #si la posición y<0 (xk al rebotar saldría de pantalla) tienen que pasar 2 cosas
        if self.y < 0:
            #no te sales de pantalla ya que la y es 0 (lo mismo he echo con paleta)
            self.y = 0
            #cambio el signo para invertir velocidad
            self.velocidad_y = -self.velocidad_y
        #para el borde inferior
        if self.y > ALTO-TAMANYO_PELOTA:
            self.y = ALTO-TAMANYO_PELOTA
            self.velocidad_y = -self.velocidad_y

#no hereda de nada, por ello no llamo con paréntesis 
class Marcador:
    #como cualquier class tengo un constructor y lo primero que hace es llamar a inicializar partida si se gana
    def __init__(self):
        #llamo a inicializar letra_marcador en el constructor xk solo la cargaré una vez
        self.letra_marcador = pygame.font.SysFont ('roboto', 100)
        #creo para llamar a otro tipo de fuente y tamaño para el sms
        self.letra_mensaje = pygame.font.SysFont('arial', 40)
        self.inicializar()

    #condicion de ganador para finalizar partida
    def comprobar_ganador(self):
        if self.partida_finalizada:
            return True
        if self.valor[0] == PUNTOS_PARTIDA:
            #establezco sms a la variable y le pongo boolean
            self.mensaje_ganador = "Ha ganado el jugador 1"
            self.partida_finalizada = True
        elif self.valor[1] == PUNTOS_PARTIDA:
            self.mensaje_ganador = "Ha ganado el jugador 2"
            self.partida_finalizada = True
        #siempre devuelvo partida finalizada y si no ha ganado nadie devolverá su valor = False
        return self.partida_finalizada

    def inicializar(self):
        self.valor = [0, 0]
        self.partida_finalizada = False
    
    #genero un metodo para que marcador se pinte solo
    def pintar (self, pantalla):
        #necesito el texto de los 2 marcadores con tipografia que me he guardado (xo esto aun no lo pinta)
        texto = pygame.font.Font.render(self.letra_marcador, str(self.valor[0]), True, C_BLANCO)
        pos_x =  (ANCHO/2 - MARGEN_LATERAL - ANCHO_PALETA)/2 - texto.get_width()/2 + MARGEN_LATERAL + ANCHO_PALETA
        pos_y =  MARGEN_LATERAL
        #ahora si que lo pinto 
        pygame.Surface.blit(pantalla, texto, (pos_x, pos_y))

        texto = pygame.font.Font.render(self.letra_marcador, str(self.valor[1]), False, C_BLANCO)
        pos_x =  (ANCHO/2 - MARGEN_LATERAL - ANCHO_PALETA)/2 - texto.get_width()/2 + ANCHO/2
        pos_y =  MARGEN_LATERAL
        #ahora si que lo pinto 
        pygame.Surface.blit(pantalla, texto, (pos_x, pos_y))

        if self.partida_finalizada:
            texto = pygame.font.Font.render(self.letra_mensaje, self.mensaje_ganador, False, C_BLANCO)
            pos_x =  ANCHO/2 - texto.get_width()/2
            pos_y =  ALTO/2 - texto.get_height()/2 - MARGEN_LATERAL
            pygame.Surface.blit(pantalla, texto, (pos_x, pos_y))
        

class Pong:
    #necesito constructor para iniciar entorno pygame
    def __init__(self):
        pygame.init()
        # módulo display para control de pantalla y usamos .set_mode (ver uso en documentación)
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        #módulo clock instancio para cuando tenga que hacer cosas...
        self.clock = pygame.time.Clock()

        #me preparo par pintar texto
        pygame.font.init()
        #para cargar una tipografia el sistema me la guardo en el propio juego por si la quiero reutilizar
        self. tipografia = pygame.font.SysFont ('roboto',50) 

        #variables creadas como propiedad de la class Pong
        self.jugador1 = Paleta(
            MARGEN_LATERAL,               # coordenada x (left)
            (ALTO-ALTO_PALETA)/2)         # coordenada y (top)

        self.jugador2 = Paleta(
            ANCHO-MARGEN_LATERAL-ANCHO_PALETA,
            (ALTO-ALTO_PALETA)/2)

        #necesito pelota que instancio y para pintarla la debo pasar al bucle principal
        self.pelota = Pelota()
        #inicio marcador y lo instancio
        self.marcador = Marcador()
    
    #necesito bucle principal que recorrerá todo el rato comprobando mil cosas del juego
    #bucle: pregunta por eventos + dibuja, dibuja + da la vuelta CONSTANTEMENTE o SALIDA!
    def bucle_principal(self):
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
                    #si pulso otra tecla reinicio partida
                    if evento.key == pygame.K_r:
                        print("Iniciamos nueva partida")
                        self.marcador.inicializar()
                if evento.type == pygame.QUIT:
                    salir = True

            #petición para saber qué teclas estoy pulsando
            #funcion get_pressed de pygame que devuelve lista con booleans segun estado de cada tecla
            estado_teclas = pygame.key.get_pressed()
            # elemplo: compruebo si estado_teclas está en índice.K_a se mueve
            if estado_teclas[pygame.K_a]:
                self.jugador1.muevete(Paleta.ARRIBA)
            if estado_teclas[pygame.K_z]:
                self.jugador1.muevete(Paleta.ABAJO)
            if estado_teclas[pygame.K_UP]:
                self.jugador2.muevete(Paleta.ARRIBA)
            if estado_teclas[pygame.K_DOWN]:
                self.jugador2.muevete(Paleta.ABAJO)

            #si hay ganador ya no me hace falta comprobar nada de esto, paro la partida
            if not self.marcador.comprobar_ganador():
                self.pelota.muevete()
                self.colision_paletas()     #hago la llamada pero def está más abajo
                self.comprobar_punto()      #hago la llamada pero def está más abajo

            #pinto la red del campo
            #con fill me borra y rellena de los espacios no usados
            #luego lo vuelvo a pintar todo (ya que estoy en bucle)
            self.pantalla.fill(C_NEGRO)
            pygame.draw.line(self.pantalla, C_BLANCO, (ANCHO/2, 0), (ANCHO/2, ALTO))
            pygame.draw.rect(self.pantalla, C_BLANCO, self.jugador1)
            pygame.draw.rect(self.pantalla, C_BLANCO, self.jugador2)
            pygame.draw.rect(self.pantalla, C_BLANCO, self.pelota)
            #llamará a marcador y le pasará la info de pantalla
            self.marcador.pintar(self.pantalla)

            # refresco de pantalla con flip
            pygame.display.flip()
            #en referencia a la variable de config. que tengo arriba fuera-> haz tick 60veces/s
            self.clock.tick(FPS)

    def colision_paletas(self):
        #Collidirect comprueba si la pelota ha colisionado con una de las paletas y le cambia la dirección
        if pygame.Rect.colliderect(self.pelota, self.jugador1) or pygame.Rect.colliderect(self.pelota, self.jugador2):
            self.pelota.velocidad_x = -self.pelota.velocidad_x
            #estamos generando un efecto simple/aleatorio al choque de pelota con paletas 
            self.pelota.velocidad_y = randint(-VEL_MAX_PELOTA, VEL_MAX_PELOTA)

    #marcador pasa a ser una priopiedad del juego
    def comprobar_punto(self):
        if self.pelota.x < 0:       #compruebo si pelota se ha salido por algun lado
            self.marcador.valor[1] = self.marcador.valor[1] + 1  #actualizo marcador   
            print(f"El nuevo marcador es {self.marcador.valor}")
            self.pelota.velocidad_x = randint(-VEL_MAX_PELOTA, -1)
            #si hay ganador inicio nuevo punto (sino no hará nada)
            self.iniciar_punto()
        elif self.pelota.x > ANCHO:
            self.marcador.valor[0] = self.marcador.valor[0] + 1
            print(f"El nuevo marcador es {self.marcador.valor}")
            self.pelota.velocidad_x = randint(1, VEL_MAX_PELOTA)
            self.iniciar_punto()

    #método que coje la pelota y la pone en centro de pantalla para poder inicializar partida 
    def iniciar_punto(self):
        self.pelota.x = (ANCHO - TAMANYO_PELOTA)/2
        self.pelota.y = (ALTO - TAMANYO_PELOTA)/2
        self.pelota.velocidad_y = randint(-VEL_MAX_PELOTA, VEL_MAX_PELOTA)


# llamo al juego desde la linea de comandos. Recuerdo que __main__ es el módulo principal que cargo
if __name__ == "__main__":
    juego = Pong()
    juego.bucle_principal()