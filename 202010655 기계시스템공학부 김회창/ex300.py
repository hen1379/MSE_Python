#!/usr/bin/env python
# coding: utf-8

# In[ ]:


per = ["10.31", "", "8.00"]

for i in per:
# per의 원소를 i에 차례대로 대입.
    try:
        print(float(i))
        # per의 각 문자열 원소를 float(실수)로 변환하여 출력하라는 코드
    except:
        print(0)
        # 예외가 발생하면 0으로 출력하라는 코드
    else:
        print("clean data")
        # 예외 없이 문자열이 실수로 변환되었을 때 "clean data"를 출력하라는 코드
    finally:
        print("변환 완료")
        # 예외 발생 여부와 상관없이 "변환 완료"를 출력하라는 코드
        
#10.31= 10.31 clean data 변환완료 출력
#"  " = 0 변환완료               출력
#8.00 = 8.00 clean data 변환완료  출력

