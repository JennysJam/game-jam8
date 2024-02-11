import pygame

window: pygame.Surface
clock = pygame.time.Clock()
def main():
    init()
    loop()

def init():
    global window
    window = pygame.display.set_mode((300, 400))
    window.fill('red')

def loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60)
        pygame.display.flip()

main()