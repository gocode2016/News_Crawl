# coding:utf-8
from bs4 import BeautifulSoup
import re
import urlparse

class HtmlParser(object):


    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        #/CommonInfo/CommonInfoContent.aspx?CommonInfoID=406
        links = soup.find_all('a', href=re.compile(r"\.\./CommonInfo/CommonInfoContent.aspx\?CommonInfoID=\d+"))
        for link in links:
            print link.get_text()
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            print new_full_url
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
        print new_data
        return new_urls, new_data