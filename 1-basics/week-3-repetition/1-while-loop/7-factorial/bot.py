print("please enter a number")
FactorialNum = int(input())
StartNum = FactorialNum
EndNum = FactorialNum-1

while EndNum < FactorialNum:
    StartNum = StartNum*EndNum
    FactorialNum-=1

print(StartNum)
    
