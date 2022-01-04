__author__ = 'justinarmstrong'


import pygame as pg
from .. import setup
from .. import constants as c


class Enemy(pg.sprite.Sprite):
    """所有敌人的基类"""
    def __init__(self):
        pg.sprite.Sprite.__init__(self)


    def setup_enemy(self, x, y, direction, name, setup_frames):
        """为敌人设置各种价值"""
        self.sprite_sheet = setup.GFX['smb_enemies_sheet']
        self.frames = []
        self.frame_index = 0
        self.animate_timer = 0
        self.death_timer = 0
        self.gravity = 1.5
        self.state = c.WALK

        self.name = name
        self.direction = direction
        setup_frames()

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y
        self.set_velocity()


    def set_velocity(self):
        """基于方向设置速度向量"""
        if self.direction == c.LEFT:
            self.x_vel = -2
        else:
            self.x_vel = 2

        self.y_vel = 0


    def get_image(self, x, y, width, height):
        """工作表中获取图像帧"""
        image = pg.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)


        image = pg.transform.scale(image,
                                   (int(rect.width*c.SIZE_MULTIPLIER),
                                    int(rect.height*c.SIZE_MULTIPLIER)))
        return image


    def handle_state(self):
        """基于状态的敌人行为"""
        if self.state == c.WALK:
            self.walking()
        elif self.state == c.FALL:
            self.falling()
        elif self.state == c.JUMPED_ON:
            self.jumped_on()
        elif self.state == c.SHELL_SLIDE:
            self.shell_sliding()
        elif self.state == c.DEATH_JUMP:
            self.death_jumping()


    def walking(self):
        """侧向移动的默认状态"""
        if (self.current_time - self.animate_timer) > 125:
            if self.frame_index == 0:
                self.frame_index += 1
            elif self.frame_index == 1:
                self.frame_index = 0

            self.animate_timer = self.current_time


    def falling(self):
        """掉落"""
        if self.y_vel < 10:
            self.y_vel += self.gravity


    def jumped_on(self):
        """当敌人被践踏"""
        pass


    def death_jumping(self):
        """死亡动画"""
        self.rect.y += self.y_vel
        self.rect.x += self.x_vel
        self.y_vel += self.gravity

        if self.rect.y > 600:
            self.kill()


    def start_death_jump(self, direction):
        """使敌人进入死亡跳跃状态"""
        self.y_vel = -8
        if direction == c.RIGHT:
            self.x_vel = 2
        else:
            self.x_vel = -2
        self.gravity = .5
        self.frame_index = 3
        self.image = self.frames[self.frame_index]
        self.state = c.DEATH_JUMP


    def animation(self):
        """基本动画，在两帧之间切换"""
        self.image = self.frames[self.frame_index]


    def update(self, game_info, *args):
        """更新敌人的行为"""
        self.current_time = game_info[c.CURRENT_TIME]
        self.handle_state()
        self.animation()




class Goomba(Enemy):

    def __init__(self, y=c.GROUND_HEIGHT, x=0, direction=c.LEFT, name='goomba'):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames)


    def setup_frames(self):
        """将图像帧放入要设置动画的列表中"""

        self.frames.append(
            self.get_image(0, 4, 16, 16))
        self.frames.append(
            self.get_image(30, 4, 16, 16))
        self.frames.append(
            self.get_image(61, 0, 16, 16))
        self.frames.append(pg.transform.flip(self.frames[1], False, True))


    def jumped_on(self):
        """当马里奥压扁敌人"""
        self.frame_index = 2

        if (self.current_time - self.death_timer) > 500:
            self.kill()



class Koopa(Enemy):

    def __init__(self, y=c.GROUND_HEIGHT, x=0, direction=c.LEFT, name='koopa'):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames)


    def setup_frames(self):
        self.frames.append(
            self.get_image(150, 0, 16, 24))
        self.frames.append(
            self.get_image(180, 0, 16, 24))
        self.frames.append(
            self.get_image(360, 5, 16, 15))
        self.frames.append(pg.transform.flip(self.frames[2], False, True))


    def jumped_on(self):
        self.x_vel = 0
        self.frame_index = 2
        shell_y = self.rect.bottom
        shell_x = self.rect.x
        self.rect = self.frames[self.frame_index].get_rect()
        self.rect.x = shell_x
        self.rect.bottom = shell_y


    def shell_sliding(self):
        if self.direction == c.RIGHT:
            self.x_vel = 10
        elif self.direction == c.LEFT:
            self.x_vel = -10



















