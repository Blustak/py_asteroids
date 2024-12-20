import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from ui import UIElement


def main():
    pygame.font.init()
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    score_element = UIElement()
    lives_element = UIElement()

    while True:
        # game logic phase
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for entity in updatable:
            entity.update(dt)

        for entity in asteroids:
            if player.is_colliding(entity):
                if player.lives <= 0:
                    game_over_screen(screen)
                    pygame.time.delay(5 * 1000)
                    print("Game over!")
                    print(f"Score:{player.score}")
                    return

                else:
                    player.lives -= 1
                    player.position = pygame.Vector2(
                        SCREEN_WIDTH / 2,
                        SCREEN_HEIGHT / 2,
                    )
                    player.rotation = 0
                    player.timer = 0

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.is_colliding(shot):
                    player.score += ASTEROID_SCORE
                    asteroid.split()
                    shot.kill()

        # update UI elements
        score_element.update(f"Score:{player.score}")
        lives_element.update(f"LIVES: {player.lives}")

        # rendering phase
        screen.fill(pygame.Color("black"))
        for entity in drawable:
            entity.draw(screen)

        # Render UI on top
        score_element.draw(screen, 0, 0)
        lives_element.draw(
            screen,
            0,
            score_element.text.get_size()[1],
        )

        # Screen update and wait
        pygame.display.flip()
        dt = (clock.tick(60)) / 1000


def game_over_screen(screen):
    text = UIElement(color="red", size=64)
    text.update("GAME OVER")
    (x, y) = (
        (SCREEN_WIDTH / 2) - text.text.get_rect().centerx,
        (SCREEN_HEIGHT / 2) - text.text.get_rect().centery,
    )
    text.draw(screen, x, y)
    pygame.display.flip()


if __name__ == "__main__":
    main()
