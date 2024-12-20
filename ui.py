import pygame
from constants import FONT_SIZE, FONT_COLOR, FONT_BACKGROUND


class UIElement(pygame.sprite.Sprite):
    def __init__(
        self,
        font=None,
        color=FONT_COLOR,
        bg_color=FONT_BACKGROUND,
        size=FONT_SIZE,
    ):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.font = pygame.font.Font(font, size=size)
        self.color = pygame.Color(color)
        self.bg_color = pygame.Color(bg_color)
        self.text = None

    def update(self, text):
        self.text = self.font.render(
            text,
            False,
            self.color,
            self.bg_color,
        )

    def draw(self, screen, x, y):
        screen.blit(self.text, (x, y))
