"""
作者：boy-tech
功能：52周存钱挑战
2.0新增功能：记录每周的存钱数
版本：2.0
日期：23/12/2019
"""

import math


def main():
    money_per_week = 10      # 每周存入的金额
    week = 1                 # 记录周数
    increase_money = 10      # 递增的金额
    total_week = 52          # 总的周数
    saving = 0               # 账户累计
    total_week_money = []    # 记录每周存钱数的列表


    while week <= total_week:
        # 存钱操作

        total_week_money.append(money_per_week)  # 每周的钱存入列表
        saving = math.fsum(total_week_money)

        # 输出信息

        print('第{}周，存入{}元，账户累计{}元'.format(week, money_per_week, saving))

        # 更新下一周存钱金额
        money_per_week += increase_money
        week += 1




if __name__ == '__main__':
    main()