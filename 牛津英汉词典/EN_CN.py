#coding:utf-8

#实现英汉词典的规格化

#打开文档，注意encoding部分对于读取和写文件非常重要
fd=open("en2cn.txt","w",encoding="utf-8")
fd_re=open("牛津英汉词典.txt","r",encoding="utf-8")
for line in fd_re.readlines():
	newline=""
	#去除头尾空格以及用空格将词典分割为单词和词义的列表，但词义可能有由“，”分割开的不同词义存在一项内
	splitted=line.strip().split()
	newline+=splitted[0]
	#print (len(splitted))
	for i in range(1,len(splitted)):
		#对由“，”分割开的不同词义存在一项内 这一情况进一步进行分割
		deepSplitted=splitted[i].split("，")
		#词性标签如n.和adv.的去除
		#（确定.的位置即可，问题在于有的词义中出现了“...”，所以对于这种情况做区分）
		#没有出现“...”，从结尾找最后一个.即可，出现的话则截取“...”之前的部分逆序进行.位置确定
		#（不同词性同一词义的情况下会出现n.&adj.这种情况，需要将最后一个.之前的部分全部删除）
		if deepSplitted[0].find("...")!=-1:
			dot=deepSplitted[0][:deepSplitted[0].find("...")].rfind(".")
		else:
			dot=deepSplitted[0].rfind(".")
		newline+="\t"+deepSplitted[0][dot+1:]
		#print (len(deepSplitted))
		for j in range(1,len(deepSplitted)):
			newline+="\t"+deepSplitted[j]
			#print (newline)
	newline+="\n"
	#print ("\n")
	fd.write(newline)
fd.close()
fd_re.close()