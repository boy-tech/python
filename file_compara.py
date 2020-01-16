def file_com(file_name1, file_name2):
    f1 = open(file_name1)
    f2 = open(file_name2)
    count = 0 # 统计行数
    differ = []# 统计不一样的数量
    for line1 in f1:
        line2 = f2.readline()
        count += 1
        if line1 != line2:
            differ.append(count)

    f1.close()
    f2.close()
    return differ


def main():
    file_name1 = input('请输入需要比较的头一个文件名：')
    file_name2 = input('请输入需要比较的另一个文件名：')
    differ = file_com(file_name1, file_name2)

    if len(differ) == 0:
        print('两个文件完全相同!')
    else:
        print('两个文件共有{}处不一样'.format(len(differ)))
        for each in differ:
            print('第{}不一样'.format(each))


if __name__ == '__main__':
    main()
# def file_compare(file1, file2):
#     f1 = open(file1)
#     f2 = open(file2)
#     count = 0 # 统计行数
#     differ = [] # 统计不一样的数量
#
#     for line1 in f1:
#         line2 = f2.readline()
#         count += 1
#         if line1 != line2:
#             differ.append(count)
#
#     f1.close()
#     f2.close()
#     return differ
#
# file1 = input('请输入需要比较的头一个文件名：')
# file2 = input('请输入需要比较的另一个文件名：')
#
# differ = file_compare(file1, file2)
#
# if len(differ) == 0:
#     print('两个文件完全一样！')
# else:
#     print('两个文件共有【%d】处不同：' % len(differ))
#     for each in differ:
#         print('第 %d 行不一样' % each)
