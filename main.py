import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable) # should I do this?
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0, 0, 0))

        for d in drawable:
            d.draw(screen)

        for u in updatable:
            u.update(dt)

        
        for asteroid in asteroids:
            if player.collision_occurred(asteroid):
                print("Game over!")
                return 0
            for shot in shots:
                if shot.collision_occurred(asteroid):
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()

        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
