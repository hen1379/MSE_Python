#!/usr/bin/env python
# coding: utf-8

# In[ ]:


if True :
# if문이 참이기때문에 바로 밑 if문이 실행 끝부분 else는 실행안됨.

    if False:     # if문은 거짓이므로 else로 넘어감
        print("1")
        print("2")
    else:
        print("3")
        
        # else값인 print("3")이 실행되므로 "3" 이 출력
        
else :  #아까 참이었기에 else값은 실행안되므로 무시
    print("4")  
print("5")  

# print("5")가 실행됨 "5"출력

#화면에 3,5가 출력됨

