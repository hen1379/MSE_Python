#!/usr/bin/env python
# coding: utf-8

# In[3]:



#for i in range(0,5,0.1):
    #print(i)    이렇게는  불가능하다. 왜냐하면 step(range에서 3번째 들어오는 수)은 정수값만 줄 수 있기 때문이다.
import numpy  #그러므로 numpy 모듈을 사용하여 arange로 한다. arange는 소수점 단위로도 증가 시킬 수 있다.  
for i in numpy.arange(0,5,0.1): #0부터 5까지 0.1씩 증가 시켜라 라는 뜻이다.
    print(i)
    #i를 출력해라


# In[ ]:




