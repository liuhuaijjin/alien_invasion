# coding:utf-8
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,screen,ai_settings):
        super(Ship,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        #加载图像并使用get_rect()获取矩阵rect属性
        self.image=pygame.image.load('images/ship.png')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        #将飞船放在屏幕底部中央
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        #在飞船的属性center中存储小数值
        self.center=float(self.rect.centerx)
        #移动标志
        self.moving_right=False
        self.moving_left=False

    def update(self):
        #根据移动标志调整飞船位置
        if self.moving_right and self.rect.right<self.screen_rect.right:
            #向右移动飞船
            #self.rect.centerx+=1
            self.center+=self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left>0:
            #向左移动飞船
            #self.rect.centerx-=1
            self.center-=self.ai_settings.ship_speed_factor
        #根据self.center更新rect对象
        self.rect.centerx=self.center

    def blitme(self):
        #在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        #让飞船在屏幕上居中
        self.center=self.screen_rect.centerx

