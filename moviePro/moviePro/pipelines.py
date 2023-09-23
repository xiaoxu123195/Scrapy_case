

class MovieproPipeline:
    def process_item(self, item, spider):
        if item.__class__.__name__ == 'MovieproItem':
            print(item['title'], item['price'])
            pass
        else:
            print(item['name'], item['spaker'])
        return item
