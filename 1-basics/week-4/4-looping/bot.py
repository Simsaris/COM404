def cross_bridge(distance):
    for count in range(distance):
        print("crossed step.")
    if distance > 5:
        print ("the bridge is collapsing")
    else:
        print()
        print("we must keep going")

cross_bridge(3)
cross_bridge(6)