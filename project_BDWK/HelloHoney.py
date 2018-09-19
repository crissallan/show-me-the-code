__author__ = 'fansly'

import os
import re
import json
import requests
from lxml import etree

class BaiduWK(object):
    def __init(self, url):
        self.title = None
        self.url = url
        self.doctype = None
        self.headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKet/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'}
        self.get_response_content(self.url)
        self.get_doc_type_and_title()

    def get_response_content(self, url):
        try:
            response = requests.get(url, headers = self.headers)
            return response.content
        except Exception as e:
            print(e)
            pass
    def get_doc_type_and_title(self):
        source_html = self.get_response_content(self.url)
        content = source_html.docode('gbk')
        self.docType = re.findall(r"docType.*?\:.*?\'(.*?)\'\,", content)[0]
        self.title = re.findall(r"title.*?\:.*?\'(.*?)\'\,", content)[0]

class BDWKTXT(BaiduWK):
    def __init__(self, url):
        super().__init__(url)
        self.docId = None
        pass

    def get_txt(self, url):
        # get source
        source_html = self.get_response_content(url)
        content = source_html.decode("gbk")
        # get docId
        self.docId = re.findall(r"docId.*?(w{24}?)\'\,", content)[0]
        # merge request url
        token_url = "https://wenku.baidu.com/api/doc/getdocinfo?callback=cb&doc_id=" + self.docId
        # request again
        first_json = self.get_response_content(token_url).decode()
        str_first_json = re.match(r'.*?\((\{.*?\})\).*', first_json).group(1)
        # print(str_first_json)
        the_first_json = json.loads(str_first_json)
        md5sum = the_first_json["md5sum"]
        rn = the_firston["docInfo"]["totalPageNum"]
        rsign = the_first_json["rsign"]
        # print(md5sum, "-->",rn)
        # request target url
        target_url = "https://wkretype.bdimg.com/retype/text/" + self
