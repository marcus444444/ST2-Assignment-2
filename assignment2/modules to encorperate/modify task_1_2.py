import pygame
import sys

pygame.init()

screenWidth, screenHeight = 800, 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
defaultFont = pygame.font.SysFont(None, 28)
clock = pygame.time.Clock()
backButton = pygame.Rect(screenWidth - 120, 20, 100, 40)

stack = []
positions = []
targetPositions = []

blockWidth, blockHeight = 200, 40
startX = (screenWidth - blockWidth) // 2
baseY = screenHeight - blockHeight - 20

enqueueButton = pygame.Rect(100, screenHeight - 90, 120, 35)
dequeueButton = pygame.Rect(100, screenHeight - 50, 120, 35)


def draw_stack():
    screen.fill((50, 50, 50))

 
    button_bar = pygame.Rect(10, screenHeight - 100, screenWidth - 20, 100)
    pygame.draw.rect(screen, (0, 128, 0), button_bar)


    pygame.draw.rect(screen, (200, 200, 200), enqueueButton)
    enq_text = defaultFont.render("Enqueue", True, (0, 0, 0))
    screen.blit(enq_text, enq_text.get_rect(center=enqueueButton.center))

    pygame.draw.rect(screen, (180, 180, 180), dequeueButton)
    deq_text = defaultFont.render("Dequeue", True, (0, 0, 0))
    screen.blit(deq_text, deq_text.get_rect(center=dequeueButton.center))


    for i, val in enumerate(stack):

        for i, val in enumerate(stack):
            rect = pygame.Rect(
                startX,
                positions[i],
                blockWidth,
                blockHeight
            )

            pygame.draw.rect(screen, (100, 150, 250), rect)

            text = defaultFont.render(str(val), True, (0, 0, 0))
            text_rect = text.get_rect(center=rect.center)
            screen.blit(text, text_rect)


        pygame.draw.rect(screen, (100, 150, 250), rect)

        text = defaultFont.render(str(val), True, (0, 0, 0))
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)


    info_text = defaultFont.render("SPACE: Push, BACKSPACE: Pop, ESC: Quit", True, (200, 200, 200))
    screen.blit(info_text, (10, 10))

    pygame.draw.rect(screen, (200, 200, 200), backButton)
    back_text = defaultFont.render("Back", True, (0, 0, 0))
    screen.blit(back_text, back_text.get_rect(center=backButton.center))


def update_animation():
    panel_top = screenHeight - 100

    for i in range(len(positions)):
        target_y = panel_top - (i + 1) * (blockHeight + 5)

        positions[i] += (target_y - positions[i]) * 0.2

def main():


    counter = 1
    running = True


    while running:

        update_animation()
        draw_stack()
        pygame.display.flip()
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if backButton.collidepoint(event.pos):
                    running = False
                    break
                if enqueueButton.collidepoint(event.pos):
                    stack.append(len(stack) + 1)
                    positions.append(screenHeight)

                if dequeueButton.collidepoint(event.pos) and stack:
                    if stack:
                        stack.pop(0)
                        positions.pop(0)

        draw_stack()
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
