import pygame
import sys
import time


pygame.init()
screenWidth, screenHeight = 800, 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
defaultFont = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()
backButton = pygame.Rect(screenWidth - 120, 20, 100, 40)
numbers = [5, 3, 9, 1, 7, 4]
cellWidth = screenWidth // len(numbers)
user_input = ""
target = []


def draw_grid(highlight_index=None, comparisons=0, target=None):
    screen.fill((30, 30, 30))
    for i, num in enumerate(numbers):
        color = (200, 200, 200)
        if i == highlight_index:
            color = (255, 100, 100)

        rect = pygame.Rect(i * cellWidth, 0, cellWidth - 2, screenHeight)
        pygame.draw.rect(screen, color, rect)
        text = defaultFont.render(str(num), True, (0, 0, 0))
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)


    button_bar = pygame.Rect(10, screenHeight - 100, screenWidth - 20, 100)
    pygame.draw.rect(screen, (0, 128, 0), button_bar)

    input_rect = pygame.Rect(20, screenHeight - 80, screenWidth - 140, 40)
    pygame.draw.rect(screen, (255, 255, 255), input_rect, 2)

    input_surface = defaultFont.render(user_input, True, (255, 255, 255))
    screen.blit(input_surface, (input_rect.x + 5, input_rect.y + 5))

            
    button_rect = pygame.Rect(screenWidth - 110, screenHeight - 80, 90, 40)
    pygame.draw.rect(screen, (100, 200, 100), button_rect)

    button_text = defaultFont.render("Search", True, (0, 0, 0))
    screen.blit(button_text, button_text.get_rect(center=button_rect.center))

  
    info = f"Target: {target}   Comparisons: {comparisons}"
    info_surface = defaultFont.render(info, True, (255, 255, 255))
    screen.blit(info_surface, (20, screenHeight - 30))

    pygame.draw.rect(screen, (200, 200, 200), backButton)
    back_text = defaultFont.render("Back", True, (0, 0, 0))
    screen.blit(back_text, back_text.get_rect(center=backButton.center))

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
                if backButton.collidepoint(event.pos):
                    running = False
                    break
                if button_rect.collidepoint(event.pos):

                    try:
                        target = [int(x.strip()) for x in user_input.split(",")]
                    except:
                        target = []

                
            for t in target:
                idx, comparisons = linear_search(t)

                draw_grid(idx, comparisons, t)
                pygame.display.flip()
                time.sleep(1)


        clock.tick(60)


    pygame.quit()


if __name__ == "__main__":
    main()