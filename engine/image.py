import pygame


def clip(surf, pos=[0, 0], size=[50, 50]):
    handle_surf = surf.copy()
    clipR = pygame.Rect(pos[0], pos[1], size[0], size[1])
    handle_surf.set_clip(clipR)
    image = surf.subsurface(handle_surf.get_clip())
    return image
