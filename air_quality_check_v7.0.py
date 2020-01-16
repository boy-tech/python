""""
作者：boy-tech
功能：空气质量检测（AQI）,网络爬虫所有城市实时数据
版本：6.0
日期：2019/12/28
"""


import requests
from bs4 import BeautifulSoup


def get_city_aqi(city_pinyin):
    """
    获取城市的aqi值
    """
    url = 'http://pm25.in/' + city_pinyin
    r = requests.get(url, timeout=50)
    soup = BeautifulSoup(r.text, 'lxml')
    div_list = soup.find_all('div', {'class': 'span1'})

    city_aqi = []
    for i in range(8):
        div_content = div_list[i]
        caption = div_content.find('div', {'class': 'caption'}).text.strip()
        value = div_content.find('div', {'class': 'value'}).text.strip()
        city_aqi.append((caption, value))
    return city_aqi


def get_all_cities():
    """
    获取所有城市的数据

    """
    url = 'http://pm25.in/'
    city_list = []
    r = requests.get(url, timeout=50)
    soup = BeautifulSoup(r.text, 'lxml')

    city_div = soup.find_all('div', {'class': 'bottom'})[1]
    city_link_list = city_div.find_all('a')
    for city_link in city_link_list:
        city_name = city_link.text
        city_pinyin = city_link['href'][1:]
        city_list.append((city_name, city_pinyin))
    return city_list


def main():
    """
    主函数
    """
    city_list = get_all_cities()
    for city in city_list:
        city_name = city[0]
        city_pinyin = city[1]
        city_aqi = get_city_aqi(city_pinyin)
        print(city_name, city_aqi)


if __name__ == '__main__':
    main()