#!/usr/bin/env python
# coding: utf-8

# In[1]:



import random
#계좌 번호를 랜덤으로 만들기 위해 import random 사용.



class Account:
    # Account 클래스를 생성한다.
    
    account_count = 0
    #account_count의 초기값을 0으로 설정

    def __init__(self, name, balance): 
    #생성자에서 입력받는 값은 예금주의 이름과 잔고라는것을 정의해줌
        self.deposit_count = 0     
        
        self.deposit_log = []
        self.withdraw_log = [] 
        #입금이 될때마다, 출금이 될때마다 그때의 상황을 기록하기 위해
        #객체가 생성될때 deposit_log[] 와 self.withdraw_log 를 만들어놓는다.

        self.name = name
        self.balance = balance
        self.bank = "SC은행"
         # self가 가리키는 공간에 새로운 이름을 만들고 입력받은 값을 저장. 

        
        num1 = random.randint(0, 999) #3자릿수 랜덤 생성
        num2 = random.randint(0, 99)  #2자릿수 랜덤 생성
        num3 = random.randint(0, 999999)#6자릿수 랜덤 생성

        num1 = str(num1).zfill(3)  # 문자열(str)로 정숫값 변경하고 zfill을 이용하여 3자리로 만든다.
        num2 = str(num2).zfill(2)  # 문자열(str)로 정숫값 변경하고 zfill을 이용하여 2자리로 만든다.
        num3 = str(num3).zfill(6) # 문자열(str)로 정숫값 변경하고 zfill을 이용하여 6자리로 만든다.
        self.account_number = num1 + '-' + num2 + '-' + num3  #num1의 3자릿수 -num2의 2자릿수- num3의 6자릿수로 랜덤하게 만들어준다.
        account.account_count += 1 #계좌가 만들어질 때 마다 account_count 값이 증가하게 한다.


    @classmethod
    #객체에 접근할 필요가 없는 값들을 @classmethod를 사용해서 정해줌.
    def get_account_num(cls):
        print(cls.account_count)  
    def deposit(self, amount):
        if amount >= 1:
        #amount가 1이거나 더 크다면 입금을 한것이다.(입금하면)
            self.deposit_log.append(amount)   #예금할때 마다 예금액을 리스트로 저장
            self.balance += amount
            #self의 잔고에 amount값을 더해준값이 잔고

            self.deposit_count += 1
            #selfdml deposit_count값을 1증가시킨다.
            if self.deposit_count % 5 == 0:         # 5로 나누면 0이 될때(5의배수의 횟수가 될때)
                # 이자 지급
                self.balance = (self.balance * 1.01) #1%의 이자를 잔고에 추가


    def withdraw(self, amount): 
        if self.balance > amount:
            #amount가 잔고보다 작다면 돈을 출금할 수 있게 해준다.(만약 amount가 잔고보다 크다면 돈 출금할 수 없다.)
            self.withdraw_log.append(amount)  #출금할때마다 출금액을 리스트로 저장
            self.balance -= amount
            #잔고에서 amount를 뺀값이 잔고가 된다.

    def display_info(self): #disply_imfo를 추가한다.
        print("은행이름: ", self.bank) 
        #은행이름 출력
        print("예금주: ", self.name) 
        #예금주 출력
        print("계좌번호: ", self.account_number)
        #계좌번호 출력
        print("잔고: ", self.balance)
        #잔고 출력

    def withdraw_history(self):
        for amount in self.withdraw_log:    #출금액 구현
            print(amount)    #출금액 출력 만약 몇회차인지 앞에 인덱스를 붙여주고 싶다면 인덱스 만드는것도 가능  

    def deposit_history(self):         
        for amount in self.deposit_log:    #입금액 구현
            print(amount)   #입금액 출력


k = Account("Kim", 1000) #"Kim"은 1000원을 가지고 있다.
k.deposit(100)  
#100원입금
k.deposit(200) 
#200원입금
k.deposit(300)  
#300원입금
k.deposit_history()
#입금내역 출력

k.withdraw(100)
#100원 출금
k.withdraw(200)
#200원 출금
k.withdraw_history()
#출금내역 출력


# In[ ]:




