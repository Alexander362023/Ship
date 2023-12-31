import sys
import pygame
from pygame.locals import *
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
# Инициализирует игру и создает объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 230, 230)
    # Создание корабля.
    ship = Ship(ai_settings, screen)
# Запуск основного цикла игры.
    while True:   
# Отслеживание событий клавиатуры и мыши.
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        
        gf.check_events(ship)
        ship.update()
        # При каждом проходе цикла перерисовывается экран.        
        gf.update_screen(ai_settings, screen, ship)   
# Отображение последнего прорисованного экрана.                
run_game()





