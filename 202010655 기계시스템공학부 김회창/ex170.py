#!/usr/bin/env python
# coding: utf-8

# In[ ]:


result = 1  #초기값을 1로 설정
for i in range(1,11):
    # for문에서 range를 이용하여 1~10까지의 숫자의 범위를 설정해준다.
    result = result*i   
    # 1부터 오른쪽 i값에 가서 곱해진 후 왼쪽의 result로 값이 넘어간다.
    # 그다음 i값들이 result값과 곱해진후 왼쪽의 result값으로 가는걸 반복한다.
print(result)
#(result)값을 출력하라.

