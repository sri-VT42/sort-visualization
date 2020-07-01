import pygame
import colors

class Label:
    """ 
    This is a class to represent a label in pygame.
      
    Attributes: 
        color (tuple): The color of the label. 
        x (int): The x-position of the label.
        y (int): The y-position of the label.
        width (int): The width of the label.
        height (int): The height of the label.
        text (string): The text to be displayed on the label. 
    """
    def __init__(self, color, x, y, width, height, text=''):
        """ 
        The constructor for the Label class. 
  
        Parameters: 
            color (tuple): The color of the label. 
            x (int): The x-position of the label.
            y (int): The y-position of the label.
            width (int): The width of the label.
            height (int): The height of the label.
            text (string): The text to be displayed on the label.    
        """

        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
    
    def draw(self, win):
        """ 
        Draws the Label to the screen. 
  
        Parameters: 
            win (pygame.display): The display to render the menu to. 
        """

        pygame.init()

        # The background    
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        # The text
        if self.text != '':
            font = colors.FONT(20)
            text = font.render(self.text, 1, colors.WHITE)
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2) + 2))

    def update_text(self, new_text):
        """ 
        Updates the text to be displayed. 
  
        Parameters: 
            new_text (string): The new value of the text to be displayed. 
        """
        self.text = new_text