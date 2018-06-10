#coding=utf-8
from nltk.stem import WordNetLemmatizer 
import nltk



def get_wordnet_pos(treebank_tag): #nltk的tag需要转换为wordnet的tag以便做词性还原
    if treebank_tag.startswith('J'):
        return 'a'
    elif treebank_tag.startswith('V'):
        return 'v'
    elif treebank_tag.startswith('N'):
        return 'n'
    elif treebank_tag.startswith('R'):
        return 'r'
    else:
        return 'n'

def lemmatize(word):
    #传入一个tuple：('morning', 'NN')
    lemmatizer = WordNetLemmatizer()
    wordLowercase=word[0].lower()
    return lemmatizer.lemmatize(wordLowercase, pos=get_wordnet_pos(word[1]))

def match(word,cn):

    result=True #默认是有匹配的
    for entry in ecDic[word]:
        if cn.find(entry)==-1: #该释义没有匹配，查看其同义词是否匹配
            result=False
            if entry in synonymsDic:
                synResult=False #同义词默认不匹配
                for syn in synonymsDic[entry]:  #查看该释义的同义词是否有匹配
                    if cn.find(syn)!=-1:
                        print("有同义词释义“"+syn+"”对应")
                        synResult=True
                if synResult==True: #遍历所有同义词后如果有匹配
                    result=True
        else:
            print("有释义“"+entry+"”对应")
            result=True

    return result
        



#加载词典
ecDic={}
synonymsDic={}
fd=open("en2cn.dic","r",encoding="utf-8")
for line in fd.readlines():
    line=line.replace("\n","")
    splitted=line.split("\t")
    key=splitted[0]
    entryList=[]
    for i in range(1,line.count("\t")+1):
        entryList.append(splitted[i])
    ecDic[key]=entryList
fd.close()

fd=open("synonyms.dic","r",encoding="utf-8")
for line in fd.readlines():
    line=line.replace("\n","")
    splitted=line.split("\t")
    key=splitted[0]
    entryList=[]
    for i in range(1,line.count("\t")+1):
        entryList.append(splitted[i])
    synonymsDic[key]=entryList
fd.close()

print(ecDic)
print(synonymsDic)


keep=[]
f=open("11_口语表达语料.TXT","r",encoding="utf-8")
for line in f.readlines():
    en=line.split("\t")[0]
    cn=line.split("\t")[1]
    tokens = nltk.word_tokenize(en)
    tagged = nltk.pos_tag(tokens)
    for item in tagged:
        word=str(item[0])
        if item[1].startswith("JJ") or item[1].startswith("NN") or item[1].startswith("VB") or item[1].startswith("WP"):
            print("\n"+word+"是实词")
        else:
            continue #只有实词才进行匹配检测
        if word in ecDic:
            word=word
        elif word.lower() in ecDic:
            word=word.lower()
        elif lemmatize(item) in ecDic:
            word=lemmatize(item)
        else:
            print("词典中没有该条目")
            continue

        
        result=match(word,cn)
        print("结果"+str(result))
        if result==False:
            keep.append(line)
            break

print(keep)
            
