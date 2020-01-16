f = open('record.txt')
boy = []
girl = []
count = 1

for each_line in f:

    if each_line[:6] != '======':
        # 我们这里进行字符串操作(分隔)
        (role, line_spoken) = each_line.split(':', 1)
        if role == '小甲鱼':
            boy.append(line_spoken)
        elif role == '小甲鱼':
            girl.append(line_spoken)

    else:
        # 文件的分别保存操作
        file_name_boy = 'boy' + str(count) + '.txt'
        file_name_girl = 'girl' + str(count) + '.txt'

        boy_file = open(file_name_boy, 'w')
        girl_file = open(file_name_girl, 'w')

        boy_file.writelines(boy)
        girl_file.writelines(girl)

        boy_file.close()
        girl_file.close()

        boy = []
        girl = []
        count += 1

file_name_boy = 'boy' + str(count) + '.txt'
file_name_girl = 'girl' + str(count) + '.txt'

boy_file = open(file_name_boy, 'w')
girl_file = open(file_name_girl, 'w')

boy_file.writelines(boy)
girl_file.writelines(girl)

boy_file.close()
girl_file.close()


f.close()


