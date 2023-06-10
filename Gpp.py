import math
import random
def render(token):
    message = token
    print(message)
        
    return message
def get(msg,type=str,):
    message = str(msg)
    if type == 'int':
        user = int(input(message))
           
           
    else:
        user = input(message)
           
           
    return user
def solve(tk1,tk2,tk3):
    a = int(tk1)
    c = str(tk2)
    b = int(tk3)
    if c == '+':
        res = a + b;
        print(res)
        return res
    elif c == '-':
        res = a - b;
        print(res)
        return res
    elif c == '*':
        res = a * b;
        print(res)
        return res
    elif c == '/':
        res = a/b;
        print(res)
        return res
    elif c == 'root':
        print(math.sqrt(a))
        return math.sqrt(a)
    elif c == 'round':
        print(round(a))
        return round(a)
    else:
        global error
        error = "Syntax Error"
        print(error)
        return error
def getInteger(thing):
    print(int(thing))
    return int(thing)
def intoByte(thing):
    try:
        print(bytes(thing,'utf-8'))
        return bytes(thing,'utf-8')
    except TypeError:
        print(bytes(thing))
        return bytes(thing)
def ifelse(condition,token1,token2):
    if condition:
        print(token1)
        return token1
    else:
        print(token2)
        return token2
def ifadv(cond1,cond2,tk1,tk2,tk3):
    if cond1:
        print(tk1)
        return tk1
    elif cond2:
        print(tk2)
        return tk2
    else:
        print(tk3)
        return tk3
vars = {}
funs = {}
def declare(name,value):
    global vars
    vars[name] = value
class rand:
    def int(From=0,to=1000000000):
        return random.randint(From,to)
def decFun(code,name):
    global funs
    funs[name] = exec(code)
def tokenize(tokens,into,run=True):
    if run:
        if into == 'string':
            return str(tokens)
        elif into == 'Number':
            return float(tokens)
        elif into == 'byte':
            return bytes(tokens)
        elif into == 'integer':
            return int(tokens)
        else:
            print(f'{into} not found')
            return 0;
    else:
        print(f"{into} Not found!")
def untokenize(token,running=True):
    if running:
        if token:
            try:
                return float(token)
            except ValueError:
                return "Could not convert"
        else:
            return "token is not string"
class program:
    def execute(code):
        return exec(code)
    def scan(code):
        if code == exec(code):
            return True
        else:
            return False
class games:
    def guessGame(userName,From,to,times):
        num = random.randint(From,to)
        for i in range(int(times)):
            user = int(input(f"Hey {userName} can you guess a number between\n{From}-{to}?"))
            if user == num:
                print("correct!")
            else:
                print("incorrect")
    def mathGame(user,From,to):
        n1 = random.randint(From,to)
        n2 = random.randint(From,to)
        try:
            plyr = int(input(f"Hey {user}, What is {n1}+{n2}: "))
            if plyr == n1 + n2:
                print("correct!")
            else:
                print("incorrect")
        
        except ValueError:
            print("not a number")
class apps:
        def numberGen():
            number = [random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)]
            print(number[0],end="")
            print(number[1],end="")
            print(number[2],end="")
            print(number[3],end="")
            print(number[4],end="")
            print(number[5],end="")
            print(number[6],end="")
            print(number[7],end="")
            print(number[8],end="")
            print(number[9],end="")
            
        