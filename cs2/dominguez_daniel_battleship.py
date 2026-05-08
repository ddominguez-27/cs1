
"""
Battleship PyGame
Author: Daniel Dominguez
Date: 5/8/26
Sources: Battleship spec, https://www.pygame.org/docs/ref/mouse.html, oliver helped me with a lot of the grid pygame, and some other stuff
Description:  Allows a battleship game between two players, where each player sets up their board with 5 ships on a 5x5 grid and take turns attacking until all ships are cleared and a player is declared the victor
Log: 1.0

"""


#setup code
import pygame
pygame.init()

width, height = 500, 500
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

cell_size = 100
grid_size = 5     



def place_ships(player, grid):

# Args:
#     player (str), grid (list of lists)
# Return:
#     grid (list of lists)
# Description: 
#    allows player to select 5 squares using the pygame interface which updates the grid variable



        
    running = True
    while running:


        counter = 0
        for row in grid:    #for loop counts how many ships have been placed
            for i in row:
                if i == 1:
                    counter += 1   
        pygame.display.set_caption(f"{player} turn! Press the grid spaces to place 5 battleships")

        screen.fill((0, 0, 0))     #starts with black screen

        for event in pygame.event.get():   
            if event.type == pygame.QUIT:
                running = False

            
            if event.type == pygame.MOUSEBUTTONDOWN:   
                x, y = pygame.mouse.get_pos()    #gets the mouse position then finds the collumn and row based on the closest divisor to 100
                col = x // cell_size
                row = y // cell_size

                if counter < 5 or grid[row][col] == 1:
                    grid[row][col] = 1 - grid[row][col]  # toggles the spot between 0 and 1
                else:
                    return(grid)
                

        for row in range(grid_size):
            for col in range(grid_size):

                x = col * cell_size     
                y = row * cell_size

                if (grid[row][col] == 1):
                    color = (128, 128, 128)   #cell with ship
                else:
                    color = ((14, 135, 204))  # empty cell

                pygame.draw.rect(screen, color, (x, y, cell_size, cell_size))
                pygame.draw.rect(screen, (255, 255, 255), (x, y, cell_size, cell_size), 1)

        
        



        pygame.display.flip()
        clock.tick(30)
    return

def attack_board(player, grid):


# Args:
#     player (str), grid (list of lists)
# Return:
#     grid (list of lists)
# Description: 
#    lets player select a square to target resulting in either a hit ship or a missed square updating the grid variable correspondingly


    counter = 0
            
    running = True
    while running:



        pygame.display.set_caption(f"{player} turn! Press a blue grid space to fire at the board")

        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            
            if event.type == pygame.MOUSEBUTTONDOWN and counter < 1:   #triggers when mouse is pressed and makes sure the user hasnt moved yet
                x, y = pygame.mouse.get_pos()
                col = x // cell_size
                row = y // cell_size


                if grid[row][col] == 1:
                    grid[row][col] = 3  #3 is hit 
                    counter += 1
                elif grid[row][col] == 0:
                    grid[row][col] = 2 #2 is missed
                    counter += 1
                elif grid[row][col] == 2 or grid[row][col] == 3:  #if they try to press an hit square
                    continue






                

        for row in range(grid_size):
            for col in range(grid_size):

                x = col * cell_size
                y = row * cell_size

                if (grid[row][col] == 1) or (grid[row][col] == 0):
                    color = ((14, 135, 204))   #water cell or hidden ship cell (blue)
                elif (grid[row][col] == 3):
                    color = ((194, 24, 7))  #red color for ship hit
                elif (grid[row][col] == 2):
                    color = (0, 0, 139)  #dark blue color for miss water


                pygame.draw.rect(screen, color, (x, y, cell_size, cell_size))
                pygame.draw.rect(screen, (255, 255, 255), (x, y, cell_size, cell_size), 1)




        
        
        if counter > 0:     #if the player has already pressed a square
            pygame.display.set_caption("Launching attack...")
            pygame.display.flip()
            clock.tick(30)
            pygame.time.wait(1500)
            return grid
        
        else:
            pygame.display.flip()
            clock.tick(30)
    return

def windetection(grid):

# Args:
#     grid (list of lists)
# Return:
#     bool
# Description: 
#    checks the grid variable for any 1s (unhit ships still on the board) and returns either true or false

    for row in grid:
        for i in row:
            if i == 1:
                return False
    return True


def passscreen(player):


# Args:
#     player (str)
# Return:
#     n/a
# Description: 
#    blank screen so players can pass device without revealing more information than needed

    pygame.event.clear()
    running = True
    font = pygame.font.Font(None, 32)
    text_surface = font.render(f'Please pass the device to {player}', True, (255, 255, 255))
    pygame.display.set_caption("Click on the screen to continue")



    while running:
        screen.fill((0, 0, 0))  # sets black screen
        screen.blit(text_surface, (80, 200))

        pygame.display.flip()
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:   #continues when screen is clicked
                return






def playerwin(player):


# Args:
#     player (str)
# Return:
#     n/a
# Description: 
#    final win screen which shows board and lets players see who won

    pygame.event.clear()
    running = True
    font = pygame.font.Font(None, 56)
    text_surface = font.render(f'{player} wins!', True, (255, 255, 255))
    pygame.display.set_caption("Game over")



    while running:
        screen.blit(text_surface, (80, 200))

        pygame.display.flip()
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return



def main():


# Args:
#     n/a
# Return:
#     n/a
# Description: 
#   main function which runs battleship using all the functions
#   starts with board setup into a loop which alternates attacks between players and checks for wins
    
    p1_board_base = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    p1_board = place_ships("Player 1", p1_board_base)

    passscreen("Player 2")


    p2_board_base = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    p2_board = place_ships("Player 2", p2_board_base)

    passscreen("Player 1")



    while True:    
        p2_board = attack_board("Player 1", p2_board)
        if windetection(p2_board):
            playerwin("Player 1")
            return
        passscreen("Player 2")

        p1_board = attack_board("Player 2", p1_board)
        if windetection(p1_board):
            playerwin("Player 2")
            return
        passscreen("Player 1")


        



main()
pygame.quit()
