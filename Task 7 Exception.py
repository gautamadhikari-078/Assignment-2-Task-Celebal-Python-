
from re import compile
T = int(input())
for _ in range(T):
    try:
        r = compile(input())
        print(True)
    except:
        print(False)
