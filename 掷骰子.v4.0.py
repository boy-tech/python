"""
 作者：boy-tech
 功能：模拟掷骰子（一个）
 2.0新增功能：模拟掷骰子（2个）
 3.0新增功能：模拟掷骰子（2个）,可视化其结果
 4.0新增功能：直方图可视化结果
 版本：4.0
 日期：2019/12/26
"""
import random
import matplotlib.pyplot as plt

# 改了之后支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def roll_dice():
    """
    模拟掷骰子
    """
    roll = random.randint(1, 6)
    return roll


def main():
    total_times = 1000
    # 记录骰子的结果
    roll_list = []

    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()

        roll_list.append(roll1 + roll2)

    plt.hist(roll_list, bins=range(2, 14), normed=1,  edgecolor='black', linewidth=1)
    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('频率')
    plt.show()


if __name__ == '__main__':
    main()