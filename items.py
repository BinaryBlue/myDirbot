from scrapy.item import Item, Field


class Website(Item):
    url = Field()
    name = Field()
