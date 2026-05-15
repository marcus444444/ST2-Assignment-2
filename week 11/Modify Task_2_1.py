import pygame
import sys

pygame.init()


WIDTH, HEIGHT = 1000, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont(None, 30)
clock = pygame.time.Clock()

NODE_RADIUS = 25



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)



    def insert_at(self, value, pos):
        new_node = Node(value)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        count = 0
        while current and count < pos - 1:
            current = current.next
            count += 1
        
        if current:
            new_node.next = current.next
            current.next = new_node




    def delete(self, value):
        current = self.head
        prev = None
        while current:
            if current.value == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False




    def delete_head(self):
        if self.head:
            self.head = self.head.next

    def to_list(self):
        elems = []
        current = self.head
        while current:
            elems.append(current.value)
            current = current.next
        return elems




def draw_node(x, y, value, highlight=False):
    color = (255, 100, 100) if highlight else (100, 200, 250)
    pygame.draw.circle(screen, color, (x, y), NODE_RADIUS)
    # Added a border for better visibility
    pygame.draw.circle(screen, (0, 0, 0), (x, y), NODE_RADIUS, 2)
    text = FONT.render(str(value), True, (0, 0, 0))
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)



def draw_arrow(start_pos, end_pos):
    pygame.draw.line(screen, (0, 0, 0), start_pos, end_pos, 3)
    # Simple arrowhead
    pygame.draw.circle(screen, (0, 0, 0), end_pos, 5)





def draw_linked_list(linked_list, highlight_index=None):
    screen.fill((240, 240, 240))
    
    instr = FONT.render("A: Append | D: Delete Head | I: Insert pos 1 | R: Reverse", True, (50, 50, 50))
    screen.blit(instr, (20, 20))
    
    nodes = []
    current = linked_list.head
    x, y = 80, HEIGHT // 2
    idx = 0
    while current:
        nodes.append((x, y, current.value, idx == highlight_index))
        x += 150
        current = current.next
        idx += 1

    for i, (x, y, val, highlight) in enumerate(nodes):
        if i < len(nodes) - 1:
            draw_arrow((x + NODE_RADIUS, y), (x + 150 - NODE_RADIUS, y))
        draw_node(x, y, val, highlight)
    
    pygame.display.flip()






def animate_reverse(ll):
    prev = None
    current = ll.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        
        temp_head = ll.head
        ll.head = prev
        draw_linked_list(ll)
        pygame.time.wait(600)
        
        current = next_node
    ll.head = prev




def main():
    ll = LinkedList()
    next_val = 5
    


    for _ in range(3):
        ll.append(next_val)
        next_val += 5

    while True:
        draw_linked_list(ll)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:  
                    ll.append(next_val)
                    next_val += 5
                
                elif event.key == pygame.K_d:  
                    ll.delete_head()
                
                elif event.key == pygame.K_i:  
                    ll.insert_at(next_val, 1)
                    next_val += 5
                
                elif event.key == pygame.K_r:  
                    animate_reverse(ll)

        clock.tick(30)

if __name__ == '__main__':
    main()