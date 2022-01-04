__author__ = 'justinarmstrong'

import pygame as pg
from .. import constants as c

class Collider(pg.sprite.Sprite):
    """放置在可与（管道、台阶、地面等）碰撞的顶部背景部分上方的不可见的单位"""
    def __init__(self, x, y, width, height, name='collider'):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width, height)).convert()
        #self.image.fill(c.RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state = None

