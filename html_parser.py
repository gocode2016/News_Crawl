# coding:utf-8
from bs4 import BeautifulSoup
import re
import urlparse
import datetime

class HtmlParser(object):


    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        #/CommonInfo/CommonInfoContent.aspx?CommonInfoID=406
        #<a id="ctl00_ContentPlaceHolder_main_NoticeStudentMore1_GridView1_ctl10_HyperLink4"
        #<a id="ctl00_ContentPlaceHolder_main_NoticeMore1_GridView1_ctl02_HyperLink3"
        #<a id="ctl00_ContentPlaceHolder_main_NewsMore1_GridView1_ctl02_HyperLink3"
        #<a id="ctl00_ContentPlaceHolder_main_EmpMore1_GridView1_ctl02_HyperLink4"
        links = soup.find_all('a', id=re.compile(r"ctl00_ContentPlaceHolder_main_\w+_GridView1_ctl\d+_HyperLink[3-4]"))
        
        for link in links:
            #print link.get_text()
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            if link.get_text() == datetime.datetime.now().strftime("%m/%d"):
            #if link.get_text() == '12/02':
                new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        count = 1

        #<p class="MsoNormal" 
        summary_nodes = soup.find_all('p')
        for summary_node in summary_nodes:
            res_data[count] = summary_node.get_text()
            count = count + 1

        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return 

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data