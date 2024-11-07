def calculate_profit():
    products = {
        'Game': 0.12,  # eBay fees for game
        'Toy': 0.18,  # eBay fees for toy
        'camera': 0.25,  # eBay fees for camera
        'Books' : 0.15, #Books ebay fees
        'Bullion' : 0.1325,
        'Clothes' : 0.15,
        'Jewerly' : 0.15,
        'Movie' : 0.156,
        'Electronic' : 0.13,
        'Books' : 0.1,

    
    }
    shipping = {
        '8oz' : 4.43,
        '1p' : 6.23,
        '3p' : 15,
        '5p' : 20,
    }
    product = input("Enter the product: ")
    sale_price = float(input("Enter the sale price: "))
    shipping_weight = (input("Enter the shipping weight: "))
    # Assume eBay fees are as per the product
    eBay_fees = sale_price * products[product]
    if sale_price <= 10:
        eBay_fees += 0.30
    else:
        eBay_fees += 0.40
    shipping_fee = shipping[shipping_weight]
    eBay_promo = sale_price * 0.01
    us_tax = sale_price * 0.0925
    
    # Add gas fee
    gas_fee = shipping[shipping_weight] * 0.2
    supplies = shipping[shipping_weight] * 0.07
    print = .077
    profit = sale_price - eBay_fees - shipping_fee - gas_fee - supplies - eBay_promo - us_tax - print
    return profit

print(f"My Profit: {calculate_profit()}")