#!/usr/bin/env python
# coding: utf-8

# In[1]:



def message1():
    print("A")  #3번 반복하여 message1()로 다시 올라가서 A프린트 

def message2():
    print("B")

def message3(): #mssage 3() 로 인해 여기서 부터 3번 루프  i=0일때 message2()호출 하여 B프린트      
    for i in range (3) : # 1.  0,1,2 3번 돌아감 루프
        message2()   # 2. message2()로 가서 B프린트
        print("C") # 3. print C한다. 4. C프린트 그후 다시 올라가서 B프린트 그 후 다시 C프린트 그리고 다시 올라가서 B프린트 후 C 프린트   (3번 루프했다.)          )    
    message1()     # 5.   3번 반복했으니 message1() 으로 다시 올라감 그래서 A 출력

message3()   #답은 BC가 3번 반복되어 BCBCBC후 message1()로 A출력되었기에 BCBCBCA 이다.


# In[ ]:




