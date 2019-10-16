print ("how many numbers should i add up?")
NumberCount = int(input())
CurrentNumber = 0
total = 0

while CurrentNumber < NumberCount:
    CurrentNumber+=1
    print("please enter number " + str(CurrentNumber) + " of " + str(NumberCount))
    NumberEntry = int(input())
    total += NumberEntry

print("the total is " + str(total))




