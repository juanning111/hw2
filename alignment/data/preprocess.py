from collections import defaultdict
import re

dir='paragraph/'
filename='文心雕龙.txt'

data=defaultdict(list)

with open(filename,encoding='utf-8') as file:
    i=1 #序号 防止文件存储后乱序
    for line in file:
        if line.strip()=='':
            continue
        if re.match(r"..第.?",line):
            flag=True #为True时表示原文 为False表示译文
            title=line.strip()
            title1=str(i)+'《'+title+'》原文'
            title2=str(i)+'《'+title+'》译文'
            i+=1
            continue
        if re.match(r"【译文】",line):
            flag=False
            continue
        sentence=re.split('[。|？|！]',line.strip())
        sentence.pop() #去掉split在句子最后产生的空字符串
        if flag:
            data[title1]+=sentence
        else:
            data[title2]+=sentence

for title in (data):
    file=open(dir+title+'.txt','w',encoding='utf-8')
    for line in data[title]:
        file.write(line+'\n')