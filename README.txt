HOW TO USE


To use, copy the code in a python file

run the file by giving it executable permission
or
python interpreter.py

this will run the debug mode

to run a .sus code


interpreter code.sus



HOW DOES THIS WORK??

CaSe INsEnSitiVe

To store data this uses a stack
most commands work by checking the peek value of the stack

(BTW there is no error handling you just have to use the correct syntax)

WEIRD STRING

String is treated as a single token
a string can only be defined as lower or upper case
by default the strings are upper case

string does not allow spaces to add spaces add escape sequence

example :
_LHELLO,__WORLD! ==> "hello, world!"
_UHELLO,__WORLD! ==> "HELLO, WORLD!"  

command list

1) PRINT <STRING>
PRINT stdouts the given string token next to it

example :
PRINT HELLO,__WORLD!    ==> HELLO, WORLD!

2) INPUT
INPUT stdins and adds it to the stack 
every element add this was is a string

3) PARSE
PARSE converts numeric values in the stack to numeric data types

4) CLEAR
CLEAR clears the stack

5) PUSH <VALUE>
PUSH pushes element in the stack

6) POP
POP pops element from the stack

7) PEEK
PEEK stdouts the peek element in the stack

8) ADD
ADD pushes the sum of all elements in the stack in the stack

9) ADDWITH <NUM>
ADDWITH pushes the sum of peek element and <NUM> in the stack

10) EVAL
EVAL evaluates the string at peek of the stack

11) IF ..COMMANDS.. FI
RUN COMMANDS if peek of the stack is not 0
COMMANDS must be written in single line

IF PRINT HELLO_N FI      RIGHT WAY

IF
PRINT HELLO_N		WRONG WAY
FI

12 LOOP ..COMMANDS.. POOL
RUN COMMANDS till the peek of stack in not 0
COMMANDS MUST BE WRITTEN IN SINGLE LINE AS IN IF...FI


13 COMPWITH <NUM>
pushes 1 to stack if peek of stack is greater than <NUM>
pushes -1 to stack if peek of stack is smaller than <NUM>
pushes 0 to stack if peek of stack is equal to <NUM>

14 END
ends the code might not work in loops and if statements

15 VAR <VARIABLE> <VALUE>
adds a variable with value 😀


EXAMPLE CODE ARE PROVIDED MAKE SURE TO CHECK THEM




THIS IS PROTOTYPE BTW
