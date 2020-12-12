#!/usr/bin/env python
# coding: utf-8

# In[ ]:


date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

close_table = dict(zip(date, close_price))

#zip 함수를 사용해 리스트 data와 close_price를 쌍쌍으로 묶어준다.
#dict 함수를 이용해 zip(data, close_price)의 결과를 딕셔너리로 만들어준다. 
#앞에서 만든 딕셔너리를 close_table로 대입

print(close_table)

#close_table을 출력

