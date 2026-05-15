import pygame
import sys
import random
import math

pygame.init()

screenWidth, screenHeight = 800, 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
defaultFont = pygame.font.SysFont(None, 24)
backButton = pygame.Rect(screenWidth - 120, 20, 100, 40)
clock = pygame.time.Clock()

heap = []  
currentMsg = "" 

def draw_heap(heap, highlight_indices=[]):
    screen.fill((255, 255, 255))
    
    status_text = defaultFont.render(f"Status: {currentMsg}", True, (0, 0, 0))
    screen.blit(status_text, (20, 20))

    pygame.draw.rect(screen, (200, 200, 200), backButton)
    back_text = defaultFont.render("Back", True, (0, 0, 0))
    screen.blit(back_text, back_text.get_rect(center=backButton.center))

    if not heap:
        text = defaultFont.render("Heap is empty", True, (0, 0, 0))
        screen.blit(text, (screenWidth // 2 - 60, screenHeight // 2))
        pygame.display.flip()
        return

    levels = int(math.log2(len(heap))) + 1
    node_positions = []

    for i in range(len(heap)):
        level = int(math.floor(math.log2(i + 1)))
        index_in_level = i - (2 ** level - 1)
        gap = screenWidth // (2 ** level + 1)
        x = gap * (index_in_level + 1)
        y = 100 + level * 70 
        node_positions.append((x, y))

    for i in range(len(heap)):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(heap):
            pygame.draw.line(screen, (0, 0, 0), node_positions[i], node_positions[left], 2)

        if right < len(heap):
            pygame.draw.line(screen, (0, 0, 0), node_positions[i], node_positions[right], 2)

    for i, val in enumerate(heap):
        color = (100, 200, 250)
        if i in highlight_indices:
            color = (255, 100, 100)
        
        pygame.draw.circle(screen, color, node_positions[i], 20)
        
        display_val = str(val[0]) 
        text = defaultFont.render(display_val, True, (0, 0, 0))
        text_rect = text.get_rect(center=node_positions[i])
        screen.blit(text, text_rect)

    pygame.display.flip()

def heapify_up(heap, index):
    while index > 0:
        parent = (index - 1) // 2
        if heap[parent][0] > heap[index][0]:
            heap[parent], heap[index] = heap[index], heap[parent]
            draw_heap(heap, [parent, index])
            pygame.time.wait(400)
            index = parent
        else:
            break

def heapify_down(heap, index):
    n = len(heap)
    while True:
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < n and heap[left][0] < heap[smallest][0]:
            smallest = left

        if right < n and heap[right][0] < heap[smallest][0]:
            smallest = right

        if smallest != index:
            heap[index], heap[smallest] = heap[smallest], heap[index]
            draw_heap(heap, [index, smallest])
            pygame.time.wait(400)
            index = smallest

        else:
            break


def insert(heap, event):
    heap.append(event)
    draw_heap(heap, [len(heap) - 1])
    pygame.time.wait(300)
    heapify_up(heap, len(heap) - 1)



def extract_min(heap):
    global currentMsg
    if len(heap) == 0:
        return None

    event_time, event_description = heap[0]
    currentMsg = f"{event_description} (at T={event_time})"
    
    if len(heap) > 1:
        heap[0] = heap[-1]
        heap.pop()
        draw_heap(heap, [0])
        pygame.time.wait(600)
        heapify_down(heap, 0)

    else:
        heap.pop()
    
    return (event_time, event_description)




def main():
    global currentMsg
    running = True


    events = [
        (12, "Email sync"), (5, "System boot"), (20, "Virus scan"), 
        (8, "Software update"), (15, "Cloud backup"), (3, "User login")
    ]


    random.shuffle(events)
    idx = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if backButton.collidepoint(event.pos):
                    running = False
                    break

        if idx < len(events):

            t, desc = events[idx]
            currentMsg = f"{desc} for T={t}"
            insert(heap, events[idx])
            idx += 1
            pygame.time.wait(600)

        else:
            pygame.time.wait(1000)
            if heap:
                extract_min(heap)


            else:
                draw_heap(heap)
                pygame.time.wait(2000)
                running = False

        draw_heap(heap)
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()