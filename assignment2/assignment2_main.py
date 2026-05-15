import os
import importlib.util
import pygame
import sys

pygame.init()
screenWidth, screenHeight = 800, 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
defaultFont = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()
moduleDir = os.path.join(os.path.dirname(__file__), "modules to encorperate")


def load_module_from_path(path, module_name):
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def run_submodule(module_filename, module_name):
    global screen
    path = os.path.join(moduleDir, module_filename)
    module = load_module_from_path(path, module_name)

    try:
        module.main()
    except SystemExit:
        pass

    pygame.init()
    screen = pygame.display.set_mode((screenWidth, screenHeight))


def draw_text(text, pos):
    surface = defaultFont.render(text, True, (0, 0, 0))
    screen.blit(surface, pos)


def draw_buttons(buttons):
    for text, rect in buttons.items():
        pygame.draw.rect(screen, (150, 150, 200), rect)
        draw_text(text, (rect.x + 20, rect.y + 10))


def menu_loop(title, buttons, background=(200, 200, 250)):
    while True:
        screen.fill(background)
        draw_text(title, (screenWidth // 3, 50))
        draw_buttons(buttons)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                for name, rect in buttons.items():
                    if rect.collidepoint(pos):
                        return name


def main():
    main_buttons = {
        'Data Structures': pygame.Rect(300, 150, 200, 50),
        'Sorting': pygame.Rect(300, 230, 200, 50),
        'Graphs': pygame.Rect(300, 310, 200, 50),
        'Heap': pygame.Rect(300, 390, 200, 50),
        'Puzzles': pygame.Rect(300, 470, 200, 50),
    }

    data_buttons = {
        'Stack / Queue': pygame.Rect(250, 150, 300, 50),
        'Linked List': pygame.Rect(250, 220, 300, 50),
        'Binary Search Tree': pygame.Rect(250, 290, 300, 50),
        'Linear Search': pygame.Rect(250, 360, 300, 50),
        'Back': pygame.Rect(250, 430, 300, 50),
    }

    data_module_map = {
        'Stack / Queue': ('modify task_1_2.py', 'modify_task_1_2'),
        'Linked List': ('Modify Task_2_1.py', 'modify_task_2_1'),
        'Binary Search Tree': ('Modify Task_2_2.py', 'modify_task_2_2'),
        'Linear Search': ('Modify Task_1_1.py', 'modify_task_1_1'),
    }

    while True:
        selection = menu_loop('Algorithm Explorer', main_buttons)

        if selection == 'Data Structures':
            submenu = menu_loop('Data Structures', data_buttons, background=(200, 220, 200))
            if submenu == 'Back':
                continue
            module_info = data_module_map.get(submenu)
            if module_info:
                run_submodule(*module_info)

        elif selection == 'Sorting':
            run_submodule('Modify Task_2_3.py', 'modify_task_2_3')

        elif selection == 'Graphs':
            run_submodule('task_3_1.py', 'task_3_1')

        elif selection == 'Heap':
            run_submodule('task_3.2.py', 'task_3_2')

        elif selection == 'Puzzles':
            run_submodule('task_3.3.py', 'task_3_3')

        clock.tick(30)


if __name__ == '__main__':
    main()
