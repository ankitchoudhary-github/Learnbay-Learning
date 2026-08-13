# price_lst = ['1.9k', '0.9k', '1999', '1999.00', '2.5k', '4k', '2999/-']
# out_price_lst = [1900, 999, 1999, 1999, 2500, 4000, 2999]

def convert_price(price):
    price = price.lower().replace("/-", "")

    if price.endswith("k"):
        return int(float(price[:-1]) * 1000)

    return int(float(price))


price_lst = ['1.9k', '0.9k', '1999', '1999.00', '2.5k', '4k', '2999', '2999/-']

out_price_lst = [convert_price(price) for price in price_lst]

print("price_lst =", price_lst)
print("out_price_lst =", out_price_lst)


# category = ['Fashion', 'fashion', "Men's Fashion", "Women's Fashion", 'Kitchen Accessories', 'Home & Kitchen', 'Apparel'
#             "Kid's Fashion", "kid's fashion", 'Electronics', "HOME & KITCHEN", "ELECTRONICS", "ELEC", "GADGETS", 'gadgets']
# # Fashion
# # Electronics
# # Home & Kitchen

# out_category = ['Fashion', 'Fashion', 'Fashion', 'Fashion', 'Home & Kitchen', 'Home & Kitchen', 'Fashion'...]

