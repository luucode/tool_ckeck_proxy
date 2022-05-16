# -*- coding: utf-8 -*-
import requests
from utils_class import *
import requests
import time
import random
import pandas as pd
from multiprocessing import Pool

string_interact = String_Interact()

def check_proxy_bing(pxoxy_i):

    proxies = {
    'http': f'http://cwuhlvjy:iz6kjcfioplp@{pxoxy_i}',
    'https': f'http://cwuhlvjy:iz6kjcfioplp@{pxoxy_i}'
    }

    # Search từ khoá bing
    try:
        url = f"""https://www.bing.com/search?q=seo là gì"""
        list_user_agent = [
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                'Mozilla/5.0 (Windows NT 10.0; Win 64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
            ]

        list_cookie = [
            'MUID=3FAB619E6D3962DC22FB716A6CF163D4; MUIDB=3FAB619E6D3962DC22FB716A6CF163D4; _EDGE_V=1; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=DEE7D89E12E244FB861BEF615E015EEB&dmnchg=1; _SS=SID=0B395B558E506A2A38CD4BA18F986B71; _EDGE_S=F=1&SID=0B395B558E506A2A38CD4BA18F986B71&mkt=vi-vn; SUID=M; MicrosoftApplicationsTelemetryDeviceId=2a7eca06-fb30-4146-b805-10fe7c9a44e6; ABDEF=V=13&ABDV=11&MRNB=1643809008347&MRB=0; _HPVN=CS=eyJQbiI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMi0wMi0wM1QwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIkRmdCI6bnVsbCwiTXZzIjowLCJGbHQiOjAsIkltcCI6MTJ9; ipv6=hit=1643880298411&t=6; ai_session=0+zjBc7/F4ieMzbRiWYaKx|1643876698727|1643876698727; SRCHUSR=DOB=20211119&T=1643876696000&TPC=1643876700000; SRCHHPGUSR=SRCHLANG=vi&BRW=XW&BRH=S&CW=1920&CH=585&SW=1920&SH=1080&DPR=1&UTC=420&DM=0&WTS=63779473496&HV=1643876701',
            'SUID=M; MUID=0C00920D1BA46BE00E2783331AC26A75; MUIDB=0C00920D1BA46BE00E2783331AC26A75; _EDGE_V=1; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=DC3F66DDD1754E03BA20A7C0C9EF20A6&dmnchg=1; _SS=SID=398CF21D49B4660211E1E32348D26787; _HPVN=CS=eyJQbiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMi0wMi0wMVQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIkRmdCI6bnVsbCwiTXZzIjowLCJGbHQiOjAsIkltcCI6Mn0=; ipv6=hit=1643717451181&t=6; MicrosoftApplicationsTelemetryDeviceId=3a869d55-fa4b-4921-ab85-62a88d071085; ai_session=dE1LHnv4XtoOT/S1Zr9287|1643713851898|1643713851898; _EDGE_S=F=1&SID=398CF21D49B4660211E1E32348D26787&mkt=vi-vn; SRCHUSR=DOB=20220201&T=1643713841000&TPC=1643713854000; dsc=order=Video; SRCHHPGUSR=SRCHLANG=vi&BRW=XW&BRH=S&CW=1920&CH=383&SW=1920&SH=1080&DPR=1&UTC=420&DM=0&WTS=63779310641&HV=1643714514',
            'MUID=327E4BECA47468621A9F5B03A512695B; MUIDB=327E4BECA47468621A9F5B03A512695B; _EDGE_V=1; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=40268E97A4834224A100E4B7617086A0&dmnchg=1; SUID=M; _SS=SID=06300B156356602A1C7F1A5562306191; SRCHUSR=DOB=20211114&T=1643876783000&TPC=1636882358000; _HPVN=CS=eyJQbiI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMi0wMi0wM1QwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIkRmdCI6bnVsbCwiTXZzIjowLCJGbHQiOjAsIkltcCI6Nn0=; ipv6=hit=1643880385158&t=6; MicrosoftApplicationsTelemetryDeviceId=7a0ddb8b-2a3c-42dd-a07b-2be294affe38; _EDGE_S=SID=06300B156356602A1C7F1A5562306191&mkt=vi-vn; ai_session=CZc45VBx0UKSEeq8azKpQK|1643876785938|1643876785938; SRCHHPGUSR=SRCHLANG=vi&BRW=W&BRH=M&CW=1365&CH=969&SW=1920&SH=1080&DPR=1&UTC=420&DM=0&HV=1643876785&WTS=63779473583',
            'SUID=M; MUID=34F9155D7234611B3853041D7352602B; MUIDB=34F9155D7234611B3853041D7352602B; _EDGE_V=1; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=66312FC986974C448085837A827DE9A7&dmnchg=1; _SS=SID=161068504B1D6475353879104A7B6556; SRCHUSR=DOB=20220203&T=1643876846000; _HPVN=CS=eyJQbiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMi0wMi0wM1QwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIkRmdCI6bnVsbCwiTXZzIjowLCJGbHQiOjAsIkltcCI6Mn0=; ipv6=hit=1643880448625&t=6; SRCHHPGUSR=SRCHLANG=vi&BRW=XW&BRH=S&CW=1920&CH=295&SW=1920&SH=1080&DPR=1&UTC=420&DM=0&WTS=63779473646&HV=1643876849; MicrosoftApplicationsTelemetryDeviceId=8231cfeb-4bac-461e-a88a-8604b24c652c; ai_session=byOHUnLQZ0wD8f/wmvBOfV|1643876849413|1643876849413; _EDGE_S=F=1&SID=161068504B1D6475353879104A7B6556&mkt=vi-vn'
        ]
        headers = {
            'user-agent': random.choice(list_user_agent),
            'cookie': random.choice(list_cookie)
        }
        res = requests.get(url, headers=headers, proxies=proxies, timeout=30)
        status_code1 = res.status_code
        print("Kết quả search là %s" %(status_code1))
        res = res.text
        # print(res)
        # time.sleep(5)
    except Exception as e:
        print('Bước search từ khoá: %s'%e,'')
        try:
            print("Proxy %s die" %pxoxy_i)
            # file_interact = File_Interact(f'../kq_search_bing/{keyword}_bing.html')
            file_interact = File_Interact(f'proxy_die.txt')
            file_interact.write_file_add(pxoxy_i)
        except Exception as e:
            print('Bước lưu trang kết quả tìm kiếm trang 1: %s'%e,'')

    # try:
    #     # file_interact = File_Interact(f'../kq_search_bing/{keyword}_bing.html')
    #     file_interact = File_Interact('ketqua.html')
    #     file_interact.write_file(res)
    # except Exception as e:
    #     print('Bước lưu trang kết quả tìm kiếm trang 1: %s' % e, '')

    if status_code1 != 200:

        try:
            # file_interact = File_Interact(f'../kq_search_bing/{keyword}_bing.html')
            print("Proxy %s die" % pxoxy_i)
            file_interact = File_Interact(f'proxy_die.txt')
            file_interact.write_file_add(pxoxy_i)
        except Exception as e:
            print('Bước lưu trang kết quả tìm kiếm trang 1: %s'%e,'')

    elif res.find('''"b_tween"''') == -1:
        try:
            # file_interact = File_Interact(f'../kq_search_bing/{keyword}_bing.html')
            print("Proxy %s die" % pxoxy_i)
            file_interact = File_Interact(f'proxy_die.txt')
            file_interact.write_file_add(pxoxy_i)
        except Exception as e:
            print('Bước lưu trang kết quả tìm kiếm trang 1: %s'%e,'')

    else:
        print("Proxy %s còn sống" %pxoxy_i)

    return pxoxy_i



def pool_handler(pxoxy_i):
    run = check_proxy_bing(pxoxy_i)

# B1: nhập dữ liệu keyword từ excel vào
try:
    # cấu hình đường dẫn file keyword
    path = 'list_proxy.xlsx'
    df = pd.read_excel(path, header=0, index_col=None)
    # print(df["keyword"].values)
    for_keyword = df["proxy"].values
    # id = df["id_chuyen_muc"].values
except Exception as e:
    print('Bước nhập từ khoá từ excel: %s' % e, '')


# Hàm để khởi chạy đa luồng
def main():
    try:
        p = Pool(24)
        multi = p.map_async(pool_handler, for_keyword)
        p.close()
        p.join()
    except Exception as e:
        print('Hàm để khởi chạy đa luồng lỗi: %s' % e, '')

if __name__ == '__main__':
    main()

    # pxoxy_i = "23.236.249.60:6111"
    # check_proxy_bing(pxoxy_i)