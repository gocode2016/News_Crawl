# coding:utf-8
import url_manager, html_downloader, html_parser, html_outputer
import traceback

class Crawl(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                count = count + 1
            except Exception,e:
                print 'craw failed!'
                print 'str(Exception):\t', str(Exception)
                print 'str(e):\t\t', str(e)
                print 'repr(e):\t', repr(e)
                print 'e.message:\t', e.message
                print 'traceback.print_exc():'; traceback.print_exc()
                print 'traceback.format_exc():\n%s' % traceback.format_exc()
        self.outputer.output_html()

if __name__=="__main__":
    root_url = "http://cs.cqut.edu.cn/Notice/NoticeStudentMore.aspx"
    obj_News_crawl = Crawl()
    obj_News_crawl.craw(root_url)