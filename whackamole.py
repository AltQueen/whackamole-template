import random
import pygame

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        def random_position():
            return (
                random.randrange(0, 640 // 32) * 32,
                random.randrange(0, 512 // 32) * 32
            )
        mole_position = (0,0)
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                    mole_rect = mole_image.get_rect(topleft=mole_position)
                    if mole_rect.collidepoint(event.pos):
                        # Move the mole to a new random position
                        mole_position = random_position()
            screen.fill((41, 77, 35))
            for x in range(0, 640 + 1, 32):
                pygame.draw.line(screen, (26, 48, 23), (x, 0), (x, 512))
            for y in range(0, 512 + 1, 32):
                pygame.draw.line(screen, (26, 48, 23), (0, y), (640, y))
            screen.blit(mole_image, mole_image.get_rect(topleft=mole_position))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()

