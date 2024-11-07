def calculate_profit():
    products = {
        'Game': 0.10,  # offerup fees for game
        'Toy': 0.10,  # eBay fees for toy
        'camera': 0.12,  # eBay fees for camera
        'Books' : 0.15, #Books ebay fees
        'Bullion' : 0.12, #gold and silver
        'Clothes' : 0.15,
        'Jewerly' : 0.15,
        'Movie' : 0.14,
        'Electronic' : 0.13,
        'Mag' : 0.14,
        'Instrument' : 0.13,

    
    }
    shipping = {
        '8oz' : 4.43,
        '1p' : 5.6,
        '3p' : 15,
        '5p' : 20,
        '20p' :35
    }
    product = input("Enter the product: ")
    sale_price = float(input("Enter the sale price: "))
    shipping_weight = (input("Enter the shipping weight: "))
    # Assume eBay fees are as per the product
    offerup_fees = sale_price * products[product]
    if sale_price <= 10:
        offerup_fees += 0.10
    else:
        offerup_fees += 0.1
    shipping_fee = shipping[shipping_weight]
    offerup_promo = sale_price * 0.01
    us_tax = sale_price * 0.0925
    
    # Add gas fee
    gas_fee = shipping[shipping_weight] * 0.2
    supplies = shipping[shipping_weight] * 0.07
    print = .01
    profit = sale_price - offerup_fees - shipping_fee - gas_fee - supplies - offerup_promo - us_tax - print
    return profit

print(f"My Profit: {calculate_profit()}")