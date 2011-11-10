#Task 8.5 - Arnab Kumar Datta (arnabkd)
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
    winner = (3 + player - computer) % 3 
    print "%s(%d points) chose %s, %s(%d points) chose %s.\tWinner: %s"%(players[1], scores[1] ,inv_choices[player], players[2],scores[2] ,inv_choices[computer], players[winner])
    scores[winner] += 1
    
if __name__ == '__main__':
    main()


#Runtime example
#arnabkd@starrenburg ~/Desktop/uni/inf3331/inf3331/ukesoppgaver/uke8 $ python roshambo.py 
#Enter number of points required to win: 3
#Enter r for rock, p for paper or s for scissors : r
#Player(0 points) chose rock, Computer(0 points) chose rock.     Winner: Tie
#Enter r for rock, p for paper or s for scissors : r
#Player(0 points) chose rock, Computer(0 points) chose rock.     Winner: Tie
#Enter r for rock, p for paper or s for scissors : p
#Player(0 points) chose paper, Computer(0 points) chose scissors.        Winner: Computer
#Enter r for rock, p for paper or s for scissors : r
#Player(0 points) chose rock, Computer(1 points) chose paper.    Winner: Computer
#Enter r for rock, p for paper or s for scissors : r
#Player(0 points) chose rock, Computer(2 points) chose paper.    Winner: Computer
#Final score: Player 0    Computer 3
