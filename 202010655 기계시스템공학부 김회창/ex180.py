#!/usr/bin/env python
# coding: utf-8

# In[ ]:


low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []
#volatility라는 빈 리스트를 만든다.

for i in range(5):  #5번 빼주어야지 5개의 변동폭을 모두다 작성할 수 있기에
                   #range를 이용하여 for문이 5번 반복되도록 한다.
    
    변동폭 = high_prices[i]-low_prices[i]  
    #변동폭을 고가와 저가의 차이로 정의한다.
    volatility.append(변동폭) 
    #append는 추가시킬때 쓰는 것이기에
    #append를 이용하여 volatility 리스트에 변동폭을 추가해준다. 

