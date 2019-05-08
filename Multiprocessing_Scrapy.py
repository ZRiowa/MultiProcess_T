import json
from multiprocessing import Pool
import requests
from requests.exceptions import RequestException
import re

def get_one_page(url): #判断页面的请求状态来做异常处理
    try:
        response = requests.get(url)
        if response.status_code == 200:#200是请求成功
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?<p class="name">.*?data-val.*?>(.*?)</a>'#正则表达式
                         +'.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         +'.*?integer">(.*?)</i>.*?fraction">(\d+)</i>.*?</dd>',re.S)
    items = re.findall(pattern, html) #返回正则结果
    for item in items:  #对结果进行迭代，修饰
        yield{
            '排名：':item[0],
            '电影：':item[1],
            '主演：':item[2].strip()[3:],
            '上映时间：':item[3].strip()[5:],
            '评分：':item[4]+item[5]
        }
def write_to_file(content): #写入文件“result.txt”中
    with open('result.txt', 'a', encoding='utf-8') as f: #以utf-8的编码写入
        f.write(json.dumps(content, ensure_ascii=False) + "\n") #json序列化默认使用ascii编码，这里禁用ascii
        f.close()

def main(page):
    url = "http://maoyan.com/board/4?offset=" + str(page) #page 为页码数
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    '''
    for i in range(10):
        main(i*10)
    '''
    pool = Pool() #建立进程池
    pool.map(main, (i*10 for i in range(10)))#映射到主函数中进行循环
