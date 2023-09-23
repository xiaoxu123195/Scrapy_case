import pymysql


# 专门用来处理item对象数据类型
class FirstbloodPipeline:
    fp = None

    # 重写父类的一个方法：该方法只在开始爬虫的时候被调用一次
    def open_spider(self, spider):
        print('start')
        self.fp = open('./first.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        auto = item['auto']
        another = item['another']
        times = item['times']
        fabulous = item['fabulous']

        self.fp.write(auto + ':' + another + ':' + times + ':' + fabulous + '\n')

        return item

    def close_spider(self, spider):
        print('end')
        self.fp.close()


# 管道文件中一个管道类对应一组数据储存到一个平台或者载体中
class mysqlPileLine(object):
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='', db='frist')

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()

        try:
            self.cursor.execute(
                'insert into first values("%s","%s","%s","%s")' % (
                    item["auto"], item["another"], item["times"], item["fabulous"]))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
