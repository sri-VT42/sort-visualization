import pygame
import colors

class Button:
    """ 
    This is a class to represent a button in pygame.
      
    Attributes: 
        color (tuple): The color of the button. 
        color_h (int): The color of the button when it is hovered over. 
        x (int): The x-position of the button.
        y (int): The y-position of the button.
        width (int): The width of the button.
        height (int): The height of the button.
        text (string): The text to be displayed on the button. 
    """

    def __init__(self, color, color_h, x, y, width, height, text=''):
        """ 
        The constructor for the Button class.
  
        Parameters: 
            color (tuple): The color of the button. 
            color_h (int): The color of the button when it is hovered over. 
            x (int): The x-position of the button.
            y (int): The y-position of the button.
            width (int): The width of the button.
            height (int): The height of the button.
            text (string): The text to be displayed on the button.     
        """

        self.color = color
        self.color_h = color_h
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
    
    def draw(self, win):
        """ 
        Draws the Menu to the screen. 
  
        Parameters: 
            win (pygame.display): The display to render the menu to. 
        """

        pygame.init()

        mouse_pos = pygame.mouse.get_pos()
        
        # Check whether the mouse is on the Button. If so, then draw it in the highlighted color.
        if self.is_over(mouse_pos):
            pygame.draw.rect(win, self.color_h, (self.x,self.y,self.width,self.height), 0)
        else:
            pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height), 0)
        
        # Draw the text onto the button.
        if self.text != '':
            font = colors.FONT()
            text = font.render(self.text, 1, colors.WHITE)
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2) + 2))

    def is_over(self, pos):
        """ 
        Checks whether a given pair of mouse coordinates are over the button. 
  
        Parameters: 
            pos (tuple): A tuple of mouse coordinates.
          
        Returns: 
            boolean: Whether the mouse coordinates are over the button.
        """

        # Simple check to see if a pair of given coordinates are inside boundaries of the button.
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False