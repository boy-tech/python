""""
作者：boy-tech
功能：空气质量检测（AQI）,网络爬虫所有城市实时数据并保存到本地（csv），利用pandas分析数据,清洗数据，数据可视化
版本：10.0
日期：2019/12/28
"""

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    """
    主函数
    """
    aqi_date = pd.read_csv('china_city_aqi.csv')
    print('基本信息：')
    print(aqi_date.info())

    print('数据预览：')

    print(aqi_date.head())

    # 数据清洗
    # 只保留AQI>0的数据
    # filter_condition = aqi_date['AQI'] > 0
    # clean_aqi_date = aqi_date[filter_condition]

    clean_aqi_date = aqi_date[aqi_date['AQI'] > 0]

    # 基本统计

    print('AQI最大值:', clean_aqi_date['AQI'].max())
    print('AQI最小值:', clean_aqi_date['AQI'].min())
    print('AQI均值:', clean_aqi_date['AQI'].mean())

    # top50空气质量城市
    top50_cities = clean_aqi_date.sort_values(by=['AQI']).head(50)
    # print('空气质量最好的10个城市')
    # print(top50_cities)

    # 数据可视化
    top50_cities.plot(kind='bar', x='City', y='AQI', title='空气质量最好的50个城市',
                      figsize=(20, 10))
    plt.savefig('top50_bar_aqi.png')
    plt.show()

    # bottom10 最差的10个城市
    # bottom10_cities = aqi_date.sort_values(by=['AQI']).tail(10)
    # 降序排列
    # bottom10_cities = clean_aqi_date.sort_values(by=['AQI'], ascending=False).head(10)
    # print('空气质量最差的10个城市')
    # print(bottom10_cities)

    # 数据保存成CSV
    # top10_cities.to_csv('top10_aqi.csv', index=False)
    # bottom10_cities.to_csv('bottom10_aqi.csv', index=False)


if __name__ == '__main__':
    main()