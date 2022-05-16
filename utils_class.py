import requests
import re
import sys
import time
import io
import os
import random
import requests
import json


class File_Interact():
    def __init__(self,file_name):
        self.file_name=file_name

    def write_file(self,ndung):
        f = io.open(self.file_name, 'w', encoding='utf-8')
        f.write(ndung)
        f.close()

    def write_file_add(self,ndung):
        f = io.open(self.file_name, 'a', encoding='utf-8')
        f.write("\n" + ndung)
        f.close()
    

    
    def write_file_from_list(self, list_lines):
        f = io.open(self.file_name, 'a', encoding='utf-8')
        f.write('\n'.join(list_lines))
        f.close()
    
    
class String_Interact():
    def __init__(self):
        pass

    def regex_one_value(self,pattern, input_str):
        regex1=re.compile(pattern)
        kq=regex1.search(input_str)
        if kq:
            kq=kq.group(1)
        else:
            kq=''
        return kq

    def regex_one_value1(self,pattern, input_str):
        regex1=re.compile(pattern)
        kq=regex1.search(input_str)
        if kq:
            kq = match.group()
        else:
            kq=''
        return kq

    def regex_many_value(self,pattern, input_str):
        regex1=re.compile(pattern)
        kq=regex1.findall(input_str)
        return kq

    def get_element_by_css_selector(self, data, css_selector):
        soup = bs4.BeautifulSoup(data, 'html.parser')
        eles=soup.select(css_selector)
        return eles #get_text() and get('href')


    def clearAttributeHtml(self, htmlraw):
        print("------clear Attribute HTML------")
        soup = BeautifulSoup(htmlraw, 'html.parser')
        try:
            for tag in soup.find_all(class_="kksr-stars"):
                tag.decompose()

            for tag in soup.find_all('div', {'class': 'adsbygoogle'}):
                tag.decompose()

            for tag in soup.find_all('div', {'class': 'mce-toc'}):
                tag.decompose()

            for tag in soup.find_all():

                if tag.name == 'a':
                    del tag['href']
                    tag.name = 'span'

                if tag.name == 'i':
                    tag.decompose()

                if tag.name == 'script':
                    tag.decompose()

                if tag.name == 'style':
                    tag.decompose()

                if tag.name == 'svg':
                    tag.decompose()

                if tag.name == 'form':
                    tag.decompose()

                if tag.name == 'iframe':
                    tag.decompose()

                if tag.name == 'noscript':
                    tag.decompose()

                if tag.name == 'textarea':
                    tag.decompose()

                if tag.name == 'input':
                    tag.decompose()

                if (type(tag.attrs) is dict and (tag.get('id') == 'ez-toc-container'
                                                 or tag.get('id') == 'toc_container'
                                                 or tag.get('id') == 'ftwp-container')):
                    tag.decompose()

                if tag.name == 'img':
                    if type(tag.attrs) is dict:
                        if 'src' in list(tag.attrs.keys()):
                            imgSrc = tag['src']
                            filename = re.search(r'/([\w_-]+[.](jpg|gif|png|jpeg))$', imgSrc)
                            if not filename:
                                if 'data-src' in list(tag.attrs.keys()):
                                    imgSrc = tag['data-src']
                                    filename = re.search(r'/([\w_-]+[.](jpg|gif|png|jpeg))$', imgSrc)
                                    if filename and 'http' in imgSrc:
                                        tag['src'] = imgSrc
                                elif 'data-lazy-src' in list(tag.attrs.keys()):
                                    imgSrc = tag['data-lazy-src']
                                    filename = re.search(r'/([\w_-]+[.](jpg|gif|png|jpeg))$', imgSrc)
                                    if filename and 'http' in imgSrc:
                                        tag['src'] = imgSrc
                                else:
                                    tag.decompose()
                            if not ('http' in imgSrc):
                                tag.decompose()
                    else:
                        tag.decompose()

            soup.prettify()
        except Exception as err:
            print('Error Filter Clear Content')
            exception_type = type(err).__name__
            print(exception_type)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            pass

        return str(soup)