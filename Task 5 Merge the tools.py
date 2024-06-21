def merge_the_tools(string, k):
    n = len(string)
    segments = [string[i:i+k] for i in range(0, n, k)]
    
    for segment in segments:
        seen = set()
        result = []
        for char in segment:
            if char not in seen:
                seen.add(char)
                result.append(char)
        print(''.join(result))





if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
