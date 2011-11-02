import operator,random
messages = ['','Please ask your math teacher for help!', 'You need more practice.','Well done!']
levels = {'B' : 10 , 'I': 25 , 'A':100}
func = {'add': operator.add, 'mul' : operator.mul, 'div' : operator.div , 'sub' : operator.sub}
ops = {func['add'] : '+' , func['mul'] : '*', func['div'] : '/' , func['sub'] : '-'}

def f(op,x,y):
    return op(x,y)

def play(level, op = random.choice(func.values())):
    operand1 = random.randint(1,level);    operand2 = random.randint(1,level)
    ans = f(op,operand1, operand2)
    input = int(raw_input(('Enter your answer for %d %s %d : ')%(operand1, ops[op],operand2 )))
    return (1 if input == ans else 0)
    

def main():
    level = levels[raw_input("Choose difficulty : (B)eginner / (I)ntermediate / (A)dvanced: ")]
    rounds = int (raw_input("Enter how many rounds you would like to play: "))
    type = (raw_input("What type of quiz do you want (note : division is integer division) :\ndiv/mul/sub/add/mix : "))

    points = 0
    
    if type != "mix":
        for i in range (rounds) : points += play(level,func[type])
    else :
        for i in range (rounds) : points += play(level)

    
    print messages[x]
    if (raw_input("Type \'r\' and press enter to restart the quiz\n")) == 'r' :
        main()

if __name__ == "__main__":
    main()
