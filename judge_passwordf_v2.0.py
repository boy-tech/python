"""
作者：boy-tech
功能：判断密码强度
版本：2.0
新增功能：循环的终止,限制输入密码的次数
日期：2019/12/25
"""


def check_number_exist(password_str):

    """"
    判断字符串中是否有数字
    """
    has_number = False
    for c in password_str:
        if c.isnumeric():
            has_number = True
            break
    return has_number


def check_letter_exist(password_str):

    """"
    判断字符串中是否有字母
    """

    has_letter = False
    for c in password_str:
        if c.isalpha():
            has_letter = True
            break

    return has_letter


def main():

    try_times = 5

    while try_times > 0:

        password = input('请输入密码：')

        # 密码强度
        strength_level = 0

        # 规则一：密码长度大于8
        if len(password) >= 8:
            strength_level += 1
        else:
            print('密码长度要求至少8位！')

        # 规则2：包含数字
        if check_number_exist(password):
            strength_level += 1
        else:
            print('密码要求包含数字！')

        # 规则3： 包含字母
        if check_letter_exist(password):
            strength_level += 1
        else:
            print('密码要求包含字母！')

        if strength_level == 3:
            print('恭喜！密码强度合格！')
            break
        else:
            print('密码强度不合格！')
            try_times -= 1
            print('***************************************')
            print('您还有{}次机会！'.format(try_times))
        if try_times <= 0:
            print('尝试次数过多密码设置失败！')


if __name__ == '__main__':
    main()
