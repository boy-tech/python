"""
   作者：boy-tech
   功能：基础代谢率的计算
   增加功能：根据用户输入计算BMR，程序持续运行
   版本：2.0
   日期：23/12/2019               15：17
"""


def main():
    """
     主函数
    """
    Y_or_N = input('是否退出程序（Y/N）?')

    while Y_or_N != 'Y':
        gender = input('性别:')
        weight = float(input('体重(kg):'))
        height = float(input('身高(cm):'))
        age = int(input('年龄:'))

        if gender == '男':
            bmr = 13.7 * weight + 5.0 * height - 6.8 * age + 66

        elif gender == '女':

            bmr = 9.6 * weight + 1.8 * height - 4.7 * age + 655
        else:

            bmr = -1
        if bmr != -1:
            print('基础代谢率（卡路里)：', bmr)

        else:
            print('不支持该性别')

        print()      # 输出空行
        Y_or_N = input('是否退出程序（Y/N）?')


if __name__ == '__main__':
    main()