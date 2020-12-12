#!/usr/bin/env python
# coding: utf-8

# In[24]:


class Stock: #Stock이라는 객체 정의 
    def __init__(self, name, code, PER, PBR, profit): #각 종목명과 종목코드, PER, PBR, 배당수익률을 받는 인스턴스 메서드
        self.name = name 
        self.code = code
        self.PER = PER
        self.PBR = PBR
        self.profit = profit
         
#self 라는 객체 공간 안에 넘어온 이름과 같은 이름의 변수를 만들고 함수 바깥에서 넘어온 값을 대입.

종목 = [] #리스트 넣어 주기 위해 리스트를 생성

samsung = Stock("삼성전자", "005930", 15.79, 1.33, 2.83) #함수 호출하는 인스턴스
hyunda = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

종목.append(삼성) #append를 사용하여 앞의 빈리스트 속에 넣어준다.
종목.append(현대차)
종목.append(LG전자)

for i in events:       #각각의 객체를 i에 대입
    print(i.code, i.PER)       #i에.을 찍어 변수에 접근하고 출력하게 한다.


# In[ ]:





# In[ ]:





# In[ ]:




