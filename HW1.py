#!/usr/bin/env python
# coding: utf-8
#---------------------------------------------------------------------------------------------------------------------------------

#Q1-1
x = 50
y = 100 
n = 30  #order數量
threshold = 50 #閾值

if n < threshold:
    print ("Your profit of the day:",x*n)
else:
    print("Your profit of the day:",n*x+(n-threshold)*y)

#---------------------------------------------------------------------------------------------------------------------------------

#Q1-2
x = 50
y = 100 
n = 70  #order數量
threshold = 50 #閾值

if n < threshold:
    print ("Your profit of the day:",x*n)
else:
    print("Your profit of the day:",threshold*x+(n-threshold)*y)
    
#---------------------------------------------------------------------------------------------------------------------------------

#Q2
class_name = str(input("class name: "))
class_grade = str(input("class grade: "))

Table = {"A+":"4.3", "A":"4.0", "A-":"3.7",
               "B+":"3.3", "B":"3.0", "B-":"2.7",
               "C+":"2.3", "C":"2.0", "C-":"1.7", "F":"0"}

print(class_name,"grade point :",Table[class_grade])

#---------------------------------------------------------------------------------------------------------------------------------

#Q3
import math

ID = str(input())
raw_data = float(input())
final_data = round(10 * math.sqrt(raw_data),2)
print("student ID:",ID)
print("final score:",'%.2f'% final_data)  # print('%.2f'% 變數)  -->  印出強制保留到小數點第二位之變數值 
                                          # print('{0:.2f}'.format(變數))  -->  同上效果
    
#---------------------------------------------------------------------------------------------------------------------------------

#Q4
import math
string = [int(i) for i in input("Please input either clockwise or counter clockwise. \ne.g. (0, 0), (0, 1), (2, 1), (2, 0)\ninput: 0 0 0 1 2 1 2 0\n").split()]
coord = [(string[0],string[1]),(string[2],string[3]),
              (string[4],string[5]),(string[6],string[7])]

len_list = []  #裝每邊距離長度
len_equal = False  #判斷每邊是否等長
diagonal = []  #裝兩對角線長度
diagonal_equal = False  #判斷兩對角線是否等長

for j in range(4): #先求每邊距離
    if j == 3:
        len_list.append(math.sqrt((coord[j][0]-coord[j-3][0])**2 + (coord[j][1]-coord[j-3][1])**2))
    else:
        len_list.append(math.sqrt((coord[j][0]-coord[j+1][0])**2 + (coord[j][1]-coord[j+1][1])**2))


if len_list[0] == len_list[1] == len_list[2] == len_list[3]:  #判斷每邊是否等長
    len_equal = True

for k in range(2):  #再求兩對角線距離
    diagonal.append(math.sqrt((coord[k][0]-coord[k+2][0])**2 + (coord[k][1]-coord[k+2][1])**2))

if diagonal[0] == diagonal[1]:  #判斷兩對角線是否等長
    diagonal_equal = True
    
if len_equal == diagonal_equal == True:
    print("rectangle")
    
if len_equal == True and diagonal_equal == False:
    print("diamond")
    
if len_equal == False and diagonal_equal == False:
    print("others")

# 題目測資
# 0 1 1 1 1 0 0 0
 # rectangle
# -2 0 0 -1 2 0 0 1
 # diamond
# -1 0 2 0 10 0 0 -1
 # others

#---------------------------------------------------------------------------------------------------------------------------------

#Q5
integers = [int(i) for i in input("Input multiple integers.  e.g. 12345: ")]
sort_integers = sorted(integers)
reverse_sort_integers = sorted(integers,reverse = True)

if integers == sort_integers and integers == reverse_sort_integers:
    print("intergers are asc and desc")

elif integers == sort_integers:
    print("asc")
elif integers == reverse_sort_integers:
    print("desc")
else:
    print("not sorted")

#---------------------------------------------------------------------------------------------------------------------------------

# end
