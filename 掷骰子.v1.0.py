"""
 作者：boy-tech
 功能：模拟掷骰子（一个）
 版本：1.0
 日期：2019/12/25
"""
import random


def roll_dice():
    """
    模拟掷骰子
    """
    roll = random.randint(1, 6)
    return roll


def main():
    total_times = 100000
    # 初始化列表[0,0,0,0,0,0]
    result_list = [0]*6
    for i in range(total_times):
        roll = roll_dice()
        for j in range(1, 7):
            if roll == j:
                result_list[j - 1] += 1

    # enumerate获取元素及其下标
    for index, result_happen in enumerate(result_list):
        print('点数{}的次数--{}--频率{}'.format(index + 1, result_happen, result_happen / total_times))


if __name__ == '__main__':
    main()