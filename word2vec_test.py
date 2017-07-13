# coding=gbk
"""
    ��Word2vec���в���
"""
import gensim
import utils.data_path as dp
import jieba

numbers = 5
# ��Ҫд����ļ�
file_names = [dp.BlogContentSegPath + 'file1_' + str(i) + '.txt' for i in range(numbers)]
target_model_names = [dp.CSDNMODELPath + "csdn_model_1_" + str(i) + ".m" for i in range(numbers)]

"""
#���ȶ�ĳ���ļ�����ֱ��ѵ��
file = open(file_names[0],encoding="utf8")
line = file.readline()
count = 0
result = []
while line:
    if count % 10000 == 0:
        print("�Ѿ���"+str(count)+"�����˷ִ�")
    line = line.strip().split("\001")
    result.append(list(jieba.cut(line[2])))
    line = file.readline()
    count += 1
file.close()

model = gensim.models.Word2Vec(result, min_count=1)
model.save(target_model_names[0])
"""

#����ԭ�ȵ�ģ�ͣ�����voca
model = gensim.models.Word2Vec.load(dp.CSDNMODELPath + "csdn_model_0.m")
file = open(file_names[0], encoding="utf8")
line = file.readline()
count = 0
result = []
while line:
    if count % 10000 == 0:
        print("�Ѿ���" + str(count) + "�����˷ִ�")
    line = line.strip().split("\001")
    result.append(list(jieba.cut(line[2])))
    line = file.readline()
    count += 1
file.close()

model.build_vocab(result)   #����vocabulary
model.train(result)   #���²���
model.save(target_model_names[1])   #ע�⣬�����Ǵ����model_1_1�еģ������Ǽ���file_1_0
