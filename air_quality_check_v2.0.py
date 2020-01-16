""""
作者：boy-tech
功能：空气质量检测（AQI）
版本：2.0
日期：2019/12/26
"""

import json


def process_json_file(filepath):
    """
    解码json文件
    """
    f = open(filepath, mode='r', encoding='utf-8')

    # 读取json文件转换成python的数据类型
    city_list = json.load(f)
    return city_list


def main():
    """
    主函数
    """

    filepath = input('请输入json文件：')
    city_list = process_json_file(filepath)
    # 以城市的AQI从小到大排序
    city_list.sort(key=lambda city: city['aqi'])
    top5_list = city_list[:]

    f = open('top5_aqi.json', mode='w', encoding='utf-8')

    # 读取python文件转换成json的数据类型
    json.dump(top5_list, f, ensure_ascii=False)
    f.close()


if __name__ == '__main__':
    main()