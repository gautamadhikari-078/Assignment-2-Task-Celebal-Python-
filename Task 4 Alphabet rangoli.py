def print_rangoli(size):
    import string
    alphabet = string.ascii_lowercase
    
    lines = []
    for i in range(size):
        # Create the left half of the line
        left_part = '-'.join(alphabet[size-1:i:-1] + alphabet[i:size])
        
        # Create full line with center
        full_line = left_part.center(4 * size - 3, '-')
        
        # Append to lines
        lines.append(full_line)
    
    # Print each line in reverse order and then the rest
    for line in reversed(lines):
        print(line)
    for line in lines[1:]:
        print(line)




if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
