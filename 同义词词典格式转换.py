# -*- coding:utf-8 -*-  
#实现同义词词林的规格化


with open('C:\\Users\\lenovo\\Desktop\\哈工大社会计算与信息检索研究中心同义词词林扩展版.txt') as f:
    with open('convert.txt','a') as w:
        for line in f:
            
            data = line[8:-1].split()
            for item in data:
                tmp = data.copy()
                tmp.remove(item)
                tmp.insert(0,item)
                w.writelines('\t'.join(tmp)+'\n')