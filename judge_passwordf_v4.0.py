"""
作者：boy-tech
功能：判断密码强度
版本：4.0
新增功能：读取保存的密码和强度
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

    # 读取文件
    f = open('password_3.0.txt', 'r')

    # 1.read()
    # content = f.read()

    #2.readline：一行一行的读取
    # line = f.readline()
    # print(line)
    # line = f.readline()
    #
    # line = f.readline()
    # print(line)
    # line = f.readline()
    # print(line)

    # 3.readlines：
    for line in f.readlines():
        print('读取：{}'.format(line))

    f.close()


if __name__ == '__main__':
    main()
