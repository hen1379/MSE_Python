#!/usr/bin/env python
# coding: utf-8

# In[1]:


class 부모:  
#부모 클래스 생성
  def __init__(self):
    #__init__을 이용하여 객체를 생성할때마다 자동으로 호출될 함수 입력
    print("부모생성")
    #부모생성 출력

class 자식(부모):  
#자식 클래스 생성
  def __init__(self):
    #__init__을 이용하여 객체를 생성할때마다 자동으로 호출될 함수 입력
    print("자식생성")
    # "자식 생성" 출력
    super().__init__()
    #super로 부모 클래스에 접근

나 = 자식()
#자식 클래스의 객체 생성
#자식 객체가 생성됬기 떄문에 "자식생성" 출력 후 부모 클래스가 호출되어 "부모생성"이 출력된다.


# In[ ]:




