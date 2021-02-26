import pygame

def Color(r, g, b, a=255):
    color = pygame.color.Color
    color.r(r)
    color.g(g)
    color.b(b)
    color.a(a)
    return color

def swap_color(image, old_color, new_color):
    image_copy = pygame.Surface((image.get_size()))
    image_copy.fill(new_color)
    image.set_colorkey(old_color)
    image_copy.blit(image, (0, 0))
    return image_copy