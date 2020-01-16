""""
作者：boy-tech
功能：空气质量检测（AQI）,网络爬虫所有城市实时数据并保存到本地（csv），利用pandas分析数据
版本：9.0
日期：2019/12/28
"""

import pandas as pd


def main():
    """
    主函数
    """
    aqi_date = pd.read_csv('china_city_aqi.csv')
    print('基本信息：')
    print(aqi_date.info())

    print('数据预览：')

    print(aqi_date.head())

    # 基本统计

    print('AQI最大值:', aqi_date['AQI'].max())
    print('AQI最小值:', aqi_date['AQI'].min())
    print('AQI均值:', aqi_date['AQI'].mean())

    # top10空气质量城市
    top10_cities = aqi_date.sort_values(by=['AQI']).head(10)
    print('空气质量最好的10个城市')
    print(top10_cities)

    # bottom10 最差的10个城市
    # bottom10_cities = aqi_date.sort_values(by=['AQI']).tail(10)
    # 降序排列
    bottom10_cities = aqi_date.sort_values(by=['AQI'], ascending=False).head(10)
    print('空气质量最差的10个城市')
    print(bottom10_cities)

    # 数据保存成CSV
    top10_cities.to_csv('top10_aqi.csv', index=False)
    bottom10_cities.to_csv('bottom10_aqi.csv', index=False)


if __name__ == '__main__':
    main()