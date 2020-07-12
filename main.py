import pygame
import colors

from label import Label
from button import Button
from slider import Slider
from drop_menu import DropMenu
from visualization import Visualization

WIDTH = 1200
HEIGHT = 600
TOOLBAR_HEIGHT = 50

WINDOW = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Sorting Visualizer')

array_length = 120

VIS = Visualization(WIDTH, HEIGHT - TOOLBAR_HEIGHT, array_length, WINDOW)

RUN = Button(colors.BLUE, colors.DARK_BLUE, 25, HEIGHT - TOOLBAR_HEIGHT + 7, 70, TOOLBAR_HEIGHT - 14, 'Run')
RESET = Button(colors.BLUE, colors.DARK_BLUE, 120, HEIGHT - TOOLBAR_HEIGHT + 7, 170, TOOLBAR_HEIGHT - 14, 'Randomize')
DELAY_SLIDER = Slider(colors.BLUE, colors.DARK_BLUE, 400, HEIGHT-TOOLBAR_HEIGHT + 7, 300, TOOLBAR_HEIGHT - 14, 10)
LENGTH_SLIDER = Slider(colors.BLUE, colors.DARK_BLUE, 790, HEIGHT - TOOLBAR_HEIGHT + 7, 75, TOOLBAR_HEIGHT - 14, 10)

DELAY_LABEL = Label(colors.BLUE, 10, 10, 100, 20, f'Delay: {int(VIS.delay_time * 1000)} ms')
LENGTH_LABEL = Label(colors.BLUE, 120, 10, 80, 20, f'Length: {int(VIS.array_length)}')

DELAY_SLIDER_LABEL = Label(colors.BLUE, 335, HEIGHT - TOOLBAR_HEIGHT + 15, 50, 20, 'Delay:')
LENGTH_SLIDER_LABEL = Label(colors.BLUE, 720, HEIGHT - TOOLBAR_HEIGHT + 15, 60, 20, 'Length:')

PAUSE = Button(colors.BLUE, colors.DARK_BLUE, 25, HEIGHT - TOOLBAR_HEIGHT + 7, 90, TOOLBAR_HEIGHT - 14, 'Pause')
STOP = Button(colors.BLUE, colors.DARK_BLUE, 130, HEIGHT - TOOLBAR_HEIGHT + 7, 70, TOOLBAR_HEIGHT - 14, 'Stop')
PLAY = Button(colors.BLUE, colors.DARK_BLUE, 25, HEIGHT - TOOLBAR_HEIGHT + 7, 70, TOOLBAR_HEIGHT - 14, 'Play')

SORT_SELECT_LABEL = Label(colors.BLUE, 875, HEIGHT - TOOLBAR_HEIGHT + 15, 80, 20, 'Algorithm:')
SORT_SELECTION = DropMenu(colors.DARK_BLUE, colors.BLUE, 965, HEIGHT - TOOLBAR_HEIGHT + 7, 240, TOOLBAR_HEIGHT - 14, ['Bubble Sort', 'Insertion Sort', 'Selection Sort'])

BUTTONS = (PAUSE, STOP, PLAY)
LABELS = (DELAY_LABEL, LENGTH_LABEL)

def main():

    WINDOW.fill(colors.GRAY)
    VIS.draw()
    RESET.draw(WINDOW)
    RUN.draw(WINDOW)
    DELAY_SLIDER.draw(WINDOW)
    LENGTH_SLIDER.draw(WINDOW)

    DELAY_LABEL.draw(WINDOW)
    LENGTH_LABEL.draw(WINDOW)
    DELAY_SLIDER_LABEL.draw(WINDOW)
    LENGTH_SLIDER_LABEL.draw(WINDOW)

    SORT_SELECTION.draw(WINDOW)
    SORT_SELECT_LABEL.draw(WINDOW)

    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if RUN.is_over(mouse_pos):
                VIS.run(SORT_SELECTION.current_state, LABELS, BUTTONS)
            if RESET.is_over(mouse_pos):
                VIS.reset()
            SORT_SELECTION.handle_click()

    DELAY_LABEL.update_text(f'Delay: {int(VIS.delay_time * 1000)} ms')
    LENGTH_LABEL.update_text(f'Length: {int(VIS.array_length)}')
    VIS.set_length(LENGTH_SLIDER.update_factor(WIDTH))
    VIS.delay_time = DELAY_SLIDER.update((0, 250))/1000.

    pygame.display.update()

if __name__ == '__main__':
    while True:
        main()