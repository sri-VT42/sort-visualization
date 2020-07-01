import pygame

# Defines the colors used in the interface.
GRAY = (30, 30, 30)
BLUE = (24, 116, 205)
DARK_BLUE = (16, 78, 139)
WHITE = (255, 255, 255)

pygame.init()

def FONT(size=40):
    """ 
        Creates a pygame font of a certain size.
  
        Parameters: 
           size (int): The size of the font. 
        """

    return pygame.font.Font(None, size)
