class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self):
        """Инициализирует настройки игры."""
# Параметры экрана
        self.screen_width = 1080
        self.screen_height = 700
        self.bg_color = (0, 85, 120)
        self.ship_speed_factor = 1.5