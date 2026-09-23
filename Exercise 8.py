price = int(input("Enter the price: "))

if price > 50000:
    sale = 0.2
    final_price = (price) - ((price) * sale)
    print(int(final_price))
    
elif 20000 < price < 50000:
    sale = 0.1
    final_price = (price) - ((price) * sale)
    print(int(final_price))
    
elif price < 20000:
    final_price = price
    print(int(final_price))
    
