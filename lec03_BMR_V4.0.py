"""
作者：boy-tech
功能：基础代谢率的计算
4.0增加功能：处理异常操作
版本：4.0
日期：23/12/2019            15：17
"""


def BMR_caculater():
    Y_or_N = input('是否退出程序（Y/N）?')
    while Y_or_N != 'Y':
        print('请输入以下信息,用空格分隔')
        infor = input('性别 体重(kg) 身高(cm) 年龄：')
        infor_list = infor.split(' ')
        try:

            gender = infor_list[0]
            weight = float(infor_list[1])
            height = float(infor_list[2])
            age = int(infor_list[3])
            if gender == '男':
                bmr = 13.7 * weight + 5.0 * height - 6.8 * age + 66

            elif gender == '女':

                bmr = 9.6 * weight + 1.8 * height - 4.7 * age + 655
            else:

                bmr = -1
            if bmr != -1:
                print('您的性别{},体重{}公斤，身高{}厘米，年龄{}岁'.format(gender, weight, height, age))
                print('您的基础代谢率为{}卡路里'.format(bmr))

            else:
                print('对不起暂不支持该性别')

        except ValueError:
            print('请输入正确的信息！')
        except IndexError:
            print('输入的信息过少！')
        except:
            print('程序异常！')

        print()  # 输出空行
        Y_or_N = input('是否退出程序（Y/N）?')

def main():
    """
     主函数
    """
    BMR_caculater()


if __name__ == '__main__':
    main()