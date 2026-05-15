import pygame
import sys

pygame.init()

screenWidth, screenHeight = 1000, 900
rowCount, colCount = 6, 6
gridMarginTop = 100
cellSize = min((screenWidth - 40) // colCount, (screenHeight - gridMarginTop - 40) // rowCount)
gridStartX = (screenWidth - cellSize * colCount) // 2
gridStartY = gridMarginTop
screen = pygame.display.set_mode((screenWidth, screenHeight))
defaultFont = pygame.font.SysFont(None, 30)
backButton = pygame.Rect(screenWidth - 120, 20, 100, 40)
clock = pygame.time.Clock()

grid_layout = [[0 for _ in range(colCount)] for _ in range(rowCount)]

grid_layout[0][1] = -1
grid_layout[2][2] = -1
grid_layout[4][3] = -1
grid_layout[3][4] = -1
grid_layout[5][2] = -1



def draw_grid(dp, highlight=None, path=[]):
    screen.fill((255, 255, 255))
    
    title = defaultFont.render("Dynamic Programming Path", True, (0, 0, 0))
    screen.blit(title, (20, 20))

    
    for r in range(rowCount):
        for c in range(colCount):
            x = gridStartX + c * cellSize
            y = gridStartY + r * cellSize
            rect = pygame.Rect(x, y, cellSize, cellSize)
            
                            
            if grid_layout[r][c] == -1:
                color = (50, 50, 50)

            elif (r, c) in path:
                color = (150, 255, 150)

            elif highlight == (r, c):
                color = (255, 180, 180)

            else:
                color = (230, 230, 230)
            
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)

            val = dp[r][c]

            if val is not None and grid_layout[r][c] != -1:
                text = defaultFont.render(str(val), True, (0, 0, 0))
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)

    pygame.display.flip()


def count_paths():
   dp = [[None] * colCount for _ in range(rowCount)]
   for r in range(rowCount):
       
       for c in range(colCount):
           if r == 0 and c == 0:
               dp[r][c] = 1

           else:
               up = dp[r - 1][c] if r > 0 else 0
               left = dp[r][c - 1] if c > 0 else 0
               dp[r][c] = up + left
           draw_grid(dp, (r, c))

           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   pygame.quit()
                   sys.exit()


               if event.type == pygame.MOUSEBUTTONDOWN and backButton.collidepoint(event.pos):
                   return None
               

           pygame.time.wait(300)
   return dp[rowCount - 1][colCount - 1]




def main():
   start_time = pygame.time.get_ticks()
   
   while pygame.time.get_ticks() - start_time < 1000:
       draw_grid([[None] * colCount for _ in range(rowCount)])
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
           if event.type == pygame.MOUSEBUTTONDOWN and backButton.collidepoint(event.pos):
               return
       clock.tick(30)

   total_paths = count_paths()
   if total_paths is None:
       return
   print(f"Total unique paths: {total_paths}")
   pygame.time.wait(3000)
   pygame.quit()

if __name__ == "__main__":
   main()
