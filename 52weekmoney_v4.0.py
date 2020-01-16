"""
作者：boy-tech
功能：52周存钱挑战
4.0新增功能：灵活设置每周的存款数，增加的存款及存款周数
版本：4.0
日期：23/12/2019
"""

import math

# 全局变量
# saving = 0


def save_money_in_n_weeks(money_per_week, increase_money, total_week):
    """
     计算n周内的存款金额

    """
    # 声明全局变量
    # global saving

    saving = 0                                              # 账户累计
    total_week_money = []                                   # 记录每周存钱数的列表

    for week in range(total_week):
        # 存钱操作
        total_week_money.append(money_per_week)  # 每周的钱存入列表
        saving = math.fsum(total_week_money)

        # 更新下一周存钱金额
        money_per_week += increase_money

    return saving


def main():
    money_per_week = float(input('请输入每周存入的金额：'))     # 每周存入的金额
    increase_money = float(input('请输入每周递增的金额：'))     # 递增的金额
    total_week = int(input('请输入总共的周数：'))              # 总的周数
    #saving = 0
    # 调用函数
    saving = save_money_in_n_weeks(money_per_week, increase_money, total_week)
    print('总的存款金额:', saving)


if __name__ == '__main__':
    main()