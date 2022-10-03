#!/usr/bin/env python
# coding: utf-8

# In[12]:


#EX_1
#Lottery winning numbers (隨機生成七數字) (前六個數字小於38且不為0) (第七位數小於8且不為0)


import random
total = []
lst = sorted(random.sample(range(1,39),6)) # random.sample()函數不會有重複取的問題
num = random.sample(range(1,9),1)
total = lst + num
for i in total:
    print(i,end = " ")


# In[207]:


#EX_2
#Easy recursive add (利用遞迴函式回傳由low加到high的數值) (不能使用sum()函數)

def recursive_add(low, high): #[法一] (由小加到大)
    if high > low:
        return low + recursive_add(low+1,high)

    else:
        return low

def recursive_add2(low, high): #[法二] (由大加到小)
    if low == high:
        return low
    else:
        return high + recursive_add2(low, high-1)

print(recursive_add(1,200)) #[法一]
print(recursive_add2(1,200)) #[法二]


# In[205]:


#EX_3
#Greatest Common Divisor (GCD) (求兩數最大公因數)

def  GCD(a,b):
    low = min(a,b)
    high = max(a,b)
    
    if low == 0:
        return high
    
    elif low == 1:
        return 1
    
    else:
        return GCD(low,high%low)

    
a = int(input(""))
b = int(input(""))


if a <= 0 or b <= 0:
    print("Not Positive")
else:
    print(GCD(a,b))


# In[199]:


#EX_4-1
#Greatest Common Divisor (GCD) (隨機四數找公因數)

import random
lst = random.sample(range(1000),4) 


def GCD(a,b):
    low = min(a,b)
    high = max(a,b)
    
    if low == 0:
        return b
    elif low == 1:
        return 1
    else:
        return GCD(high%low,low)

    
def GCD_4(i,j,k,l):
    return GCD(GCD(i,j),GCD(k,l))


print("四變數 (",end = " ")
print(lst[0],lst[1],lst[2],lst[3],sep = ", ",end = " ")
print(") 的公因數為 :",GCD_4(lst[0],lst[1],lst[2],lst[3]))


# In[200]:


#EX_4-2
#變形 (共花幾次找到公因數為2)

import random
temp = True
count = 0


def GCD(a,b):
    low = min(a,b)
    high = max(a,b)
    
    if low == 0:
        return b
    elif low == 1:
        return 1
    else:
        return GCD(high%low,low)

    
def GCD_4(i,j,k,l):
    return GCD(GCD(i,j),GCD(k,l))


while temp == True:
    lst = random.sample(range(1000),4)
    count += 1
    
    if GCD4(lst[0],lst[1],lst[2],lst[3]) == 2:
        print("你嘗試了:",count,"次 後得到公因數為 2 !")
        temp = False

