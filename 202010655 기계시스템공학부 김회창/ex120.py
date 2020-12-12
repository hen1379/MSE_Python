#!/usr/bin/env python
# coding: utf-8

# In[ ]:


fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
과일 = input("좋아하는 과일은?")
if 과일 in fruit.values(): #과일이 딕셔너리 안의 values안에 있다면 참이므로 print("정답입니다") 실행되어 "정답입니다."출력
    print("정답입니다.")
else:
    print("오답입니다.") #과일이 딕셔너리 안의 values안에 없다면 print("오답입니다")가 실행되어 "오답입니다."출력
    
#예시의 한라봉은 딕셔너리의 values안에 없기에 print("오답입니다.")실행되어 
#오답입니다. 실행됨

