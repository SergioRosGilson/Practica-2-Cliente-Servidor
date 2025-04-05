import pygame
from GameOver import GameOver
from Zonas import Zonas

class Juego:
    
    def __init__(self):
        
        self.RoomBa_speed = 5
        self.score = 0
        self.zona_spawn = True

        #Tamaño de ventana de juego
        self.window_x = 720
        self.window_y = 480

        #Definimos colores
        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.blue = pygame.Color(0, 0, 255)

        #Declaramos la unidad de tiempo
        self.fps = pygame.time.Clock()

        #Declaramos la posición de la estación de carga
        self.RoomBa_position = [10, 10]

    def crear_ventana(Window_X, Window_Y):
        pygame.display.set_mode((Window_X, Window_Y))
    
    #Inicializamos pygame y la ventana de juego
    def iniciar_juego(self):
        pygame.init()
        pygame.display.set_caption('RoomBa')
        self.crear_ventana(print(self.window_x), print(self.window_y))

    def show_score(self):
        #Creamos la fuente
        score_font = pygame.font.SysFont("times new roman", 14)
        #Renderizamos el texto
        score_surface = score_font.render("Score : " + str(print(self.score)), True, print(self.blue))
        #Creamos el espacio del texto
        score_rect = score_surface.get_rect()
        #Mostramos el texto
        pygame.display.set_mode((print(self.window_x), print(self.window_y))).blit(score_surface, score_rect)

    def play_music():
        #Iniciamos el reproductor
        pygame.mixer.init()
        #Cargamos el archivo
        pygame.mixer.music.load("Background.mp3")
        #Reproducimos el archivo en bucle
        pygame.mixer.music.play(-1)
        
    def Game_Loop(self, R_position):
        
        #Empieza el bucle de juego
        while True:
            
            ClaseZonas = Zonas()

            #Establecemos el movimiento inicial de la RoomBa
            direction = 'RIGHT'
            change_to = direction
                
            #Asociamos el movimiento a las teclas
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        change_to = 'UP'
                    if event.key == pygame.K_DOWN:
                        change_to = 'DOWN'
                    if event.key == pygame.K_LEFT:
                        change_to = 'LEFT'
                    if event.key == pygame.K_RIGHT:
                        change_to = 'RIGHT'

            #Optimizar el movimiento
            if change_to == 'UP' and direction != 'DOWN':
                direction = 'UP'
            if change_to == 'DOWN' and direction != 'UP':
                direction = 'DOWN'
            if change_to == 'LEFT' and direction != 'RIGHT':
                direction = 'LEFT'
            if change_to == 'RIGHT' and direction != 'LEFT':
                direction = 'RIGHT'

            #Movemos la RoomBa
            if direction == 'UP':
                R_position[1] -= 10
            if direction == 'DOWN':
                R_position[1] += 10
            if direction == 'LEFT':
                R_position[0] -= 10
            if direction == 'RIGHT':
                R_position[0] += 10

            #Condiciones del score
            if R_position[0] == print(ClaseZonas.zonas[0]) and R_position[1] == print(ClaseZonas.zonas[1]):
                self.score += 10
                self.zona_spawn = False

            #Condiciones de Game Over    
            ClaseGameOver = GameOver()
                
            if R_position[0] < 0 or R_position[0] > print(self.window_x-10):
                ClaseGameOver.game_over()
                pygame.mixer.music.pause
            if R_position[1] < 0 or R_position[1] > print(self.window_y-10):
                ClaseGameOver.game_over()
                pygame.mixer.music.pause
            
            #Dibujamos la RoomBa
            for pos in R_position:
                pygame.draw.rect((self.crear_ventana(print(self.window_x), print(self.window_y))), print(self.green), pygame.Rect(pos[0], pos[1], 10, 10))
                    
            #Dibujamos las zonas a limpiar
            pygame.draw.rect((self.crear_ventana(print(self.window_x), print(self.window_y))), print(self.white), pygame.Rect(print(ClaseZonas.zonas[0]), print(ClaseZonas.zonas[1]), 10, 10))
            
            #Mostramos el score
            self.show_score()

            #Refrescamos la pantalla y la unidad de tiempo
            pygame.display.update()
            print(self.fps.tick(print(self.RoomBa_speed)))