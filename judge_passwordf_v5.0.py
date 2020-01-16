"""
作者：boy-tech
功能：判断密码强度
版本：5.0
新增功能：将相关方法封装成一个整体：面向对象编程，定义password的一个工具类
日期：2019/12/25
"""


class PasswordTool:
    """"
    密码工具类
    """
    # 类的属性
    def __init__(self, password):
        self.password = password
        self.strength_level = 0

    def process_password(self):
        # 规则一：密码长度大于8
        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            print('密码长度要求至少8位！')

        # 规则2：包含数字
        if self.check_number_exist():
            self.strength_level += 1
        else:
            print('密码要求包含数字！')

        # 规则3： 包含字母
        if self.check_letter_exist():
            self.strength_level += 1
        else:
            print('密码要求包含字母！')

    # 类的方法
    def check_number_exist(self):

        """"
        判断字符串中是否有数字
        """
        has_number = False
        for c in self.password:
            if c.isnumeric():
                has_number = True
                break
        return has_number

    def check_letter_exist(self):
        """"
        判断字符串中是否有字母
        """

        has_letter = False
        for c in self.password:
            if c.isalpha():
                has_letter = True
                break

        return has_letter


def main():

    try_times = 5

    while try_times > 0:

        password = input('请输入密码：')
        # 实例化密码工具对象
        password_tool = PasswordTool(password)
        password_tool.process_password()

        f = open('password_5.0.txt', 'a')
        f.write('密码：{}，强度：{}\n'.format(password, password_tool.strength_level))
        f.close()

        if password_tool.strength_level == 3:
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
