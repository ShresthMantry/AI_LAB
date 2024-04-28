n = int(input("Enter capacity of jug 1"))
m = int(input("Enter capacity of jug 2"))

d = int(input("Enter amount of water to measure")

initialState = (0,0)
q = []
q.append(initialState)
while !q.empty():
        jug1,jug2 = q.pop()

        if jug1==d or jug2==d:
                print(path)
                break

        nextState1 = (jug1,m)
        nextState2 = (n,jug2)
        nextState3 = (jug1,min(jug2-n,m))
        nextState4 = (min(jug1-jug2,n),jug2)

        if nextState1 not in closeList:
                closeList.append(nextState1)

        if nextState1 not in closeList:
                closeList.append(nextState2)
        if nextState1 not in closeList:
                closeList.append(nextState3)
        if nextState1 not in closeList:
                closeList.append(nextState4)
