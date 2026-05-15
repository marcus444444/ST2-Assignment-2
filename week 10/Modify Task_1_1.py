import pygame
import sys
import time


pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()
numbers = [5, 3, 9, 1, 7, 4]
cell_width = WIDTH // len(numbers)
user_input = ""
target = []


def draw_grid(highlight_index=None, comparisons=0, target=None):
    screen.fill((30, 30, 30))
    for i, num in enumerate(numbers):
        color = (200, 200, 200)
        if i == highlight_index:
            color = (255, 100, 100)

        rect = pygame.Rect(i * cell_width, 0, cell_width - 2, HEIGHT)
        pygame.draw.rect(screen, color, rect)
        text = FONT.render(str(num), True, (0, 0, 0))
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)


    button_bar = pygame.Rect(10, HEIGHT - 100, WIDTH - 20, 100)
    pygame.draw.rect(screen, (0, 128, 0), button_bar)

    input_rect = pygame.Rect(20, HEIGHT - 80, WIDTH - 140, 40)
    pygame.draw.rect(screen, (255, 255, 255), input_rect, 2)

    input_surface = FONT.render(user_input, True, (255, 255, 255))
    screen.blit(input_surface, (input_rect.x + 5, input_rect.y + 5))

    # Button
    button_rect = pygame.Rect(WIDTH - 110, HEIGHT - 80, 90, 40)
    pygame.draw.rect(screen, (100, 200, 100), button_rect)

    button_text = FONT.render("Search", True, (0, 0, 0))
    screen.blit(button_text, button_text.get_rect(center=button_rect.center))

    # Info text
    info = f"Target: {target}   Comparisons: {comparisons}"
    info_surface = FONT.render(info, True, (255, 255, 255))
    screen.blit(info_surface, (20, HEIGHT - 30))

    return input_rect, button_rect



def linear_search(target):

    comparisons = 0

    for i, num in enumerate(numbers):

        comparisons += 1
        draw_grid(i, comparisons, target)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if num == target:
            return i, comparisons

        time.sleep(0.5)

    return -1, comparisons



def main():
    global user_input, target

    running = True

    while running:
        input_rect, button_rect = draw_grid()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode




            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):

                    try:
                        target = [int(x.strip()) for x in user_input.split(",")]
                    except:
                        target = []

                
            for t in target:
                idx, comparisons = linear_search(t)

                # show result before next search
                draw_grid(idx, comparisons, t)
                pygame.display.flip()
                time.sleep(1)


        clock.tick(60)


    pygame.quit()


if __name__ == "__main__":
    main()