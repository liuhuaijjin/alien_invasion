# coding:utf-8
class Settings():

    def __init__(self):
        #设置屏幕大小
        self.screen_width=1200
        self.screen_height=800
        #设置屏幕背景颜色
        self.bg_color=(255,255,255)
        #设置飞船速度
        self.ship_speed_factor=1.5
        self.ship_limit=3
        #子弹设置为宽3像素，高15像素的深灰色
        self.bullet_speed_factor=1
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=60,60,60
        self.bullets_allowed=10
        #外星人设置
        self.alien_speed_factor=1
        self.fleet_drop_speed=10
        #加速游戏节奏
        self.speedup_scale=1.1
        #外星人分数的提高速度
        self.score_scale=1.5
        self.initialize_dynamic_settings()
        #为1表示向右移，为-1表示向左移
        self.fleet_direction=1

    def initialize_dynamic_settings(self):
        #初始化游戏速度
        self.ship_speed_factor=1.5
        self.bullet_speed_factor=3
        self.alien_speed_factor=1
        # 为1表示向右移，为-1表示向左移
        self.fleet_direction = 1
        #记分
        self.alien_points=50

    def increase_speed(self):
        #提高速度设置
        self.ship_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.alien_speed_factor*=self.speedup_scale
        #提高外星人分数
        self.alien_points=int(self.alien_points*self.score_scale)
