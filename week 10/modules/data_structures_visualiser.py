import pygame
import sys
from .stack import Stack
from .queue import Queue

WIDTH, HEIGHT = 800, 600
clock = pygame.time.Clock()

BLOCK_WIDTH, BLOCK_HEIGHT = 200, 40
START_X = (WIDTH - BLOCK_WIDTH) // 2
BASE_Y = HEIGHT - BLOCK_HEIGHT - 20



def stack_visualization(screen, font):
   stack = Stack()
   counter = 1
   running = True

   while running:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False
           elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_SPACE:
                   stack.push(counter)
                   counter += 1
               elif event.key == pygame.K_BACKSPACE and not stack.is_empty():
                   stack.pop()
               elif event.key == pygame.K_ESCAPE:
                   running = False

       screen.fill((50, 50, 50))
       for i, val in enumerate(stack._data):
           rect = pygame.Rect(START_X, BASE_Y - i * (BLOCK_HEIGHT + 5), BLOCK_WIDTH, BLOCK_HEIGHT)
           pygame.draw.rect(screen, (100, 150, 250), rect)
           text = font.render(str(val), True, (0, 0, 0))
           text_rect = text.get_rect(center=rect.center)
           screen.blit(text, text_rect)

       info_text = font.render("SPACE: Push, BACKSPACE: Pop, ESC: Return to menu", True, (200, 200, 200))
       screen.blit(info_text, (10, 10))

       pygame.display.flip()
       clock.tick(30)



def queue_visualization(screen, font):
    queue = Queue()
    positions = []
    target_positions = []
    

    enqueue_button = pygame.Rect(300, HEIGHT - 90, 120, 35)
    dequeue_button = pygame.Rect(380, HEIGHT - 90, 120, 35)
    
    counter = 1
    running = True
    
    def update_animation():
        panel_top = HEIGHT - 100
        for i in range(len(positions)):
            target_y = panel_top - (i + 1) * (BLOCK_HEIGHT + 5)
            positions[i] += (target_y - positions[i]) * 0.2
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if enqueue_button.collidepoint(event.pos):
                    queue.enqueue(counter)
                    positions.append(HEIGHT)
                    counter += 1
                if dequeue_button.collidepoint(event.pos) and not queue.is_empty():
                    queue.dequeue()
                    if positions:
                        positions.pop(0)
        
        update_animation()
        
        screen.fill((50, 50, 50))
        
        
        button_bar = pygame.Rect(10, HEIGHT - 100, WIDTH - 20, 100)
        pygame.draw.rect(screen, (0, 128, 0), button_bar)
        
       
        pygame.draw.rect(screen, (180, 180, 180), enqueue_button)
        enq_text = font.render("Enqueue", True, (0, 0, 0))

        screen.blit(enq_text, enq_text.get_rect(center=enqueue_button.center))
        
      
        pygame.draw.rect(screen, (180, 180, 180), dequeue_button)
        deq_text = font.render("Dequeue", True, (0, 0, 0))

        screen.blit(deq_text, deq_text.get_rect(center=dequeue_button.center))
        
      
        for i, val in enumerate(queue.items):
            if i < len(positions):
                rect = pygame.Rect(START_X, positions[i], BLOCK_WIDTH, BLOCK_HEIGHT)
                pygame.draw.rect(screen, (150, 100, 250), rect)
                text = font.render(str(val), True, (0, 0, 0))
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)
        
        info_text = font.render("Click buttons or ESC to return", True, (200, 200, 200))
        screen.blit(info_text, (10, 10))
        
        pygame.display.flip()
        clock.tick(30)






def run(screen):
   font = pygame.font.SysFont(None, 28)

   menu_items = [
       "Stack Visualization (press enter)",
       "Queue Visualization (press enter)",
       "Linked List Visualization (not implemented)",
       "BST Visualization (not implemented)",
       "Back"
   ]
   selected = 0
   running = True
   while running:
       screen.fill((220, 220, 220))
       for i, item in enumerate(menu_items):
           color = (255, 0, 0) if i == selected else (0, 0, 0)
           text = font.render(item, True, color)
           screen.blit(text, (100, 100 + i * 40))

       pygame.display.flip()

       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
           elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_DOWN:
                   selected = (selected + 1) % len(menu_items)
               elif event.key == pygame.K_UP:
                   selected = (selected - 1) % len(menu_items)
               elif event.key == pygame.K_RETURN:
                   choice = menu_items[selected]
                   if choice == "Stack Visualization (press enter)":
                       stack_visualization(screen, font)

                   elif choice == "Queue Visualization (press enter)":
                       queue_visualization(screen, font)

                   elif choice == "Back":
                       running = False

       clock.tick(30)
