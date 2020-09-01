# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class GetgamePipeline(object):
    def __init__(self):
        self.f = open("d:/games.csv", "w", newline='')
        self.writer = csv.writer(self.f)
        self.writer.writerow(['game_name', 'box_txt', 'game_tag', 'game_fever', 'game_fav', 'game_nag',
                              'feedback_rate', 'game_avg', 'detail_url',  'game_intro'])


    def process_item(self, item, spider):
        game_name = item['game_name']
        box_txt = item['box_txt']
        # network_model = item['network_model']
        # game_type = item['game_type']
        game_tag = item['game_tag']
        game_fever = item['game_fever']
        game_fav = item['game_fav']
        game_nag = item['game_nag']
        feedback_rate = item['feedback_rate']
        game_avg = item['game_avg']
        detail_url = item['detail_url']
        game_intro =  item['game_intro']

        game_list = [item['game_name'], item['box_txt'], item['game_tag'], item['game_fever'],
                     item['game_fav'], item['game_nag'], item['feedback_rate'], item['game_avg'],
                     item['detail_url'], item['game_intro']]
        self.writer.writerow(game_list)
        return item

    # def close_spider(self, spider):  # 关闭
    #     self.writer.close()