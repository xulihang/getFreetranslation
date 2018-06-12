# -*- coding:utf-8 -*-  
import pandas as pd
import numpy as np
import re

def transform():
    fp = open(u"G:/NLP/11_口语表达语料.TXT", "r", encoding="utf-8")
    temp = fp.readlines()
    fp.close()
    number = 0
    for item in temp:
        number += 1
        print(number)
        item_split = item.split("\t")
        english = item_split[0].strip()
        chinese = item_split[1].strip()
        regex = re.compile(u":|：")
        english_temp = regex.split(english)
        if len(english_temp)>1:
            english = ':'.join(english_temp[1:])
            english = english.strip()
        with open(u"G:/NLP/口语表达语料_v1.TXT", "a+") as output:
            output.write(english + "\t" + chinese + "\n")
            
        
      
if __name__ == '__main__':
    transform()