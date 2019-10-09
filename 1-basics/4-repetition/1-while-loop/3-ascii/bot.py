print("how many bars shoud be charged")
ChargeNeeded = int(input())
ChargedBars =  0

while (ChargedBars < ChargeNeeded):
    ChargedBars+=1
    print("charging: " + " █ " *  ChargedBars) 

if (ChargedBars == ChargeNeeded):
    print("battery is fully charged")