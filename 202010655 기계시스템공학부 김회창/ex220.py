#!/usr/bin/env python
# coding: utf-8

# In[ ]:



def print_max(a, b, c) :
    max_val = 0   #초기값 설정
    if a > max_val :
        max_val = a  #a가 max_val가 됬음
    if b > max_val :
        max_val = b  #만약 b가 max_val 보다 크다면 b가 max_val가 됨 그러나 b가 max_val 보다 작다면 max_val는 그대로 바뀌지 않음    
    if c > max_val :
        max_val = c  #만약 c가 max_val 보다 크다면 c가 max_val가 됨 그러나 c가 max_val 보다 작다면 max_val는 그대로 바뀌지 않음
                     
    print(max_val)
    #(max_val)를 출력하라

