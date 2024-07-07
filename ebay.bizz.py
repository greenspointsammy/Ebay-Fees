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
        'Electronic' : 0.126,

    
    }
    product = input("Enter the product: ")
    sale_price = float(input("Enter the sale price: "))
    shipping_cost = float(input("Enter the shipping cost: "))
    # Assume eBay fees are as per the product
    eBay_fees = sale_price * products[product]
    if sale_price <= 10:
        eBay_fees += 0.30
    else:
        eBay_fees += 0.40
      
    eBay_promo = sale_price * 0.03
    us_tax = sale_price * 0.12
    # Add gas fee
    gas_fee = 1.5
    supplies = .5
    profit = sale_price - eBay_fees - shipping_cost - gas_fee - supplies - eBay_promo - us_tax
    return profit

print(f"My Profit: {calculate_profit()}")
