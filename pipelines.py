from scrapy.exceptions import DropItem


class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""

    # put all words in lowercase
    words_to_filter = ['']

    def process_item(self, item, spider):
        #for word in self.words_to_filter:
            #curl = item['url']
            if not item['url']:
                raise DropItem("Unknown URL")
            else:
                return item
