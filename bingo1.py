import random
s=0
for j in range(1000):
    P=[[random.randint(1,80) for i in range(5)] for i in range(100)]
    win = False
    R=[]
    while win == False:
        r=random.randint(1,80)
        if r not in R:
            R.append(r)
            for player in P:
                if r in player:
                    player.remove(r)
                    if player == []:
                        win = True
                        break
    s +=len(R)
print(int(s/1000))
