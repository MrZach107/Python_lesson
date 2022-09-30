#!/usr/bin/env python
# coding: utf-8

#---------------------------------------------------------------------------------------------------------------------------------

#EX_1
#Pick up the Maxi and sum 挑最大值並求總和

nums = [int(i) for i in input().split()]
lowwer = -100
upper = 100
out_of_range = False
if -1 <= nums[0] <= 10:
    del(nums[0])
    
    for j in nums:
        if upper < j or j < lowwer:
            out_of_range = True
            print("Value is out of range")
            break
            
    if out_of_range == False:
        sum_num = sum(nums)
        max_num = max(nums)
        print(max_num,sum_num)
else:
    print("n intergers is out of range")

#---------------------------------------------------------------------------------------------------------------------------------

#EX_2
#數字處理 (奇數 *=3,再 +=1 ) (偶數 //= 2)

num = int(input())
status = False
if num <= 1000000:
    while status == False:
        
        if num % 2 == 1:
            num *= 3 
            num += 1
            print(num, end = " ")
            
        if num % 2 == 0:
            num //= 2  # "//" 為整數除法
            print(num, end = " ")
        
        if num == 1:
            status = True

else:
    print("Please input a number lowwer than 1000000.")
    
#---------------------------------------------------------------------------------------------------------------------------------

#EX_3
#狙擊手遊戲 (避開danger_coordinates) (斜線、直線都不能站)

coords = [int(i) for i in input().split()]
x1,y1,x2,y2,x3,y3 = coords[0],coords[1],coords[2],coords[3],coords[4],coords[5]
is_safe = True

for i in range(6):
    for j in range(6):
        is_safe = True
        if (i == x1) or (i == x2) or (i == x3):
            is_safe = False
        elif (j == y1) or (j == y2) or (j == y3):
            is_safe = False
        elif ((abs(i-x1) == abs(j-y1)) or (abs(i-x2) == abs(j-y2)) or (abs(i-x3) == abs(j-y3))):
            is_safe = False
        if is_safe == True:
            print(i,j)


# 0 0 0 1 0 2

#---------------------------------------------------------------------------------------------------------------------------------

#EX_4
# 猜數字 幾A幾B

import random
target = random.sample(range(1, 10), 4)
A = 0
B = 0
print("請輸入四位連續數字 直到滿足 4 A 0 B 即為成功")
temp = False

while temp == False:
    guess = input()
    for i in range(4):
        if (int(guess[i]) == target[int(i)]):
            A+=1
        elif (int(guess[i]) in target):
            B+=1
    print(A,"A",B,"B")
    
    if A==4:
        temp = True
        print("Success!")
        
    A = 0
    B = 0
    
#---------------------------------------------------------------------------------------------------------------------------------

#EX_5
#回文字串 palindrome

string = str(input())
half_length = int(len(string)) // 2
is_palindrome = True
for i in range(half_length):
    if string[i] == string[-i-1]:
        continue
        
    elif string[i] != string[-i-1]:
        is_palindrome = False
        break

if is_palindrome == True:
    print("The entered string is palindrome")

elif is_palindrome == False:
    print("The entered string is not palindrome")

#---------------------------------------------------------------------------------------------------------------------------------

#EX_6
#1-0 knapsack 取與不取問題

print("輸入規則如下:\nline1: n ∈ {1,...,100} , B ∈ {1,...,10000}\nline2: Wi ∈ {1,...,100}\nline3: Vi ∈ {1,...,100}\nline4: Xi ∈ {1,0}\n")
line1 = [int(i) for i in input().split()]  # item,knapsack
line2 = [int(i) for i in input().split()]  # weight
line3 = [int(i) for i in input().split()]  # value
line4 = [int(i) for i in input().split()]  # take or not 

item,knapsack = line1[0],line1[1]
weight,value = 0,0

if (line1[0] > 100) or (line1[0] < 0) or (line1[1] > 10000) or (line1[1] < 0):
    print("Error: line1 out of index ( n ∈ {1,...,100} , B ∈ {1,...,10000} )")
    
for i in range(item):
    if (line2[i] > 100) or (line2[i] < 0):  # weight
        print("Error: line2 out of index ( Wi ∈ {1,...,100} )")
        break
    elif (line3[i] > 100) or (line3[i] < 0):  # value
        print("Error: line3 out of index ( Vi ∈ {1,...,100} )")
        break
    elif (line4[i] > 1) or (line4[i] < 0):  # 1: take 
                                            # 0: not take
        print("Error: line4 out of index ( Xi ∈ {1,0} )")
        break

for j in range(item):
    if line4[j] == 1:
        weight += int(line2[j])
        value += int(line3[j])

if weight > knapsack:
    print(0)
else:
    print(weight,value)
    
#測資
# 4 9
# 2 3 4 3
# 2 4 5 3
# 1 0 1 1
# output: 9 10

# 4 9
# 2 3 4 3
# 2 4 5 3
# 1 1 1 1
# output: 0

#---------------------------------------------------------------------------------------------------------------------------------

#EX_7
#The moving average method

print("輸入規則如下:\nline1: n ∈ {2,3,4,5,6}\nline2: Mi ∈ {10,...,100}\nline3: Xi ∈ {0,...,10000}\n")


sum_demand = 0
forecast = 0
lst = []


#input line1
n = int(input())
if (n == 2) or (n == 3) or (n == 4) or (n == 5) or (n == 6):
    pass
else:
    print("Error: n is out of index ( n ∈ {2,3,4,5,6} )")
    
    
#input line2
m = int(input())
if (m > 100) or (m < 10):
    print("Error: Mi is out of index ( Mi ∈ {10,...,100} )")

    
#input line3
line3 = [int(i) for i in input().split()]
for i in range(m):
    if (line3[i] > 10000) or (line3[i] < 0):  
        print("Error: line3 out of index ( Xi ∈ {0,...,10000} )")

for i in range (m-n+1):
    sum_demand = 0
    for j in range(n):
        sum_demand += int(line3[j+i])
        
    forecast = sum_demand // n
    lst.append(forecast)

#印出字串(用逗點隔開)
lst_str = str(lst)[1:-1]
print(lst_str.replace(" ",""))

#測資
# 3
# 10
# 14 23 26 17 17 12 24 19 10 18
# output: 21,22,20,15,17,18,17,15

#---------------------------------------------------------------------------------------------------------------------------------

# end
