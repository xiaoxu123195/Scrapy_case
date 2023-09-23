import openpyxl


class Spider2022Pipeline:
    def __init__(self):  # 工作簿
        self.wb = openpyxl.Workbook()  # 工作表
        # ws = wb.create_sheet()    创建新的工作表
        self.ws = self.wb.active  # 拿到一张现在有的工作表
        self.ws.title = 'top250'
        self.ws.append(('标题', '评分', '主题'))

    def close_spider(self, spider):
        self.wb.save('电影数据.xlsx')

    def process_item(self, item, spider):
        # self.ws.append((item['title'],item['rank'],item['subject']))
        title = item.get('title', '')  # 可以处理掉空数据
        rank = item.get('rank', '')
        subject = item.get('subject', '')
        self.ws.append((title, rank, subject))
        return item
