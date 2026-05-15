import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 300, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont(None, 28)
clock = pygame.time.Clock()

stack = []
positions = []
target_positions = []

BLOCK_WIDTH, BLOCK_HEIGHT = 200, 40
START_X = (WIDTH - BLOCK_WIDTH) // 2
BASE_Y = HEIGHT - BLOCK_HEIGHT - 20

enqueue_button = pygame.Rect(100, HEIGHT - 90, 120, 35)
dequeue_button = pygame.Rect(100, HEIGHT - 50, 120, 35)


def draw_stack():
    screen.fill((50, 50, 50))

 
    button_bar = pygame.Rect(10, HEIGHT - 100, WIDTH - 20, 100)
    pygame.draw.rect(screen, (0, 128, 0), button_bar)


    pygame.draw.rect(screen, (180, 180, 180), enqueue_button)
    enq_text = FONT.render("Enqueue", True, (0, 0, 0))
    screen.blit(enq_text, enq_text.get_rect(center=enqueue_button.center))

    pygame.draw.rect(screen, (180, 180, 180), dequeue_button)
    deq_text = FONT.render("Dequeue", True, (0, 0, 0))
    screen.blit(deq_text, deq_text.get_rect(center=dequeue_button.center))


    for i, val in enumerate(stack):

        for i, val in enumerate(stack):
            rect = pygame.Rect(
                START_X,
                positions[i],
                BLOCK_WIDTH,
                BLOCK_HEIGHT
            )

            pygame.draw.rect(screen, (100, 150, 250), rect)

            text = FONT.render(str(val), True, (0, 0, 0))
            text_rect = text.get_rect(center=rect.center)
            screen.blit(text, text_rect)


        pygame.draw.rect(screen, (100, 150, 250), rect)

        text = FONT.render(str(val), True, (0, 0, 0))
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)


    info_text = FONT.render("SPACE: Push, BACKSPACE: Pop, ESC: Quit", True, (200, 200, 200))
    screen.blit(info_text, (10, 10))


def update_animation():
    panel_top = HEIGHT - 100

    for i in range(len(positions)):
        target_y = panel_top - (i + 1) * (BLOCK_HEIGHT + 5)

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
                if enqueue_button.collidepoint(event.pos):
                    stack.append(len(stack) + 1)
                    positions.append(HEIGHT)

                if dequeue_button.collidepoint(event.pos) and stack:
                    if stack:
                        stack.pop(0)
                        positions.pop(0)

        draw_stack()
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
