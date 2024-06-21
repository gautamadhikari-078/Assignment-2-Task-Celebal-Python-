def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n = int(data[0])
    s = set(map(int, data[1].split()))
    m = int(data[2])
    
    commands = data[3:3+m]
    
    for command in commands:
        parts = command.split()
        if parts[0] == 'pop':
            if s:
                s.pop()
        elif parts[0] == 'remove':
            try:
                s.remove(int(parts[1]))
            except KeyError:
                pass
        elif parts[0] == 'discard':
            s.discard(int(parts[1]))
    
    print(sum(s))

if __name__ == "__main__":
    main()
