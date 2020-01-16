def file_view(file_name, line_num):
    print('文件{}的前{}的内容如下:'.format(file_name, line_num))
    f = open(file_name)
    for i in range(int(line_num)):
        print(f.readline(), end='')
    f.close()


def main():
    file_name = input('请输入要打开的文件：')
    line_num = input('请输入需要显示该文件前几行：')
    file_view(file_name, line_num)


if __name__ == '__main__':
    main()
