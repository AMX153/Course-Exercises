n = int(input("Enter the n: "))

if 2 <= n <= 2000:
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = (n * 3) + 1
            
        print(int(n))
        
else:
    print("Pay attention!. 2 <= n <= 2000.")
    