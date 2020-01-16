def file_view(file_name, line_num):
    if line_num.strip() == ':':
        begin = '1'
        end = '-1'

    (begin, end) = line_num.split(':')

    if begin == '':
        begin = '1'
    if end == '':
        end = '-1'

    if begin == '1' and end == '-1':
        prompt = '的全文'
    elif begin == '1':
        prompt = '从开始到{}结束'.format(end)
    elif end == '-1':
        prompt = '从{}到结束'.format(begin)

    else:
        prompt = '从第{}行到第{}行'.format(begin, end)
    print('文件{}{}的内容如下：'.format(file_name, prompt))

    begin = int(begin) - 1
    end = int(end)
    lines = end - begin

    f = open(file_name)

    for i in range(begin):
        f.readline()

    if lines < 0:
        print(f.read())
    else:
        for j in range(lines):
            print(f.readline(), end='')
    f.close()


def main():

    file_name = input(r'请输入要打开的文件（C:\\test.txt）：')
    line_num = input('请输入需要显示的行数【格式如 13:21 或 :21 或 21: 或 : 】：')
    file_view(file_name, line_num)


if __name__ == '__main__':
    main()
