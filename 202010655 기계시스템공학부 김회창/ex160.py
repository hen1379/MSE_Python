#!/usr/bin/env python
# coding: utf-8

# In[ ]:


리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
#for문 사용하여 리스트안의 원소 하나씩 i에 대입   
  split = i.split(".")
    #split으로 .을 기점으로 반으로 나누어 진다. 
  if (split[1] == "h") or (split[1] == "c"):
   
    print(i)
     # split으로 나누었는데 뒤에 있는것이 h나 c에 있는게 있다면 print(i)가 실행된다.
        #앞의 조건에 맞는 i를 출력한다.

