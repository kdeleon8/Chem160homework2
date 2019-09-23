from random import choices
#
ntrials=1000
player1wins=0
for j in range(ntrials):
    ndice1=2
    ndice2=3
    dice1= choices(range(1,7), k=ndice1)
    if dice1[0] == dice1[1]:
        player1wins +=1

    dice2= choices(range(1,7), k=ndice2)
    dice2.sort(reverse=True)
    sum1=dice1[0]+dice1[1]
    sum2=dice2[0]+dice2[1]
    if sum1 >= sum2:
        player1wins +=1
        avg_rollsratio=player1wins/ntrials
print(avg_rollsratio)
