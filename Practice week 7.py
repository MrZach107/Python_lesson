#!/usr/bin/env python
# coding: utf-8

#---------------------------------------------------------------------------------------------------------------------------------

#EX_1 
#給定一個list，並用random.seed()輸出20個隨機數(0~100)

import random

Day = 10
random.seed(Day)
lst=[]

for i in range(20):
    x = random.randint(1,100)
    if x not in lst:
        lst.append(x)

temp = str(lst)[1:-1]
lst_str = temp.replace(", ","\n")
print(lst_str)

#---------------------------------------------------------------------------------------------------------------------------------

#EX_2 
#將list內的資料放到文件中


doc = open("doc.txt","wt",encoding ="utf-8")
doc.writelines(lst_str)
doc.close()

#---------------------------------------------------------------------------------------------------------------------------------

#EX_3
#計算list內的平均數、標準差

import cmath

def mean(lst): # Mean
    m = sum(lst)/len(lst)
    return m

def div(lst,m): # Standard deviation
    variance = sum([((x - m) **2) for x in lst]) / len(lst)
    res = variance ** 0.5
    return res


M = mean(lst)
D = div(lst,M)
print(D)


doc = open("doc.txt","wt",encoding = "utf-8")
doc.writelines("\nmean: " + str(M))
doc.writelines("\ndiv:" + str(D))
doc.close()

#---------------------------------------------------------------------------------------------------------------------------------

#EX_4 
#計算list內的平均數、標準差

def compare(std,Day):

    if std > Day:
        return(True)
    else:
        return(False)

#---------------------------------------------------------------------------------------------------------------------------------

#合併EX_1 ~ EX_5

#EX_1 
#給定一個list，並用random.seed()輸出20個隨機數(0~100)

import random

Day = 10
random.seed(Day)
lst=[]

for i in range(20):
    x = random.randint(1,100)
    if x not in lst:
        lst.append(x)

temp = str(lst)[1:-1]
lst_str = temp.replace(", ","\n")


#EX_3 
#計算list內的平均數、標準差

import cmath

def mean(lst): # Mean
    m = sum(lst)/len(lst)
    return m

def div(lst,m): # Standard deviation
    variance = sum([((x - m) **2) for x in lst]) / len(lst)
    res = variance ** 0.5
    return res

M = mean(lst)
D = div(lst,M)

#EX_4 
#計算list內的平均數、標準差

def compare(std,Day):

    if std > Day:
        return(True)
    else:
        return(False)

#EX_2、EX_5 
#將所有資料放到文件中

doc = open("doc.txt","wt",encoding = "utf-8")
doc.writelines(lst_str)
doc.writelines("\n\nmean: " + str(M))
doc.writelines("\nstd: " + str(D))
if compare(D,Day) == True:
    doc.writelines("\nStandard deviation is bigger than Day.")
elif compare(D,Day) == False:
    doc.writelines("\nStandard deviation is less than Day.")

doc.close()

