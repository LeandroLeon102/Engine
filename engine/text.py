import pygame
from engine.color import swap_color
from engine.image import clip
from os import path
font_path = path.join(path.dirname(__file__), 'small_font.png')
text_box_path = path.join(path.dirname(__file__), 'text_box.png')
arrow_path = path.join(path.dirname(__file__), 'arrow.png')
class Font:
    def __init__(self, path=font_path, color=[0, 0, 0], alpha=255):
        self.spacing = 1
        self.alpha = alpha
        self.character_order = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','.', '-',
                           ',', ':', '+', '\'', '!', '?', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', ')',
                           '/', '_', '=', '\\', '[', ']','*', '"', '<', '>', ';', '%']
        self.font_img = pygame.image.load(path).convert()
        self.font_img = swap_color(self.font_img, (0, 0, 0), (color[0], color[1], color[2]))
        self.current_char_width = 0
        self.characters = {}
        self.character_count = 0
        for x in range(self.font_img.get_width()):
            c = self.font_img.get_at((x, 0))
            if c[0] == 127:
                self.char_image = clip(self.font_img, (x-self.current_char_width, 0), (self.current_char_width,
                                                                                       self.font_img.get_height()))
                self.char_image.set_colorkey([255, 255, 255])

                self.characters[self.character_order[self.character_count]] = self.char_image
                self.character_count += 1
                self.current_char_width = 0
            else:
                self.current_char_width += 1
        self.space_width = self.characters['A'].get_width()

    def render(self, surf, text='', size=3, pos=[0, 0]):
        self.x_offset = 0
        for char in text:
            if char != ' ':
                self.x_offset += self.characters[char].get_width() + self.spacing
            else:
                self.x_offset += self.space_width + self.spacing
        new_surf = pygame.Surface((int(self.x_offset + self.spacing), int(self.characters['A'].get_height())))
        x, y = int(new_surf.get_width() * size), int(new_surf.get_height() * size)
        new_surf.fill((255, 255, 255))
        new_surf.set_colorkey((255, 255, 255))

        self.x_offset = 0
        for char in text:
            if char != ' ':
                new_surf.blit(self.characters[char], (self.x_offset + self.spacing, 0))
                self.x_offset += self.characters[char].get_width() + self.spacing
            else:
                self.x_offset += self.space_width + self.spacing
        new_surf = pygame.transform.scale(new_surf, (x, y))
        new_surf_rect = new_surf.get_rect()
        new_surf_rect.center = (pos[0], pos[1])
        new_surf.set_alpha(self.alpha)
        surf.blit(new_surf, new_surf_rect)

    def character_order(self, order=list):
        try:
            self.character_order = order[:].copy()

        except:
            print("can't assing that order to the font")

    def change_font_img(self, image=None, path=None):
        if  image != None:
            try:
                self.font_img = image
                self.current_char_width = 0
                self.characters = {}
                self.character_count = 0
                for x in range(self.font_img.get_width()):
                    c = self.font_img.get_at((x, 0))
                    if c[0] == 127:
                        self.char_image = clip(self.font_img, (x - self.current_char_width, 0),
                                               (self.current_char_width,
                                                self.font_img.get_height()))
                        self.char_image.set_colorkey([255, 255, 255])

                        self.characters[self.character_order[self.character_count]] = self.char_image
                        self.character_count += 1
                        self.current_char_width = 0
                    else:
                        self.current_char_width += 1
                self.space_width = self.characters['A'].get_width()
            except:
                print("Error while changing the font image")
        if path != None:
            try:
                self.font_img = pygame.image.load(path).convert()
                self.current_char_width = 0
                self.characters = {}
                self.character_count = 0
                for x in range(self.font_img.get_width()):
                    c = self.font_img.get_at((x, 0))
                    if c[0] == 127:
                        self.char_image = clip(self.font_img, (x - self.current_char_width, 0),
                                               (self.current_char_width,
                                                self.font_img.get_height()))
                        self.char_image.set_colorkey([255, 255, 255])

                        self.characters[self.character_order[self.character_count]] = self.char_image
                        self.character_count += 1
                        self.current_char_width = 0
                    else:
                        self.current_char_width += 1
                self.space_width = self.characters['A'].get_width()
            except:
                print("Error while changing the font image")

    def change_font_color(self, actualColor=[0, 0, 0], newColor=[0, 0, 0]):
        try:
            self.font_img = swap_color(self.font_img, actualColor, newColor)
            self.current_char_width = 0
            self.characters = {}
            self.character_count = 0
            for x in range(self.font_img.get_width()):
                c = self.font_img.get_at((x, 0))
                if c[0] == 127:
                    self.char_image = clip(self.font_img, (x - self.current_char_width, 0),
                                           (self.current_char_width,
                                            self.font_img.get_height()))
                    self.char_image.set_colorkey([255, 255, 255])

                    self.characters[self.character_order[self.character_count]] = self.char_image
                    self.character_count += 1
                    self.current_char_width = 0
                else:
                    self.current_char_width += 1
            self.space_width = self.characters['A'].get_width()
        except:
            print("Error while changing the font color")

class Queue(object):
    def __init__(self, screenSize):
        self.screen_size = screenSize
        self.messages = []
        self.pos = 0
        self.text_box_img = pygame.transform.scale(pygame.image.load(text_box_path).convert(), (screenSize[0], int(screenSize[1] * .30)))
        self.text_box_img.set_colorkey([255, 255, 255])
        self.arrow_img = pygame.transform.scale(pygame.image.load(arrow_path).convert(), [20, 20])
        self.arrow_img.set_colorkey([255, 255, 255])
        self.font = Font()
        self.timer = 0
        self.offset = 0
        self.rect = self.text_box_img.get_rect()

    def set_text_box_image(self, image=None, path=None, size=[100, 20]):
        if image != None:
            try:
                self.text_box_img = image
            except:
                print('Error while setting new image to the queue')
        if path != None:
            try:
                self.text_box_img = pygame.transform.scale(pygame.image.load(path).convert(), (size[0], size[1]))
            except:
                print('Error while setting new image to the queue')

    def set_text_box_color(self, oldColor=[20, 16, 32], newColor=[20, 16, 32]):
        self.text_box_img = swap_color(self.text_box_img, oldColor, newColor)
        self.text_box_img.set_colorkey([255, 255, 255])

    def set_arrow_image(self, image=None, path=None, size=None):
        if image != None:
            try:
                self.arrow_img = pygame.transform.scale(image, (size[0], size[1]))
            except:
                print('Error while setting new image to the queue arrow')
        if path != None:
            try:
                pygame.transform.scale(pygame.image.load(path).convert(), (size[0], size[1]))
            except:
                print('Error while setting new image to the queue arrow')

    def add_message(self, text):
        self.messages.append(str(text))

    def check_click(self):
        self.click = pygame.mouse.get_pressed()
        if self.click[0] == 1:
            if self.pos == -40 and (self.timer - len(self.messages[0]) > 20):
                self.messages.pop(0)
                self.timer = 0

    def update(self, surf, char_limit):
        self.check_click()
        if self.messages:
            self.pos += (-40 - self.pos) / 10
            if abs(self.pos + 40) < 0.5:
                self.pos = -40
        else:
            self.pos += (10 - self.pos) / 10
        if self.pos < 0:
            self.text_box_img.set_alpha(int(abs(self.pos) / 40 * 165))
            surf.blit(self.text_box_img, (0, self.screen_size[1] - self.text_box_img.get_height() / 1.5 + self.pos))
        if self.pos == -40:
            self.timer += 1
            if self.timer <= char_limit:
                self.font.render(surf, self.messages[0][:int(self.timer)], pos=[self.text_box_img.get_width() / 2, self.screen_size[1] * .85])
            else:
                if len(self.messages[0]) <= char_limit:
                    self.font.render(surf, self.messages[0][:char_limit],
                                     pos=[self.text_box_img.get_width() / 2, self.screen_size[1] * .85])
                elif self.timer <= char_limit*2:
                    self.font.render(surf, self.messages[0][:char_limit],
                                     pos=[self.text_box_img.get_width() / 2, self.screen_size[1] * .85])
                    self.font.render(surf, self.messages[0][char_limit:self.timer],
                                     pos=[self.text_box_img.get_width() / 2, self.screen_size[1] * .90])
                elif len(self.messages[0]) <= char_limit*2:
                    self.font.render(surf, self.messages[0][:char_limit],
                                     pos=[self.text_box_img.get_width() / 2, self.screen_size[1] * .85])
                    self.font.render(surf, self.messages[0][char_limit:char_limit*2],
                                     pos=[self.text_box_img.get_width() / 2, self.screen_size[1] * .90])
                elif self.timer <= char_limit*3:
                    self.font.render(surf, self.messages[0][:char_limit],
                                     pos=[self.text_box_img.get_width() / 2, self.screen_size[1] * .80])
                    self.font.render(surf, self.messages[0][char_limit:char_limit * 2],
                                     pos=[self.text_box_img.get_width() / 2, self.screen_size[1] * .85])
                    self.font.render(surf, self.messages[0][char_limit*2:self.timer],
                                     pos=[self.text_box_img.get_width() / 2, self.screen_size[1] * .90])
                elif len(self.messages[0]) <= char_limit*3:
                    self.font.render(surf, self.messages[0][:char_limit],
                                     pos=[self.text_box_img.get_width() / 2, self.screen_size[1] * .80])
                    self.font.render(surf, self.messages[0][char_limit:char_limit * 2],
                                     pos=[self.text_box_img.get_width() / 2, self.screen_size[1] * .85])
                    self.font.render(surf, self.messages[0][char_limit*2:char_limit*3],
                                     pos=[self.text_box_img.get_width() / 2, self.screen_size[1] * .90])

            self.offset += 1

    def set_font_color(self, old_color=[0, 0, 0], new_color=[0, 0, 0]):
        self.font.change_font_color(old_color, new_color)