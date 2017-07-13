# coding=gbk
"""
    �����ṩ�����Ͽ���ѵ��������
"""
import gensim
import utils.data_path as dp
import jieba


def target_train(filename,target_model_file):
    """
    ֱ�Ӷ�ָ�������ļ�ѵ��word2vec�����ܻ���Ϊ������������ڴ�����������޸ĺ����Ѿ��ִʺ������
    :param filename:��Ҫ��ȡ�������ļ������Ѿ��ֺô���
    :param target_model_file:��Ҫд���ģ���ļ���
    :return:
    """
    file = open(filename,encoding="utf8")
    # lines = file.readlines()
    # print("�ܹ���---"+str(len(lines)))
    # print("��һ����������Ϊ---"+str(type(lines[0])))

    line = file.readline()
    count = 0
    result = []
    while line:
        #print("��ǰ��--"+str(line))
        if count % 10000 == 0:
            print("�Ѿ���ȡ��---"+str(count)+"---��")
        result.append(eval(line.strip()))
        line = file.readline()
        count += 1
    file.close()

    model = gensim.models.Word2Vec(result, min_count=1)
    model.save(target_model_file)


def continue_train(modelname,filename,target_model_file=None):
    """
    ��ԭģ���м���ģ�ͣ�����µ�����ѵ����ģ�ͣ������Ҫд���µ�ģ���ļ���д�룬����д��ԭģ���ļ�
    :param modelname:ԭģ���ļ���
    :param filename:�����ļ���
    :param target_model_file:д���Ŀ���ļ���
    :return:
    """
    model = gensim.models.Word2Vec.load(modelname)

    file = open(filename, encoding="utf8")
    line = file.readline()
    count = 0
    result = []
    while line:
        if count % 10000 == 0:
            print("�Ѿ���ȡ��"+str(count)+"��")
        line = line.strip().split("\001")
        result.append(list(jieba.cut(line[2])))
        line = file.readline()
        count += 1
    file.close()

    model.update_vocab(result)   #����vocabulary
    model.train(result)   #���²���
    if target_model_file:
        model.save(target_model_file)
    else:
        model.save(modelname)



if __name__ == '__main__':
    # ��Ҫд����ļ�
    file_name = dp.BlogContentSegPath + "merge_jieba_0_2.txt"
    target_model_name = dp.CSDNMODELPath + "csdn_model_merge_0_2.m"

    target_train(file_name, target_model_name)   #�������ļ�����ѵ��
