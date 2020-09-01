# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GetgameItem(scrapy.Item):
    game_name = scrapy.Field()
    box_txt = scrapy.Field()
    # company = scrapy.Field()
    # network_model = scrapy.Field()
    # game_type = scrapy.Field()
    game_tag = scrapy.Field()
    game_fever = scrapy.Field()
    game_fav = scrapy.Field()
    game_nag = scrapy.Field()
    feedback_rate = scrapy.Field()
    game_avg = scrapy.Field()
    detail_url = scrapy.Field()
    game_intro = scrapy.Field()