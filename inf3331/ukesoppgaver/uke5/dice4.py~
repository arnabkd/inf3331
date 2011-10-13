#Arnab Kumar Datta  (arnabkd)
#Task 5.4 : Simulate hazard game and determine if you should play this game
import random,sys

def throw_dice():
    return random.randint(1,6)

def hazard_game(dice_count , threshold):
    sum = 0
    for x in range(dice_count):
        sum += throw_dice()
    return sum >= threshold

#Everytime you win, you earn 9 units of money. Everytime you lose, you lose 1 unit.
#You start with 1 unit of money
balance = 1 ; reps = 100
for i in range (reps):
    balance += 9 if hazard_game(4,9) else -1

if (balance >= 1):
    print "Yes you should play this game."
else :
    print "No, this game will make you lose money."

#Runtime example
#arnabkd@skjold ~/Desktop/uni/inf3331/inf3331/ukesoppgaver/uke5 $ python dice4.py 
#Yes you should play this game.
