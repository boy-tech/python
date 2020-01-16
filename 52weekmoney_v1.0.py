"""
作者：boy-tech
功能：52周存钱挑战
版本：1.0
日期：23/12/2019
"""


def main():
    money_per_week = 10      # 每周存入的金额
    week = 1                 # 记录周数
    increase_money = 10      # 递增的金额
    total_week = 52          # 总的周数
    saving = 0               # 账户累计

    while week <= total_week:
        # 存钱操作
        saving += money_per_week

        # 输出信息
        print('第{}周，存入{}元，账户累计{}元'.format(week, money_per_week, saving))

        # 更新下一周存钱金额
        money_per_week += increase_money
        week += 1


if __name__ == '__main__':
    main()