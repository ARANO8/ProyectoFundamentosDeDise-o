import pygame
import sys
pygame. init()

g = 9.81
initial_velocity_y = 5
initial_velocity_x = 1
coef_restitution = 0.85
time_step = 0.01
ground_level = 500
ball_radius = 50
width, height = 490, 590
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("COD - 205")

y_pos = 100
x_pos = width // 2
velocity_y = -initial_velocity_y
velocity_x = initial_velocity_x
WHITE = (255, 255, 255)

try:
    background_image = pygame.image.load("./img/fondo.jpg") 
    background_image = pygame.transform.scale(background_image, (width, height)) 
except pygame.error as e:
    print(f"Error al cargar la imagen de fondo: {e}")
    pygame.quit()
    sys.exit()

try :
    ball_image = pygame.image.load( "./img/ballSinFondo.png")
    ball_image = pygame.transform.scale(ball_image, (ball_radius*2,ball_radius*2))  
except pygame.error as e:
    print(f"Error al cargar la imagen: {e}")
    pygame.quit()
    sys.exit()

rotation_angle = 0
rotation_speed = 5
running = True

clock= pygame.time.Clock()
def update_ball_position():
    global y_pos, velocity_y, x_pos, velocity_x, rotation_angle
    velocity_y += g * time_step
    y_pos += velocity_y * time_step * 100
    x_pos += velocity_x * time_step * 100
    if y_pos + ball_radius >= ground_level :
        y_pos = ground_level - ball_radius
        velocity_y = -velocity_y * coef_restitution
    if x_pos - ball_radius <= 0 or x_pos + ball_radius >= width :
        velocity_x = -velocity_x * coef_restitution
    if y_pos * ball_radius >= ground_level :
        rotation_angle -= velocity_x * rotation_speed
try :
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        update_ball_position()

        # Dibujar el fondo
        screen.blit(background_image, (0, 0))
        rotated_ball_image = pygame.transform.rotate(ball_image, rotation_angle)
        ball_rect = rotated_ball_image.get_rect(center = (int(x_pos), int(y_pos)))
        screen.blit(rotated_ball_image, ball_rect.topleft)
        
        pygame.display.flip()
        clock.tick(60)
except Exception as e:
    print(f"Error: {e}")
    pygame.quit()
    sys.exit()
pygame.quit()