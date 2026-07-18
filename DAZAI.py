print ("=== ATM Cash Dispenser ===\n")

total_100 = total_50 = total_20 = total_10 = total_5
customers_served = 0
total_dispensed = 0

serving = True

while serving:

    name = input("Enter customer name: ")  
    amount = int(input(f"holle {name}! Enter withdrawal amount: "))        