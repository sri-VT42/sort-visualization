import pygame
import colors

class DropMenu:
    """ 
    This is a class for drop-down menus in pygame. 
      
    Attributes: 
        color (tuple): The color of the drop-down. 
        color_h (int): The color of the drop-down when it is hovered over. 
        x (int): The x-position of the menu.
        y (int): The y-position of the menu.
        width (int): The width of the menu.
        height (int): The height of the menu.
        states (list): The list of options in the menu.
        box_coords (list): The list of the coordinates of the boxes that show the options.
        clicked (boolean): Flag to check whether the menu is on focus or not.
        current_state (string): The current option displayed on the menu.
    """

    def __init__(self, color, color_h, x, y, width, height, states):
        """ 
        The constructor for the DropMenu class. 
  
        Parameters: 
            color (tuple): The color of the drop-down. 
            color_h (int): The color of the drop-down when it is hovered over. 
            x (int): The x-position of the menu.
            y (int): The y-position of the menu.
            width (int): The width of the menu.
            height (int): The height of the menu.
            states (list): The list of options in the menu.    
        """

        self.color = color
        self.color_h = color_h
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.states = states
        self.box_coords = [(x, y - i * self.height, self.width, self.height) for i in range(len(states))]
        self.clicked = False
        self.current_state = self.states[0]
    
    def draw(self,win):
        """ 
        Draws the DropMenu to the screen. 
  
        Parameters: 
            win (pygame.display): The display to render the menu to. 
        """

        pygame.init()

        mouse_pos = pygame.mouse.get_pos()

        # Check whether the mouse is on the main box. If so, then draw it in the highlighted color.
        if self.is_over(mouse_pos):
            pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height), 0)
        else:
            pygame.draw.rect(win, self.color_h, (self.x,self.y,self.width,self.height), 0)
        
        
        
        # Draw the current state onto the main box.
        if self.current_state != '':
            font = colors.FONT()
            text = font.render(self.current_state, 1, colors.WHITE)
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2) - 15, self.y + (self.height/2 - text.get_height()/2) + 2))
            coord_1 = (self.x + (self.width - 21), self.y + 5 * self.height / 8)
            coord_2 = (self.x + (self.width - 16), self.y + 3 * self.height / 8)
            coord_3 = (self.x + (self.width - 11), self.y + 5 * self.height / 8)
            pygame.draw.polygon(win, colors.WHITE, (coord_1, coord_2, coord_3))
            pygame.draw.line(win, colors.WHITE, (self.x + (self.width - 30), self.y + 5), (self.x + (self.width - 30), self.y + self.height - 5), 2)
        
        # If the DropMenu is active, then draw the rest of the options to the screen.
        if self.clicked:
            mouse_pos = pygame.mouse.get_pos()

            for i in range(1, len(self.states)):
                if self.is_over_coords(mouse_pos, self.box_coords[i]):
                    pygame.draw.rect(win, self.color, self.box_coords[i], 0)
                else:
                    pygame.draw.rect(win, self.color_h, self.box_coords[i], 0)
                
                if self.current_state != '':
                    font = colors.FONT()
                    text = font.render(self.states[i], 1, colors.WHITE)
                    win.blit(text, (self.box_coords[i][0] + (self.box_coords[i][2]/2 - text.get_width()/2), self.box_coords[i][1] + (self.box_coords[i][3]/2 - text.get_height()/2) + 2))

    def handle_click(self):
        """ 
        Handles mouse clicks. Whenever the mouse is clicked, this method will be called to check where and act accordingly. 
        """

        # If the mouse is on the main box, it will toggle from active to not active.
        if self.is_over(pygame.mouse.get_pos()):
            self.clicked = not self.clicked
        # If it is active, then it sets the current_state of the menu to the selected one.
        if self.clicked:
            for i in range(1, len(self.states)):
                box = self.box_coords[i]
                if self.is_over_coords(pygame.mouse.get_pos(), box):
                    self.current_state = self.states[i]
                    self.states[i], self.states[0] = self.states[0], self.states[i]
                    self.clicked = not self.clicked

    def is_over(self, pos):
        """ 
        Checks whether a given pair of mouse coordinates are in the main box of the menu. 
  
        Parameters: 
            pos (tuple): A tuple of mouse coordinates.
          
        Returns: 
            boolean: Whether the mouse coordinates are in the main box.
        """
        
        # Simple check to see if a pair of given coordinates are inside the main box.
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False
    
    def is_over_coords(self, pos, coords):
        """ 
        Checks whether the mouse is above any given box. Used to check if the mouse is above any of the other squares when the menu is active. 
  
        Parameters: 
            pos (tuple): A tuple of mouse coordinates.
            coords (tuple): A tuple of coordinates specifying the box to check 
          
        Returns: 
            boolean: Whether the mouse coordinates are in the given box.
        """

        # Simple check to see if a pair of given coordinates are inside any given box.
        if pos[0] > coords[0] and pos[0] < coords[0] + coords[2]:
            if pos[1] > coords[1] and pos[1] < coords[1] + coords[3]:
                return True
            
        return False
