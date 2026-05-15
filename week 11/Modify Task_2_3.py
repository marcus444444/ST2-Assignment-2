import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont(None, 24)
clock = pygame.time.Clock()

ARRAY_SIZE = 30
array = [random.randint(10, 350) for _ in range(ARRAY_SIZE)]
bar_width = WIDTH // ARRAY_SIZE




def draw_array(array, color_positions=None):
    screen.fill((30, 30, 30))

    pygame.draw.rect(screen, (255, 255, 255), (0, 0, WIDTH, 50))
    
    text_line = "B: Bubble | S: Selection | M: Merge | R: Reset"
    text_surface = FONT.render(text_line, True, (0, 0, 0))

    text_rect = text_surface.get_rect(center=(WIDTH // 2, 30))
    screen.blit(text_surface, text_rect)

    for i, val in enumerate(array):
       color = (100, 200, 250)

       if color_positions and i in color_positions['compare']:
           color = (255, 100, 100)

       if color_positions and i in color_positions['swap']:
           color = (100, 255, 100)


       pygame.draw.rect(screen, color, (i * bar_width, HEIGHT - val, bar_width - 2, val))

    pygame.display.flip()


def bubble_sort_visualize(array):
   n = len(array)

   for i in range(n):
       

       for j in range(0, n - i - 1):
           draw_array(array, {'compare': [j, j + 1], 'swap': []})
           pygame.time.wait(50)


           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   pygame.quit()
                   sys.exit()


           if array[j] > array[j + 1]:
               array[j], array[j + 1] = array[j + 1], array[j]
               draw_array(array, {'compare': [], 'swap': [j, j + 1]})
               pygame.time.wait(50)
   draw_array(array)


def selection_sort_visualize(array):
    n = len(array)


    for i in range(n):
        min_idx = i


        for j in range(i + 1, n):
            draw_array(array, {'compare': [j, min_idx], 'swap': []})
            pygame.time.wait(20)


            if array[j] < array[min_idx]:
                min_idx = j


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
        array[i], array[min_idx] = array[min_idx], array[i]
        draw_array(array, {'compare': [], 'swap': [i, min_idx]})
        pygame.time.wait(50)



def merge_sort_visualize(array, l, r):
    if l < r:
        mid = (l + r) // 2
        merge_sort_visualize(array, l, mid)
        merge_sort_visualize(array, mid + 1, r)
        
        left = array[l:mid + 1]
        right = array[mid + 1:r + 1]
        i = j = 0
        k = l
        
        while i < len(left) and j < len(right):
            draw_array(array, {'compare': [k], 'swap': list(range(l, r + 1))})
            pygame.time.wait(40)
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1






def main():
    global array
    


    while True:
        draw_array(array)
        
        for event in pygame.event.get():
         
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_b:
                    bubble_sort_visualize(array)

                elif event.key == pygame.K_s:
                    selection_sort_visualize(array)

                elif event.key == pygame.K_m:
                    merge_sort_visualize(array, 0, len(array) - 1)

                elif event.key == pygame.K_r:
                    array = [random.randint(10, 350) for _ in range(ARRAY_SIZE)]

    pygame.quit()


if __name__ == "__main__":
   main()
