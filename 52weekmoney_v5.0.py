"""
作者：boy-tech
功能：52周存钱挑战
5.0新增功能：根据用户输入的日期，判断是一年中的第几周，然后输出相应的存款金额
版本：5.0
日期：23/12/2019
"""

import math
import datetime


def save_money_in_n_weeks(money_per_week, increase_money, total_week):
    """
     计算n周内的存款金额

    """
    saved_money_list = []                                   # 记录每周账户累计
    total_week_money = []                                   # 记录每周存钱数的列表

    for week in range(total_week):
        # 存钱操作
        total_week_money.append(money_per_week)  # 每周的钱存入列表
        saving = math.fsum(total_week_money)
        saved_money_list.append(saving)

        # 更新下一周存钱金额
        money_per_week += increase_money

    return saved_money_list


def main():
    money_per_week = float(input('请输入每周存入的金额：'))       # 每周存入的金额
    increase_money = float(input('请输入每周递增的金额：'))       # 递增的金额
    total_week = int(input('请输入总共的周数：'))                 # 总的周数

    # 调用函数
    saved_money_list = save_money_in_n_weeks(money_per_week, increase_money, total_week)
    input_data_str = input('请输入日期(yyyy/mm/dd)：')

    # datetime.datetime.strptime把时间字符串解析成时间////而datetime.datetime.strftime把时间解析成字符串

    input_data = datetime.datetime.strptime(input_data_str, format('%Y/%m/%d'))

    week_num = input_data.isocalendar()[1]
    print('第{}周的存款：{}元'.format(week_num, saved_money_list[week_num - 1]))


if __name__ == '__main__':
    main()