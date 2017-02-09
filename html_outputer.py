# coding:utf-8

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        for data in self.datas:
            for key in data:
                print data[key]
        return