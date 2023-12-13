import requests
import datetime
from bs4 import BeautifulSoup
import random

def convert_date_str_to_ts(date_str):
    # dtae_str format YYYY/MM/DD
    year, month, day = [ int(date_info) for date_info in date_str.split('/') ]
    dtime = datetime.datetime(year, month, day)
    ts = int(dtime.timestamp())
    return ts

class infocarwler():
    def __init__(self):
        self.base_url = ''
        self.headers = {}
        self.user_agent_list = [
        	#Chrome
        	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        	'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        	'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        	'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        	'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        	'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        	'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        	'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        	#Firefox
        	'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
        	'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        	'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
        	'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
        	'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
        	'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
        	'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
        	'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
        	'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
        	'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
        	'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
        	'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
        	'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
    	]
    def set_random_user_agent(self):
        user_agent = random.choice(self.user_agent_list)
        self.headers['User-Agent'] = user_agent
        return user_agent
    def get_result_data(self, *args, **kwargs):
        pass
    def parse_page(self, raw_response):
        pass

class yahooFinanceCrawler(infocarwler):
    # ctrl 오른쪽왼쪽대괄호 -> 들여쓰기
    def __init__(self):
        super().__init__()
        self.base_url = "https://query2.finance.yahoo.com/v8/finance/chart/{}?interval=1d&period1={}&period2={}"
        self.set_random_user_agent

    def get_result_data(self, target_code, from_date_str, to_date_str):
        # [ {timeStamp: int, open_price: float, close_price: float, .....}, {}, {} ]
        from_ts = convert_date_str_to_ts(from_date_str)
        to_ts = convert_date_str_to_ts(to_date_str)
        target_url = self.base_url.format(target_code, from_ts, to_ts)
        res = requests.get(target_url, headers=self.headers)
        res_list = self.parse_page(res)
        return res_list
    def parse_page(self, raw_response):
        print(raw_response.text)

class naverFinanceCrawler(infocarwler):
    def __init__(self):
        super().__init__()
        self.base_url = 'https://finance.naver.com'
    def set_random_user_agent(self):
        pass
    def get_result_data(self, *args, **kwargs):
        pass
    def parse_page(self, raw_response):
        pass

class marketBuyerInforCrawler(naverFinanceCrawler):
    def __init__(self):
        super().__init__()
        self.base_url = ''
    def set_random_user_agent(self):
        pass
    def get_result_data(self, *args, **kwargs):
        pass
    def parse_page(self, raw_response):
        pass


# [ {timeStamp: int, open_price: float, close_price: float, .....}, {}, {} ]
# ts = convert_date_str_to_ts('2023/04/13')
yfc = yahooFinanceCrawler()
result_list = yfc.get_result_data('GC=F', '2023/03/14', '2023/04/12')
