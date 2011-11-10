#Task 10.1 - Arnab Kumar Datta (arnabkd)

#Q:_What is the difference between a string and an integer/float?
#A: A string is a literal object, while integers and floats are integer values.


#Q: What makes a float different from an integer?
#A: Int has only integer values and typically take 4 bytes of memory. Floats
#   have a broader range of numbers, but less precisely (after 16 million
#   numbers or so)

#Q: Given a variable, x, what is the command to get python to print out the type
#   of x?
#A: print type(x)

#Q: What is a keyword?
#A: Words that are reserved by a programming language, and has a particular
#   meaning in the context of that language.

#Q: What is a statement? Give 2 examples.
#A: A statement is the smallest unit of instruction given in a programming
#   language. Ex: call statement, assign statement

#Q: What is an expression? Give 2 examples.
#A: An expression is the combination of at least 1 operator and 1 operand.
#   Ex : (1+2) , random.randint(1,5) + random.randint(0,6)

#Q: What is the difference between a statement and an expression?
#A: An expression always returns a value of some sort; this is not necessary
#   for a statement

#Q: The following statement produces no output when not run in the shell.
#   3.14 * 6 * 6
#   Modify it to produce output.
#A: print 3.14 * 6 * 6

#Q: What is an operator?
#A: A function (not a method) that combines one or more operands.

#Q: What problem arises in integer devision?
#    * I want to divide 1 by 3 and get a result like: 0.333333333333. What is
#      the exact command to do this?
#    * HINT: you must use floats! What do floats have that integers do not have?
#A: Integer division will have a lower precision when used for division. This is
#   due to integers not having decimal point precision, which floats have.

#Q: Integer division always rounds which way? (up or down)
#A: Down.

#Q: What is concatenation, and on what type of variables
#   (integers/floats/strings) does it operate on?
#A: Concatenation is adding a list of elements to the end of another list of
#   elements. In python, it means string concatenation (ex : 'hello' + ' world'
#   will yield 'hello world')

#Q: Why do we use comments? (what is their purpose)
#A: To make up for code that is not self-explanatory.

#Q: Enter the following code:
#      >>> 1 == 1
#      >>> "1" == "1"
#      >>> 1 == "1"
#   Why is the third line false, while the first 2 lines are true?
#A: type(1) and type("1") are not equal and the == operator returns
#   false for two objects with different types.
