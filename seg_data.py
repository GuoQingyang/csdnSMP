# coding=gbk
"""
    �����ݷ�Ϊ��ݣ����ÿ����8����
"""
import numpy as np
import utils.data_path as dp

file = open(dp.BlogContentSegPath+"file1.txt", encoding="utf8")
lines = file.readlines()
lines_len = len(lines)
print("lines length----",lines_len)
#�����ݷ�Ϊ5��
numbers= 5
#��Ҫд����ļ�
file_names = [dp.BlogContentSegPath+'file1_'+str(i)+'.txt' for i in range(numbers)]

def seg_list(ls,n):
    """
    ���б�ȷֳ�n��
    :param ls: ��Ҫ�ȷֵ��б�
    :param n: �ȷֵķ���
    :return:
    """
    if not isinstance(ls,list) or not isinstance(n,int):
        return []
    ls_len = len(ls)
    if n<=0 or ls_len == 0:
        return []
    if n>ls_len:
        return []
    elif n == ls:
        return [[i] for i in ls]
    else:
        k = int(ls_len/n)
        ls_return = []
        for i in np.arange(0,(n-1)*k,k):
            ls_return.append(ls[int(i):int(i+k)])  #��ȷ�����һ���Ƿ�ȫ������
        ls_return.append(ls[(n-1)*k:])  #�����Ҫ������������һ��
        return ls_return


div_list = seg_list(list(range(lines_len)),numbers)

print("div list is:",div_list)

def get_line(lines,list_indexs,file):
    for i in list_indexs:
        if i % 10000 == 0:
            print("now lines index---",i)
        file.write(lines[i])
    if file:
        file.flush()
        file.close()

for i in range(len(div_list)):   #div_list���Ⱥ�filenames����һ��
    if len(file_names) != len(div_list):
        print("file names length not equal div list length!")
        break
    print("now iter "+str(i)+" list! file name "+file_names[i])
    file = open(file_names[i],'w',encoding="utf8")
    get_line(lines,div_list[i],file)   #�Ѿ������洦����ļ�����͹ر�

lines = []
del lines