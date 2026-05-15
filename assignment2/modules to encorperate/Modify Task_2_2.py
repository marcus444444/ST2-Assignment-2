import pygame
import sys

pygame.init()

screenWidth, screenHeight = 800, 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
defaultFont = pygame.font.SysFont(None, 30)
clock = pygame.time.Clock()
backButton = pygame.Rect(screenWidth - 120, 20, 100, 40)

nodeRadius = 20


class BSTNode:
    def __init__(self, value):
       self.value = value
       self.left = None
       self.right = None


class BST:
    def __init__(self):
       self.root = None

    def insert(self, value):
       def _insert(node, value):
           if not node:
               return BSTNode(value)
           if value < node.value:
               node.left = _insert(node.left, value)
           elif value > node.value:
               node.right = _insert(node.right, value)
           return node

       self.root = _insert(self.root, value)

    def inorder(self):
       result = []

       def _inorder(node):
           if node:
               _inorder(node.left)
               result.append(node)
               _inorder(node.right)

       _inorder(self.root)
       return result


    def preorder(self):
            result = []

            def preorder1(node):
                if node:
                    result.append(node)
                    preorder1(node.left)
                    preorder1(node.right)

            preorder1(self.root)
            return result


    def postorder(self):
        result = []

        def postorder1(node):
            if node:
                postorder1(node.left)
                postorder1(node.right)
                result.append(node)

        postorder1(self.root)
        return result

    def get_search_path(self, value):
            path = []
            current = self.root

            while current:
                path.append(current)
                if value == current.value:
                    return path
                
                elif value < current.value:
                    current = current.left
                
                else:
                    current = current.right
                    
            return []


    def delete(self, value):
            
            def min_value_node(node):
                current = node
                while current.left:
                    current = current.left
                return current

            def delete(node, value):
                if not node: 
                    return node

                if value < node.value:
                    node.left = delete(node.left, value)


                elif value > node.value:
                    node.right = delete(node.right, value)


                else:
                    if not node.left: return node.right
                    elif not node.right: return node.left

                    temp = min_value_node(node.right)
                    node.value = temp.value
                    node.right = delete(node.right, temp.value)
                return node
            
            self.root = delete(self.root, value)



def draw_node(x, y, value, highlight=False, search_highlight=False):
    color = (100, 200, 250)


    if highlight: 
        color = (255, 0, 0)

    if search_highlight: 
        color = (0, 255, 0) 
    
    pygame.draw.circle(screen, color, (x, y), nodeRadius)
    pygame.draw.circle(screen, (0, 0, 0), (x, y), nodeRadius, 2)
    text = defaultFont.render(str(value), True, (0, 0, 0))
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)


def draw_edge(start_pos, end_pos, in_path=False):
    color = (0, 255, 0) if in_path else (0, 0, 0)
    width = 5 if in_path else 3
    pygame.draw.line(screen, color, start_pos, end_pos, width)





def draw_tree(node, x, y, x_offset, search_path=[]):
    if node:
      
        if node.left:
            in_path = node in search_path and node.left in search_path
            draw_edge((x, y), (x - x_offset, y + 80), in_path)
            draw_tree(node.left, x - x_offset, y + 80, x_offset // 2, search_path)


        if node.right:
            in_path = node in search_path and node.right in search_path
            draw_edge((x, y), (x + x_offset, y + 80), in_path)
            draw_tree(node.right, x + x_offset, y + 80, x_offset // 2, search_path)
        
        is_search = node in search_path
        draw_node(x, y, node.value, search_highlight=is_search)





def main():
    bst = BST()
    initial_values = [50, 30, 70, 20, 40, 60, 80]
    for v in initial_values: bst.insert(v)

    traversal_mode = "In-order"
    current_traversal = bst.inorder()
    search_path = []
    
    running = True
    highlight_idx = 0

    while running:
        screen.fill((240, 240, 240))
        
       
        mode_text = defaultFont.render(f"Mode (T): {traversal_mode}", True, (50, 50, 50))
        ctrl_text = defaultFont.render("S: Search 20 | D: Delete 30 | T: Cycle Traversal", True, (80, 80, 80))
        screen.blit(mode_text, (20, 20))
        screen.blit(ctrl_text, (20, 50))

  
        draw_tree(bst.root, screenWidth // 2, 120, 150, search_path)
        
        pygame.draw.rect(screen, (200, 200, 200), backButton)
        back_text = defaultFont.render("Back", True, (0, 0, 0))
        screen.blit(back_text, back_text.get_rect(center=backButton.center))

        if highlight_idx < len(current_traversal):
            node_to_hl = current_traversal[highlight_idx]
  

            def highlight_recursive(node, x, y, x_offset):
                if node:
                    if node == node_to_hl:
                        draw_node(x, y, node.value, highlight=True)
                    highlight_recursive(node.left, x - x_offset, y + 80, x_offset // 2)
                    highlight_recursive(node.right, x + x_offset, y + 80, x_offset // 2)
            highlight_recursive(bst.root, screenWidth // 2, 120, 150)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if backButton.collidepoint(event.pos):
                    running = False
                    break

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_t: 
                    highlight_idx = 0
                    search_path = []

                    if traversal_mode == "In-order":
                        traversal_mode = "Pre-order"
                        current_traversal = bst.preorder()


                    elif traversal_mode == "Pre-order":
                        traversal_mode = "Post-order"
                        current_traversal = bst.postorder()

                    else:
                        traversal_mode = "In-order"
                        current_traversal = bst.inorder()
                

                if event.key == pygame.K_s: 
                    search_path = bst.get_search_path(70)
                
                if event.key == pygame.K_d: 
                    bst.delete(30)
                   

                    if traversal_mode == "In-order": current_traversal = bst.inorder()
                    elif traversal_mode == "Pre-order": current_traversal = bst.preorder()
                    else: current_traversal = bst.postorder()
                    highlight_idx = 0

        pygame.display.flip()
        clock.tick(2) 
        
        if not search_path: 
            highlight_idx += 1
            if highlight_idx >= len(current_traversal):
                highlight_idx = 0

    pygame.quit()

if __name__ == "__main__":
    main()
