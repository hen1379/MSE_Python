#!/usr/bin/env python
# coding: utf-8

# In[1]:



def my_print (a, b) :
#my_print를 정의
    print("왼쪽:", a)       #왼쪽:a값을 출력해라
    print("오른쪽:", b)     #오른쪽:b값을 출력해라
#my_print(200,100) 으로 해도 된다. 
#그러나 my_print(b=100, a=200) 처럼 순서를 꼭 b부터 하려면 a와 b를 명시적으로 적어준다.
my_print(b=100, a=200)     


# In[ ]:




