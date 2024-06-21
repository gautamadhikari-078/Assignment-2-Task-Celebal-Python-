from collections import Counter

def calculate_earnings(num_shoes, shoe_sizes, num_customers, customers):
    # Count the occurrences of each shoe size
    shoe_count = Counter(shoe_sizes)
    
    total_earnings = 0
    
    # Process each customer
    for size, price in customers:
        if shoe_count[size] > 0:
            total_earnings += price
            shoe_count[size] -= 1
    
    return total_earnings

if __name__ == '__main__':
    # Read input
    num_shoes = int(input().strip())
    shoe_sizes = list(map(int, input().strip().split()))
    num_customers = int(input().strip())
    
    customers = []
    for _ in range(num_customers):
        size, price = map(int, input().strip().split())
        customers.append((size, price))
    
    # Calculate and print the total earnings
    earnings = calculate_earnings(num_shoes, shoe_sizes, num_customers, customers)
    print(earnings)
