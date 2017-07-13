# coding=gbk
"""
    ��ÿ���ļ����зִʣ����������ļ����ݺϲ�����
"""
import utils.data_path as dp
import jieba

numbers = 3
# ��Ҫ�ִʵ��ļ�
file_names = [dp.BlogContentSegPath + 'file' + str(i) + '.txt' for i in range(numbers)]
target_file_names = [dp.BlogContentSegPath + 'file_jieba_' + str(i) + '.txt' for i in range(numbers)]

def cut_lines(file_name,target_file_name):
    file = open(file_name, encoding="utf8")
    target_file = open(target_file_name,'w',encoding="utf8")
    line = file.readline()
    count = 0
    while line:
        if count % 10000 == 0:
            print("��ʱ���ļ�"+target_file_name+"����д��---"+"�Ѿ���" + str(count) + "�����˷ִ�")
        line = line.strip().split("\001")
        target_file.write(str(list(jieba.cut(line[1])) + list(jieba.cut(line[2])))+"\n")
        line = file.readline()
        count += 1
    file.close()

    if target_file:
        target_file.flush()
        target_file.close()



def merge_file(file_names,target_file_name):
    """
    ��Ҫ�ϲ����ļ�����ע�������ǽ����򵥵���β�ϲ�
    :param filenames: list����
    :param target_file_name:Ŀ���ļ���
    :return:
    """
    if not isinstance(file_names,list):
        print("please input file name list")
        return None

    target_file = open(target_file_name,'w',encoding="utf8")
    for name in file_names:
        count = 0
        file = open(name,encoding="utf8")
        for line in file.readlines():
            if count % 10000 == 0:
                print("��ǰ��ȡ�ļ���"+name+"----��ǰ�У�"+str(count))
            line = line.strip()
            target_file.write(line+"\n")
            count += 1
        if file:
            file.flush()
            file.close()
    if target_file:
        target_file.flush()
        target_file.close()



if __name__ == '__main__':
    # for i in range(numbers):
    #     cut_lines(file_names[i], target_file_names[i])

    target_merge_file_name = dp.BlogContentSegPath + "merge_jieba_0_2.txt"
    merge_file(target_file_names, target_merge_file_name)   #��Ŀ��Դ�ļ��ϲ�Ϊһ���ļ�