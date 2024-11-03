import pygame as pg
pg.init()

SCREEN = pg.display.set_mode((75*10, 75*10))
pg.display.set_caption("COD - 205")
def animacion():
    ani_der = []
    ani_izq = []
    ani_arr = []
    ani_aba = []
    pag = pg.image.load("./img/Snorlax-sprite.png").convert_alpha()

    # Tamaño de cada celda en la imagen
    sprite_width = 84
    sprite_height = 102

    # La imagen tiene 4 filas y 3 columnas
    # Las filas están indexadas de 0 a 3
    # Las columnas están indexadas de 0 a 2

    for fil in range(0, 4):  # 4 filas
        for col in range(0, 3):  # 3 columnas
            spr = pg.Rect(sprite_width * col, sprite_height * fil, sprite_width, sprite_height)
            if fil == 0:
                ani_aba.append(pag.subsurface(spr))  # Fila 0 = Abajo
            if fil == 1:
                ani_izq.append(pag.subsurface(spr))  # Fila 1 = Izquierda
            if fil == 2:
                ani_der.append(pag.subsurface(spr))  # Fila 2 = Derecha
            if fil == 3:
                ani_arr.append(pag.subsurface(spr))  # Fila 3 = Arriba


    return ani_der, ani_izq, ani_arr, ani_aba

ad, ai, ar, ab = animacion()

class jugador(pg.sprite.Sprite):
    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self)
        self.ani_derecha = ad
        self.ani_izquierda = ai
        self.ani_arriba = ar
        self.ani_abajo = ab
        self.index = 0
        self.speed = 7
        self.direction = ""
        self.image = self.ani_derecha[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def update(self):
        if self.index >= len(self.ani_derecha):  # Aseguramos que el índice esté dentro del rango
            self.index = 0
        if self.direction == "DER":
            self.image = self.ani_derecha[self.index]
            self.index += 1
        elif self.direction == "IZQ":
            self.image = self.ani_izquierda[self.index]
            self.index += 1
        elif self.direction == "ARR":
            self.image = self.ani_arriba[self.index]
            self.index += 1
        elif self.direction == "ABJ":
            self.image = self.ani_abajo[self.index]
            self.index += 1
        else:
            if self.direction == "DER_F":
                self.image = self.ani_derecha[0]
            elif self.direction == "IZQ_F":
                self.image = self.ani_izquierda[0]
            elif self.direction == "ARR_F":
                self.image = self.ani_arriba[0]
            elif self.direction == "ABJ_F":
                self.image = self.ani_abajo[0]

    def hevent(self, key):
        # Obtenemos las dimensiones de la ventana
        screen_width, screen_height = SCREEN.get_size()

        # Controlamos los límites de la ventana
        if key[pg.K_a]:  # Izquierda
            if self.rect.x - self.speed >= 0:
                self.rect.x -= self.speed
                self.direction = "IZQ"
        elif key[pg.K_d]:  # Derecha
            if self.rect.x + self.rect.width + self.speed <= screen_width:
                self.rect.x += self.speed
                self.direction = "DER"
        elif key[pg.K_w]:  # Arriba
            if self.rect.y - self.speed >= 0:
                self.rect.y -= self.speed
                self.direction = "ARR"
        elif key[pg.K_s]:  # Abajo
            if self.rect.y + self.rect.height + self.speed <= screen_height:
                self.rect.y += self.speed
                self.direction = "ABJ"
        else:
            # Si no se presiona ninguna tecla, detener la animación de movimiento
            if self.direction == "DER":
                self.direction = "DER_F"
            elif self.direction == "IZQ":
                self.direction = "IZQ_F"
            elif self.direction == "ARR":
                self.direction = "ARR_F"
            elif self.direction == "ABJ":
                self.direction = "ABJ_F"
            else:
                self.direction = ""

# Cargar imagen de fondo
# fondo = pg.image.load("./img/fondopokemon2.png").convert()
fondo = pg.transform.scale(pg.image.load("./img/fondopokemon2.png").convert(), (SCREEN.get_width(), SCREEN.get_height()))

# MÓDULO PRINCIPAL
jgd = jugador([0, 0])
g_sprites = pg.sprite.Group()
g_sprites.add(jgd)
FPS = 18
CLOCK = pg.time.Clock()
cerrar = False
while not cerrar:
    CLOCK.tick(FPS)
    
    # Dibujar el fondo
    SCREEN.blit(fondo, (0, 0))  # Dibuja el fondo en la posición (0, 0)
    
    # Actualizar la pantalla
    g_sprites.update()
    g_sprites.draw(SCREEN)

    # Controlar eventos y movimiento del jugador
    key = pg.key.get_pressed()
    jgd.hevent(key)  # Llamamos al método hevent dentro de la clase jugador
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            cerrar = True
    
    pg.display.update()  # Actualiza la pantalla