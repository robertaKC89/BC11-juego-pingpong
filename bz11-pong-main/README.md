# bz11-pong

Clon del clásico juego PONG de Atari.

## Como colaborar en este proyecto

Primero debes clonar este repositorio en tu PC.

Es recomendable usar un entorno virtual antes de instalar las dependencias.

```
python -m venv env

# En MacOS o Linux
source ./env/bin/activate

# En Windows (con cmd/símbolo del sistema)
.\env\Scripts\activate
```

Una vez creado y activado el entorno virtual, ya puedes instalar las dependencias

```
pip install -r requirements.txt
```

Para arrancar el juego basta con ejecutar desde la línea de comandos:

```
python pong.py
```

## Cómo jugar

- El jugador 1 mueve su paleta con las teclas A y Z
- El jugador 2 mueve su paleta con las teclas ARRIBA y ABAJO
- La tecla ESC cierra el programa
- La tecla R inicia una nueva partida
