#!/usr/bin/env python
# coding: utf-8

# In[ ]:



#오름차순 정렬하는 방법에는 두가지의 방법이 있다.

#첫번째 방법
data = [2, 4, 3, 1, 5, 10, 9]

data.sort()                          
#sort()를 사용하여 data를 오름차순으로 정렬한다.

print(data)

#data를 출력한다.

# 두번째 방법

data = [2, 4, 3, 1, 5, 10, 9]

data2 = sorted(data)  

#data 에 대입된 리스트를 sorted 함수로 오름차순으로 정렬하고 그 결과를 새로운 변수 data2에 대입

print(data2)

#data2를 출력한다.                    

