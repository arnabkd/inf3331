import operator,random
levels = {'B' : 10 , 'I': 25 , 'A':100}
func = {'add': operator.add, 'mul' : operator.mul, 'sub' : operator.sub}
ops = {func['add'] : '+' , func['mul'] : '*', func['sub'] : '-'}
messages = ['Please ask your math teacher for help!','You need more practice.',\
                'Well done!']

def play(level,op):
    operand1 = random.randint(1,level);    operand2 = random.randint(1,level)
    ans = op(operand1, operand2)
    input = int(raw_input(('Enter your answer for %d %s %d : ')\
                              %(operand1, ops[op],operand2 )))
    return 1 if input == ans else 0

def feedback(points,rounds):
    ratio = float(points) / float(rounds)
    if (ratio > 2.0/3.0): #more than 2/3rd correct
        print messages[2]
    elif(ratio >= 1.0/3.0): #more than, or exactly 1/3rd correct
        print messages[1]
    else: #less than 1/3rd correct
        print messages[0]    

def main():
    level = levels[raw_input("Choose difficulty (B)eginner / (I)ntermediate"+\
                              " / (A)dvanced: ")]
    rounds = int (raw_input("Enter how many rounds you would like to play: "))
    type = (raw_input("What type of quiz do you want :\nmul/sub/add/mix : "))

    points = 0
    
    if 'mix' not in type:
        for i in range (rounds) : points += play(level,func[type])
    else :
        for i in range (rounds) : points += play(level, random.choice(func.values()))

    feedback(points,rounds)

    if (raw_input("Type \'r\' and press enter to restart the quiz\n")) == 'r' :
        main()

if __name__ == "__main__":
    main()
