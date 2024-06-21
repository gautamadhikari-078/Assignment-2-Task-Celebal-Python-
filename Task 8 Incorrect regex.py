import re

T = int(input())
for _ in range(T):
    try:
        pattern = input()
        re.compile(pattern)
        print("True")
    except re.error:
        print("False")
