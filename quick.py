import random
import pygame

class Visualization:

    def __init__(self):
        
        #Colors:
        self.background_color = (1, 120, 255)
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.green = (0, 255, 0)

        #Dimensions:
        self.window_width = 1200
        self.window_height = 600
        self.array_length = 1200
        self.bar_width = self.window_width/self.array_length

        self.array = [random.randint(1, self.window_height) for i in range(self.array_length)]

        self.ind_to_color = []

        self.window = pygame.display.set_mode([self.window_width, self.window_height])
        pygame.display.set_caption('Quick Sort Visualization')

    def finished_animation(self):
        for i in range(len(self.array)):

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
            pygame.draw.rect(self.window, self.green, [i * self.bar_width, self.window_height - self.array[i], self.bar_width, self.array[i]])

            pygame.display.update()

    def draw(self):
        self.window.fill(self.background_color)
        for i in range(self.array_length):
            pygame.draw.rect(self.window, self.white, [i * self.bar_width, self.window_height - self.array[i], self.bar_width, self.array[i]])
            
        pygame.display.update()

    def partition(self, low, high):
        i = low
        pivot = self.array[high]
        
        for j in range(low, high):
            if self.array[j] <= pivot:
                self.array[i], self.array[j] = self.array[j], self.array[i]
                i += 1

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()

                self.draw()
                
        self.array[i], self.array[high] = self.array[high], self.array[i]

        return i

    def quick_sort(self, low, high):
        if low < high:
            part_ind = self.partition(low=low, high=high)
            
            self.quick_sort(low=low, high=part_ind-1)
            self.quick_sort(low=part_ind+1, high=high)
        
            

    def run(self):
        pygame.init()
    
    
        self.draw()
            
        self.quick_sort(0, len(self.array)-1)
            
        self.finished_animation()

        pygame.quit()

if __name__ == '__main__':

    vis = Visualization()
    vis.run()







        

