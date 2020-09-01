# -*- coding: utf-8 -*-
import scrapy
from getgame.items import GetgameItem


class MigameSpider(scrapy.Spider):
    name = 'mobilegame'
    allowed_domains = ['shouyou.gamersky.com']
    start_urls = ['https://shouyou.gamersky.com/ku/0-0-0-30.html']

    # 下一页的网址信息
    def parse_next_page(self, response):
        next_page = response.xpath("//a[@class='p2']/@href").extract_first('')
        if next_page:
            yield scrapy.Request(
                url=next_page,
                callback=self.parse,
                meta={},
                dont_filter=True
            )

    def parse(self, response):
        # 创建item对象
        item = GetgameItem()
        # 获取返回值并提取数据
        game_list = response.xpath("//ul[@class='pictxt']/li")
        # 病例封装数据
        for game_msg in game_list:
            detail_url = game_msg.xpath("a/@href").extract_first()
            item["detail_url"] = detail_url
            # 爬取详细数据
            yield scrapy.Request(item["detail_url"], priority={'https': "36.112.128.235:3128"}, callback=self.detail_parse)
            # yield item
        # 发送请求获取下一页
        yield scrapy.Request(
            url=response.url,
            callback=self.parse_next_page,
            dont_filter=True,
        )
    # 爬取详细信息
    def detail_parse(self, response):
        item = response.url
        print(response)
        game_name = response.xpath("//span[@class='tit']/text()").extract_first()
        box_txt = response.xpath("//div[@class='box_txt']/text()").extract_first()
        tag_list = response.xpath("//div[@class='box_tag']/a")
        game_tag = ""
        for game_msg in tag_list:
            game_tag += str(game_msg.xpath("text()").extract_first())
        game_fever = response.xpath("//div[@class='box_ZS']/div[@class='RD']/c/text()").extract_first()
        feedback_rate = response.xpath("//div[@id='Sorce']/text()").extract_first()
        game_fav = response.xpath("//span[@id='like']/text()").extract_first()
        game_nag = response.xpath("//span[@id='unlike']/text()").extract_first()
        game_avg = response.xpath("//div[@id='scoreAvg']/text()").extract_first()
        game_intro = response.xpath("//div[@id='Intro']/p/text()").extract()
        game_intro = "".join(game_intro).replace("\u3000"," ")
        item["game_name"] = game_name
        item['box_txt'] = box_txt
        item['game_tag'] = game_tag
        item['game_fever'] = game_fever
        item['game_fav'] = game_fav
        item['game_nag'] = game_nag
        item['feedback_rate'] = feedback_rate
        item['game_avg'] = game_avg
        item['game_intro'] = game_intro
        return item


    # 下一页的网址信息
    # def parse_next_page(self, response):
    #     next_page = response.xpath("//li[@class='bk'][2]/a/@href").extract_first('')
    #     if next_page:
    #         yield scrapy.Request(
    #             url=next_page,
    #             callback=self.parse_job_info,
    #             meta={},
    #             dont_filter=True
    #         )

        # 详情爬取
    # def detail_parse(self, response):
    #     # 接收上级已爬取的数据
    #     item = response.meta['item']
    #     job_msg = response.xpath("//div[@class='cn']/p[@class='msg ltype']/@title").extract()
    #     print("*******************************************", str(job_msg))
    #     job_comm = response.xpath("//div[@class='jtag']//span/text()").extract()
    #     job_con = response.xpath("//div[@class='bmsg inbox']/p/text()").extract()
    #     com_flag = response.xpath("//div[@class='com_tag']/p[1]/text()").extract()
    #     com_peo = response.xpath("//div[@class='com_tag']/p[2]/text()").extract()
    #     com_trade = response.xpath("//div[@class='com_tag']/p[3]/@title").extract()
    #     item['job_msg'] = job_msg
    #     item['job_comm'] = job_comm
    #     item['job_con'] = job_con
    #     item['com_flag'] = com_flag
    #     item['com_peo'] = com_peo
    #     item['com_trade'] = com_trade
    #     return item

        # 解析并封装数据到item中
    # def parse_job_info(self, response):
    #     game_list = response.xpath("//li[@class='clearfix']")
    #     for game_detail in game_list:
    #         rank = game_detail.xpath("i/text()").extract()
    #         genresList = game_detail.xpath("div[@class='game-about']/div[@class='label-list clearfix']/span")
    #         genres = []
    #         for gen in genresList:
    #             genres += gen.xpath('text()').extract()
    #         title = game_detail.xpath("div[@class='game-about']/div/span[@class='about-name']/text()").extract()
    #         intruduction = game_detail.xpath("div[@class='game-about']/p/text()").extract()
    #         rating = game_detail.xpath("div[@class='game-about']/div//span[@class='about-score']/text()").extract()
    #         # num_rating = game_detail.xpath("//li[@class='clearfix']//div[@class='label-list clearfix']/span").extract_first().strip()
    #         # content = game_detail.xpath("//li[@class='clearfix']//div[@class='label-list clearfix']/span").extract_first().strip()
    #         # yield item
    #
    #         # 数据封装到item中
    #         item = GetgameItem()
    #         item['rank'] = rank[0]
    #         item['genres'] = ','.join(genres)
    #         item['title'] = title[0]
    #         item['intruduction'] = intruduction[0]
    #         item['rating'] = rating[0]
    #         # 爬取内页数据
    #         # yield scrapy.Request(item['detail_url'], meta={'item': item}, callback=self.detail_parse)
    #         print(item)
    #         return item

        # # 发送请求获取下一页
        # yield scrapy.Request(
        #     url=response.url,
        #     callback=self.parse_next_page,
        #     dont_filter=True,
        # )


