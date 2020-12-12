#!/usr/bin/env python
# coding: utf-8

# In[ ]:


ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],  #100-100=0
        [200, 210, 180, 190], #200-190=10       0+10-10=0
        [300, 310, 300, 310]] #300-310=-10
profit = 0  

#초기값0으로 설정

for i in ohlc[1:]:                    

    # for 문을 사용하여 2번째 행부터 4번째 행까지를 차례대로 i 에 대입
    
    profit += (i[3] - i[0])  
    
    # "close"에서 "open"을 빼야 시가("open")에 매수해서 종가("close")에 
    # 매도하는 것이기에 빼주고 그 값을 왼쪽 profit 변수에 대입한다.
    #i가 4번째 행을 담을때까지 연산을 반복한다.

print(profit)

# profit을 출력한다.

