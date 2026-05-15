import pygame
import sys
import collections

pygame.init()

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont(None, 24)
clock = pygame.time.Clock()

# Graph nodes positioned manually
nodes_pos = {
    'A': (100, 100),
    'B': (250, 60),
    'C': (250, 200),
    'D': (400, 100),
    'E': (500, 150),
    'F': (400, 300)
}

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

traversal_order = []

def draw_graph(visited=set(), frontier=set(), current=None, mode_text=""):
    screen.fill((240, 240, 240))

    # Draw instructions and Traversal Order
    draw_ui(mode_text)

    # Draw edges
    for node, neighbors in graph.items():
        x1, y1 = nodes_pos[node]
        for n in neighbors:
            x2, y2 = nodes_pos[n]
            pygame.draw.line(screen, (0, 0, 0), (x1, y1), (x2, y2), 2)

    # Draw nodes
    for node, (x, y) in nodes_pos.items():
        color = (200, 200, 200) 

        if node in visited:
            color = (100, 200, 100) 
        if node in frontier:
            color = (255, 200, 100) 
        if node == current:
            color = (255, 100, 100) 

        pygame.draw.circle(screen, color, (x, y), 25)
        text = FONT.render(node, True, (0, 0, 0))
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)
    
    pygame.display.flip()



def draw_ui(mode_text):
   

    instruction = FONT.render("Left click: BFS | Right click: DFS", True, (0, 0, 0))
    mode = FONT.render(f"Running: {mode_text}", True, (0, 0, 0))
    order_title = FONT.render("Traversal order:", True, (0, 0, 0))
    order_text = FONT.render(" -> ".join(traversal_order), True, (0, 0, 150))
    
    screen.blit(instruction, (20, 20))
    screen.blit(mode, (20, 45))
    screen.blit(order_title, (20, HEIGHT - 60))
    screen.blit(order_text, (20, HEIGHT - 35))

def get_node_at_pos(pos):
    """Returns the node name if a click is within a node's circle."""
    for node, (x, y) in nodes_pos.items():
        dist = ((x - pos[0])**2 + (y - pos[1])**2)**0.5
        if dist <= 25:
            return node
    return None

def bfs(start):
    global traversal_order
    traversal_order = []
    visited = set()
    queue = collections.deque([start])
    in_queue = {start} 

    while queue:
        current = queue.popleft()
        if current not in visited:
            visited.add(current)
            traversal_order.append(current)

            draw_graph(visited=visited, frontier=set(queue), current=current, mode_text="BFS")
            pygame.time.wait(700)

            for neighbor in graph[current]:
                if neighbor not in visited and neighbor not in in_queue:
                    queue.append(neighbor)
                    in_queue.add(neighbor)
        
        handler()

def dfs(start):
    global traversal_order
    traversal_order = []
    visited = set()
    stack = [start]

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            traversal_order.append(current)

            draw_graph(visited=visited, frontier=set(stack), current=current, mode_text="DFS")
            pygame.time.wait(700)

            for neighbor in reversed(graph[current]):
                if neighbor not in visited:
                    stack.append(neighbor)
        
        handler()


def handler():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()




def main():
    running = True

    while running:
        draw_graph()
        
        for event in pygame.event.get():
     
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


            if event.type == pygame.MOUSEBUTTONDOWN:
                node = get_node_at_pos(event.pos)

                if node:
                    if event.button == 1: 
                        bfs(node)

                    elif event.button == 3: 
                        dfs(node)

  

if __name__ == "__main__":
    main()