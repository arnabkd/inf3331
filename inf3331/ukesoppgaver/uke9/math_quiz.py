import operator,random
messages = {0:'Please ask your math teacher for help!', 1:'You need more practice.', 2:'Well done!'}
levels = {'B' : 10 , 'I': 25 , 'A':100}
func = {'add': operator.add, 'mul' : operator.mul, 'div' : operator.div , 'sub' : operator.sub}
ops = {func['add'] : '+' , func['mul'] : '*', func['div'] : '/' , func['sub'] : '-'}

def f(op,x,y):
    return op(x,y)

def play(level, op):
    operand1 = random.randint(1,level);    operand2 = random.randint(1,level)
    ans = f(op,operand1, operand2)
    input = int(raw_input(('Enter your answer for %d %s %d : ')%(operand1, ops[op],operand2 )))
    return (1 if input == ans else 0)
    

def main():
    level = levels[raw_input("Choose difficulty : (B)eginner / (I)ntermediate / (A)dvanced: ")]
    rounds = int (raw_input("Enter how many rounds you would like to play: "))
    type = (raw_input("What type of quiz do you want : div/mul/sub/add/mix"))

    points = 0
    
    if type != "mix":
        for i in range (rounds) :
            points += play(level,func[type])
    else :
        for i in range (rounds) :
            points += play(level, random.choice(func.keys()))

    print "You got %d out of %d possible!"%(points,rounds)
    

if __name__ == "__main__":
    main()
