# coding=gbk
"""
    ���ݶ�ȡ
"""
import pandas as pd
import utils.data_path as dp
def read_txt(filename,columns_name,target_file=None):
    """
    ��ȡtxt����
    :param filename:
    :return:
    """
    dic = {}
    lines = open(filename,encoding="utf8").readlines()
    for line in lines:
        line = line.strip().split("\001")
        #print(line)
        if line[0] not in dic:
            dic[line[0]] = ["\001".join(line[1:])]
        else:
            dic[line[0]].append("\001".join(line[1:]))

    print("dic length----"+str(len(dic)))

    for key,value in zip(dic.keys(),dic.values()):
        if dic[key] != value:
            print("ERROR!!!!!!!!!")

    pd_data = pd.DataFrame({columns_name[0]:list(dic.keys()),columns_name[1]:list(dic.values())})

    if target_file:
        pd_data.to_csv(target_file,encoding="utf8")

    return pd_data

def read_special_txt(filename):
    """
    ��ȡtxt����
    :param filename:
    :return:
    """
    file = open(filename,encoding="utf8")
    count = 0
    while True:
        line = file.readline()
        print(line.strip())

        count += 1
        if count == 10:
            break

def train_data(train_file=None):
    pd_post = read_txt(dp.PostTxt,['uid','post'],dp.PostCSV)
    pd_brows = read_txt(dp.BrowseTxt,['uid','brows'],dp.BrowseCSV)
    pd_comment = read_txt(dp.CommentTxt,['uid','comment'],dp.CommentCSV)
    pd_voteup = read_txt(dp.VoteupTxt,['uid','voteup'],dp.VoteupCSV)
    pd_votedown = read_txt(dp.VotedownTxt,['uid','votedown'],dp.VotedownCSV)
    pd_favorite = read_txt(dp.FavoriteTxt,['uid','favorite'],dp.FavoriteCSV)

    #print(pd.merge(pd_post,pd_brows,on="uid"))
    # print(pd_post.join([pd_brows,pd_comment,pd_voteup,pd_votedown,pd_favorite],how="inner"))

    pd_follow = read_txt(dp.FollowTxt,['uid','follow'],dp.FollowCSV)
    pd_letter = read_txt(dp.LetterTxt,['uid','letter'],dp.LetterCSV)

    pd_train = read_txt(dp.TrainTxt,['uid','labels'],dp.TrainCsv)

    pd_train['post'] = [None]*len(pd_train)
    pd_train['brows'] = [None]*len(pd_train)
    pd_train['comment'] = [None]*len(pd_train)
    pd_train['voteup'] = [None]*len(pd_train)
    pd_train['votedown'] = [None]*len(pd_train)
    pd_train['favorite'] = [None]*len(pd_train)
    pd_train['follow'] = [None]*len(pd_train)
    pd_train['letter'] = [None]*len(pd_train)

    def f(pd_data,row,con_column,target_column):
        if row[con_column] in list(pd_data[con_column]):  #���pd�а�����uid�����ҳ���һ����valueֵ��ͬʱ���uid����Ψһ��
            #print("�ҵ���-------------")
            return list(pd_data[pd_data[con_column] == row[con_column]][target_column])[0]   #ȷ��ֻ����һ��
        else:
            #print("δ�ҵ�")
            return None #���򷵻ؿ�

    print(pd_train)
    count = 0
    for index,row in pd_train.iterrows():
        print("��ǰindexΪ��"+str(index))
        #��Ϊ����
        pd_train['post'][index] = f(pd_post,row,'uid','post')
        pd_train['brows'][index] = f(pd_brows,row,'uid','brows')
        pd_train['comment'][index] = f(pd_comment,row,'uid','comment')
        pd_train['voteup'][index] = f(pd_voteup,row,'uid','voteup')
        pd_train['votedown'][index] = f(pd_votedown,row,'uid','votedown')
        pd_train['favorite'][index] = f(pd_favorite,row,'uid','favorite')

        if None not in list(row):
            count += 1

        #�罻����
        pd_train['follow'][index] = f(pd_follow,row,'uid','follow')
        pd_train['letter'][index] = f(pd_letter,row,'uid','letter')


    print("ȫ�����ݶ��е���---"+str(count))


    print(pd_train)

    if train_file:
        pd_train.to_csv(train_file,encoding="utf8")



if __name__ == '__main__':
    train_data(dp.TrainCsv)

    #read_special_txt(dp.BlogContentTxt)


"""
ѵ������
ӵ��ȫ����Ϊ���罻���ݶ��е���---2���û�
ӵ��ȫ����Ϊ������
"""