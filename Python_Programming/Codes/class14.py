# 1. Positional parameters and arguments
# Position/order matters
# The number of parameters and arguments should match

# Define a fcuntion which takes this list (data) as input and gives me only Male and Female values after filtering rest of the values

# inp_data_lst = ['Male', 'Male', 'Female', 'Other', 'None', 'Male', None, 10, 'Female', 1, 0, 'Yes', 'No']
# filter_lst = ['Male', 'Female']

# # # output_lst = ['Male', 'Male', 'Female','Male''Female']


inp_data_lst = ['Male', 'Male', 'Female', 'Other', 'None', 'Male', None, 10, 'Female', 1, 0, 'Yes', 'No']
filter_lst = ['Male', 'Female']

def filter_list_func(inp_data_lst, inp_filter_lst):
    return [ele for ele in inp_data_lst if ele in inp_filter_lst]

print(filter_list_func(inp_data_lst, filter_lst))



# def generate_bill(*item_prices, gst_percent=18):
#   return a dictionary which will have item count, subtotal, gst amount, grand total

def generate_bill(*item_prices, gst_percent=18):
    subtotal = sum(item_prices)
    gst_amount = subtotal * gst_percent / 100
    grand_total = subtotal + gst_amount

    return {
        "item_count": len(item_prices),
        "subtotal": subtotal,
        "gst_amount": gst_amount,
        "grand_total": grand_total
    }


bill = generate_bill(100, 250, 150, 500)

print(bill)