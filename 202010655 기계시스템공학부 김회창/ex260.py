#!/usr/bin/env python
# coding: utf-8

# In[8]:



class OMG : 
    def print() : #3. 함수 호출 하지만 실제로는 OMG.print(mystock)으로 호출됨 인자로 넘어가 버려서 오류가 생김. 그러므로 def print()안에 self를 적어줘야한다. 
        
        #print함수에는 인자값이 없는데 def print(myself) 라는 인자값을 넣어주면 Oh my god이 출력된다.
        
        print("Oh my god")
myStock = OMG() #1. 객체 생성 그러나 비어있음 생성자가 없고 초기화 한것이 아니기에
myStock.print()  # 2. mystock이라는 변수가 바인딩 그후 print하면 나와야하는데 객체가 비어있기에 클래스로 넘어감


# In[ ]:




