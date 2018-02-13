import random
player1=[]
player2=[]
win = False
players=[player1,player2]
u=len(players)
L=list(range(1,81))
card=random.sample(L,5)

for u in range(2):
    for i in range(5):
        x=int(input('Give me a number.\n'))

        while x>80 or x<1:
                print('You should pick a number from 1 to 80.\n')
                while len(player1)<5:
                    x= int(input('Give me a number.\n'))
                while len(player2)<5:
                    x= int(input('Give me a number.\n'))
        else:
            player1.append(x)
            player2.append(x)
print(player1, player2)

for j in range(5):
    if player1[j] == card[j] :
        win = True
        print('Bingo! Player1, you win!')
    elif player2[j] == card[j]:
        win = True
        print('Bingo! Player2, you win!')
