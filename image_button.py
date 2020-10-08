# Made by Seb C: for Lemon Clicker in 2020, however it may be used in other PyGame projects
import pygame
pygame.init()

class Button:
    def __init__(self, window, x, y, texture, sizex, sizey): #Texture is a directory string linking the the image, not the loaded pygame image
        self.window = window
        self.x = x
        self.y = y
        self.texture = pygame.transform.scale(pygame.image.load(texture).convert_alpha(), (sizex, sizey))
        self.sizex = sizex
        self.sizey = sizey
        self.clicked = False
        self.clickable = True
        self.mousedown = False

    def disp(self, window = None, x = None, y = None):
        if window is None:
            window = self.window
        if x is None:
            x = self.x
        if y is None:
            y = self.y
        if not self.clicked and not self.mousedown: #If not clicked, then display the image at normal size
            window.blit(self.texture, (x, y))
        #elif self.clicked: 
        elif self.mousedown: #While the mouse is down, the lemon is still held down until mouse is released
            pc25_sizex = round(0.25 * self.sizex)
            pc25_sizey = round(0.25 * self.sizey)
            resized_texture = pygame.transform.scale(self.texture, (self.sizex - pc25_sizex, self.sizey - pc25_sizey)) #Sizex and sizey are the variables we will be using for the math
            window.blit(resized_texture, (x + pc25_sizex / 2, y + pc25_sizey / 2))
        #print(self.clicked) #If clicked, then display the image at a smaller size (3/4 of it's normal size)

    def handle_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] == True: #If left mouse down
            if mouse_pos[0] > self.x and mouse_pos[0] < self.x + self.sizex and mouse_pos[1] > self.y and mouse_pos[1] < self.y + self.sizey:
                self.mousedown = True
                if self.clickable: #If the button is clickable
                    self.clicked = True #Set clicked to true
                    self.clickable = False #Set clickable to false
                    #print("mouse clicked")
                    return True
            #else:
            #    if self.mousedown:
        elif pygame.mouse.get_pressed()[0] == False: #If left mouse up
            self.mousedown = False
            if not self.clickable:
                self.clickable = True
                pass
            #print(f"Hovering Over, boundaries of this are: x1{self.x} y1{self.y} x2{self.x + self.sizex} y2{self.y + self.sizey}")
        self.clicked = False
    
    def update(self, disp_img = None):
        if disp_img is None:
            disp_img = True
        if disp_img == True:
            self.disp()
            self.handle_click()