class console:
    def getandrender(n,n2):
        print(input(n))
        return 0
    def tokenize(thing,untokenize=False):
        if untokenize :
            return float(thing)
        else:
            return str(thing)
    def solveandget(t1,op,t2):
        if op == '+':
            print(t1+t2)
            print(f"problem was {t1} + {t2}")
            return 0
        elif op == '-':
            print(t1-t2)
            print(f"problem was {t1} - {t2}")
            return 0
        elif op == '*':
            print(t1*t2)
            print(f"problem was {t1} * {t2}")
            return 0
        elif op == '/':
            print(t1/t2)
            print(f"problem was {t1} / {t2}")
            return 0
        else:
            print("error")