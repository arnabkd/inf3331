#Task 8.5 Rock paper scissors (arnabkd)
import random
players = ['Tie','Player','Computer']
scores = [0,0,0]
choices = {'r':0 , 'p':1 , 's':2}
inv_choices = {0:'rock', 1:'paper', 2:'scissors'}

def main():
    try:
        post = int(raw_input("Enter number of points required to win: "))
    except: 
        print "Points required to win must be given as an int";exit(-1)
    while (scores[1] < post and scores[2] < post):
        play()
    print "Final score: %s %d \t %s %d"%(players[1],scores[1], players[2] , scores[2])

def play():
    player = choices[raw_input("Enter r for rock, p for paper or s for scissors : ")]
    computer = random.randint(0,2)
    winner = (3 + player - computer) % 3 #for player = X, computer = Y, this gives 0 if it is a tie, 1 if player wins, and 2 if computer wins
    print "%s(%d points) chose %s, %s(%d points) chose %s.\tWinner: %s"%(players[1], scores[1] ,inv_choices[player], players[2],scores[2] ,inv_choices[computer], players[winner])
    scores[winner] += 1
    
if __name__ == '__main__':
    main()
