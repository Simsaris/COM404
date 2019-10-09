print("how many live wires should i avoid?")
LiveWireInput = int(input())
LiveWireAvoided = 0

while (LiveWireAvoided < LiveWireInput):
    LiveWireAvoided +=1
    print("Avoiding..." )
    print("Done! " +str(LiveWireAvoided) + " wire(s) have been avoided!")
