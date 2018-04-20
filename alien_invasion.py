# coding:utf-8
import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf
from alien import Alien

def run_game():
    pygame.init()
    #实例化类
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #实例化按钮
    play_button=Button(ai_settings,screen,"Play")
    #实例化GameStats类
    stats=GameStats(ai_settings)
    #实例化记分牌
    sb=Scoreboard(ai_settings,screen,stats)
    #创建一艘飞船,Ship实例化
    ship=Ship(screen,ai_settings)
    #实例化存储子弹的编组
    bullets=Group()
    aliens=Group()
    #实例化外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)

    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)

run_game()

