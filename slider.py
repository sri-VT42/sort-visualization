import os
import pygame, sys
import colors

class Slider:
    """ 
    This is a class to represent a slider input in pygame.
      
    Attributes: 
        color (tuple): The color of the slider. 
        color_h (int): The color of the slider when it is hovered over. 
        x (int): The x-position of the slider.
        y (int): The y-position of the slider.
        width (int): The width of the slider.
        height (int): The height of the slider.
        slider_w (int): The width of the part of the slider that slides.
    """
    def __init__(self, color, color_h, x, y, w, h, slider_w):
        """ 
        The constructor for the Slider class. 
  
        Parameters: 
            color (tuple): The color of the slider. 
            color_h (int): The color of the slider when it is hovered over. 
            x (int): The x-position of the slider.
            y (int): The y-position of the slider.
            width (int): The width of the slider.
            height (int): The height of the slider.
            slider_w (int): The width of the part of the slider that slides.    
        """

        self.color = color
        self.color_h = color_h
        self.x_pos = (x + x + w)/2
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.slider_w = slider_w

    def draw(self, win):
        """ 
        Draws the Slider to the screen. 
  
        Parameters: 
            win (pygame.display): The display to render the menu to. 
        """
        # Gets which mouse buttons are pressed
        slider = pygame.mouse.get_pressed()
        x, y = pygame.mouse.get_pos()

        # If the left mouse button is pressed
        if slider[0] != 0:
            # If it's in the slider box
            if x > self.x and x < self.x + self.width:
                self.x_pos = x - self.slider_w / 2

                # Checks for whether the slider is out of bounds
                if self.x_pos > self.x + self.width - self.slider_w / 2:
                    self.x_pos = self.x + self.width - self.slider_w

                if self.x_pos < self.x + self.slider_w / 2:
                    self.x_pos = self.x

        # If the mouse is hovering over the slider, draw it a different color.
        if self.is_over((x, y)):
            pygame.draw.rect(win, self.color_h, pygame.Rect(self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

        # Draw the bar that gets dragged by the mouse
        pygame.draw.rect(win, colors.WHITE, pygame.Rect(self.x_pos, self.y, self.slider_w, self.height))
        
        pygame.display.update(pygame.Rect(self.x, self.y, self.width, self.height))
    
    def update(self, var_range):
        """ 
        Returns an updated value for a variable in the given range. 
  
        Parameters: 
            var_range (tuple): The given range for the variable to be updated.
        
        Returns: 
            int: The new value for the variable.
        """
        
        # Uses a direct proportion to scale the value of a variable in the given range to the slider input.
        ratio = (self.x_pos - self.x) / (self.width - self.slider_w)
        new_val = var_range[0] + (var_range[1] - var_range[0]) * ratio
        
        return int(new_val) if new_val < var_range[1] else int(var_range[1])
    
    def update_factor(self, var_max):
        """ 
        Returns an updated value for a variable in the range 0, var_max. Makes sure that the new updated value is a factor of var_max. 
  
        Parameters: 
            var_max (tuple): The maximum value for the updated variable.
        
        Returns: 
            int: The new value for the variable.
        """

        # Does the same thing but returns the closest factor of the given number.
        # When setting the length of the array, the number of bars has to be a factor of the screen's width, otherwise rendering gets messed up.
        ratio = (self.x_pos - self.x) / (self.width - self.slider_w)
        new_val = (var_max - 1) * ratio + 1
        factors = [i for i in range(1, var_max + 1) if var_max % i == 0][1:]
        return self.closest(factors, new_val)
    
    def closest(self, lst, K):
        """ 
        Finds the closest value to a given value in a list and returns that value.
  
        Parameters: 
            lst (list): The list of values.
            K (int): The value that the method is trying to find the closest value to in lst.
        
        Returns: 
            int: The closest value to K in lst.
        """

        return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]

    def is_over(self, pos):
        """ 
        Checks whether a given pair of mouse coordinates are over the slider. 
  
        Parameters: 
            pos (tuple): A tuple of mouse coordinates.
          
        Returns: 
            boolean: Whether the mouse coordinates are over the slider.
        """

        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False 


