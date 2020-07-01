import random
import pygame
import time
import colors

class Visualization:
    """ 
    This is a class to represent a sorting visualization in pygame.
      
    Attributes: 
        width (int): The width of the slider.
        height (int): The height of the slider.
        array_length (int): The length of the array.
        window (pygame.display): The display to draw to.
        background_color (tuple): The color of the background.

    """

    def __init__(self, width, height, array_length, window):
        """ 
        The constructor for the Visualization class. 
  
        Parameters: 
            width (int): The width of the slider.
            height (int): The height of the slider.
            array_length (int): The length of the array.
            window (pygame.display): The display to draw to.    
        """
        
        #Colors:
        self.background_color = colors.GRAY
        self.bar_color = colors.WHITE
        self.highlight_color = colors.BLUE

        #Dimensions:
        self.window_width = width
        self.window_height = height
        self.array_length = array_length
        self.bar_width = self.window_width/self.array_length

        self.delay_time = 1/1000.

        self.reset()

        self.window = window

    def reset(self):
        """ 
        The function to reset the array by randomizing all of the values. 
  
        """

        self.array = [random.randint(1, self.window_height) for i in range(self.array_length)]

    def draw_highlight(self, colors, highlight):
        """ 
        The function to draw the bars to the screen, but with one of the bars highlighted. 
  
        Parameters: 
            colors (tuple): The standard color and the highlighted color.
            highlight: (int): The index to be highlighted. 
        """

        # Iterates through array.
        for i in range(self.array_length):
            # If it's the highlight index, draw it in the different color.
            if abs(i - highlight) < 1:
                pygame.draw.rect(self.window, colors[1], [i * self.bar_width, self.window_height - self.array[i], self.bar_width, self.array[i]])
            else:
                pygame.draw.rect(self.window, colors[0], [i * self.bar_width, self.window_height - self.array[i], self.bar_width, self.array[i]])
        

    def draw(self):
        """ 
        The function to draw the bars to the screen. 
  
        """

        # Makes sure the bars are the correct width. Check doesn't need to be made in draw_highlight, since it's only used during sorting.
        self.bar_width = self.window_width / self.array_length
        for i in range(self.array_length):
            pygame.draw.rect(self.window, self.bar_color, [i * self.bar_width, self.window_height - self.array[i], self.bar_width, self.array[i]])
    

    def finished_animation(self):
        """ 
        Draws the animation that occurs when the sort is finished. 

        """

        # Iterate through array.
        for i in range(len(self.array)):

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            
            # Draw the rectangle.
            pygame.draw.rect(self.window, self.highlight_color, [i * self.bar_width, self.window_height - self.array[i], self.bar_width, self.array[i]])

            pygame.display.update()

            # Delay
            self.delay(1 / self.array_length)
    
    def delay(self, seconds):
        """ 
        The function to delay by a certain amount of time. Used to delay the sorting. 
  
        Parameters: 
            seconds (float): The number of seconds to delay
        """

        start_time = time.time()
        time_elapsed = time.time() - start_time
        while time_elapsed < seconds:
            time_elapsed = time.time() - start_time

    def selection(self, labels, buttons):
        """ 
        The function to animate the selection sort algorithm. 
  
        Parameters: 
            labels (list): A list of labels to draw during the animation.
            buttons (list): A list of buttons to draw during the animation.
        """

        pygame.init()

        # Get the buttons
        PAUSE = buttons[0]
        STOP = buttons[1]
        PLAY = buttons[2]

        index = 0
        
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                # If buttons are pressed, call the apropriate methods.
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if PAUSE.is_over(mouse_pos):
                        self.pause(PLAY, labels)
                    if STOP.is_over(mouse_pos):
                        self.reset()
                        return

            self.window.fill(self.background_color)

            # Find the minimum value not sorted.
            min_index = index
            for j in range(index, len(self.array)):
                if self.array[j] < self.array[min_index]:
                    min_index = j
            
            # Swap the minimum value with the current value then draw.
            self.array[index], self.array[min_index] = self.array[min_index], self.array[index]
            self.draw_highlight((self.bar_color, self.highlight_color), min_index)

            # If we're done, then break
            if index < len(self.array) - 1:
                index += 1
            else:
                break
            
            # Draw everything, update the screen, then delay.
            for label in labels:
                label.draw(self.window)

            PAUSE.draw(self.window)
            STOP.draw(self.window)

            pygame.display.update()
            self.delay(self.delay_time)

        # Once the sort is finished, it gets drawn once, then goes through the finished_animation, then resets the array.
        self.draw()
        self.finished_animation()
        self.reset()

    def insertion(self, labels, buttons):
        """ 
        The function to animate the insertion sort algorithm. 
  
        Parameters: 
            labels (list): A list of labels to draw during the animation.
            buttons (list): A list of buttons to draw during the animation.
        """

        pygame.init()

        index = 1
        
        # Get the buttons
        PAUSE = buttons[0]
        STOP = buttons[1]
        PLAY = buttons[2]
        
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                
                # If buttons are pressed, call the apropriate methods.
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if PAUSE.is_over(mouse_pos):
                        self.pause(PLAY, labels)
                    if STOP.is_over(mouse_pos):
                        self.reset()
                        return


            self.window.fill(self.background_color)

            # Set the current value
            value = self.array[index]
            j = index - 1
            
            # Insert the value into its correct spot.
            while j >= 0 and self.array[j] > value:
                self.array[j+1] = self.array[j]
                j -= 1

            self.array[j + 1] = value

            # Draw the bars.
            self.draw_highlight((self.bar_color, self.highlight_color), j)

            # If we're done then break.
            if index < len(self.array)-1:
                index += 1
            else:
                break

            # Draw everything, update the screen, then delay.
            for label in labels:
                label.draw(self.window)
            
            PAUSE.draw(self.window)
            STOP.draw(self.window)

            pygame.display.update()
            self.delay(self.delay_time)

        # Once the sort is finished, it gets drawn once, then goes through the finished_animation, then resets the array.
        self.draw()
        self.finished_animation()
        self.reset()
    
    def bubble(self, labels, buttons):
        """ 
        The function to animate the bubble sort algorithm. 
  
        Parameters: 
            labels (list): A list of labels to draw during the animation.
            buttons (list): A list of buttons to draw during the animation.
        """

        pygame.init()
        
        # Get the buttons
        PAUSE = buttons[0]
        STOP = buttons[1]
        PLAY = buttons[2]

        while True:
            
            count = 0

            # Iterate through the array
            for i in range(len(self.array) - 1):

                self.window.fill(self.background_color)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                    # If buttons are pressed, call the apropriate methods.
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if PAUSE.is_over(mouse_pos):
                            self.pause(PLAY, labels)
                        if STOP.is_over(mouse_pos):
                            self.reset()
                            return

                # If two elements are out of place, swap them.
                if self.array[i] > self.array[i+1]:
                    self.array[i], self.array[i+1] = self.array[i+1], self.array[i]

                    # Draw everything, update the screen, and delay.
                    self.draw_highlight((self.bar_color, self.highlight_color), i+1)

                    for label in labels:
                        label.draw(self.window)
            
                    PAUSE.draw(self.window)
                    STOP.draw(self.window)

                    pygame.display.update()
                    self.delay(self.delay_time)

                    count += 1

            # If we're done then break.
            if count == 0: break

        # Once the sort is finished, it gets drawn once, then goes through the finished_animation, then resets the array.
        self.draw()
        self.finished_animation()
        self.reset()

    def pause(self, play_button, labels):
        """ 
        The function to pause the execution of an algorithm. 
  
        Parameters: 
            play_button (list): The play button to draw during the pause.
            labels (list): A list of labels to draw during the animation.
        """

        while True:

            self.window.fill(self.background_color)

            # Draw everything
            for label in labels:
                label.draw(self.window)

            play_button.draw(self.window)
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                
                # If the play button is hit, then return out of the pause method.
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if play_button.is_over(mouse_pos):
                        return
            
            # Update the display.
            pygame.display.update()
    
    def run(self, sort, labels, buttons):
        """ 
        Checks which sort was given and executes it. 
  
        Parameters: 
            sort (string): The type of sort to execute.
            labels (list): A list of labels to draw during the animation.
            buttons (list): The buttons to draw during the animation.
        """

        if sort == 'Selection Sort':
            self.selection(labels, buttons)
        elif sort == 'Insertion Sort':
            self.insertion(labels, buttons)
        elif sort == 'Bubble Sort':
            self.bubble(labels, buttons)


    def set_length(self, new_length):
        """ 
        Sets length to a new value and resets the array. 
  
        Parameters: 
            new_length (int): The new value of the length.
        """
        # If the new length is different than before, set the new length and reset the array.
        if new_length != self.array_length:
            self.array_length = new_length
            self.reset()