def average(array):
    # your code goes here

    distinct_heights = set(arr)  # Convert array to set to get distinct heights
    avg = sum(distinct_heights) / len(distinct_heights)  # Compute average
    return round(avg, 3)  # Round to 3 decimal places



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
