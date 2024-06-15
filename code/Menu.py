import pygame as pygame
from code.Const import WIN_HEIGHT,WIN_WIDTH
class Menu:
    def __init__(self,window):
        pygame.init()
        self.window: Surface = window
        self.surf = pygame.image.load('asset\MenuBG.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('asset\menu.wav')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf,dest=self.rect)
            self.menu_text(50,"Mountain",(255,128,0),((WIN_WIDTH/2),70))
            pygame.display.flip()

    #Função que gera texto do menu
    def menu_text(self,text_size: int, text: str, text_color: tuple, text_center_position: tuple):
        text_font: Font = pygame.font.SysFont(name = "Lucida Sans Typewriter", size= text_size)
        text_surf: Surface = text_font.render(text,True,text_color)
        text_rect: Rect = text_surf.get_rect(center = text_center_position)
        self.window.blit(source = text_surf, dest=text_rect)
        
   
