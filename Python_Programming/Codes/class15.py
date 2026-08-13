# # email_id = 'abhishek.gupta@learnbay.co'
# # user_name = lambda email: email.split('@')[0]
# # print(user_name(email_id))


# my_lst = [
#     'abhishek@gmail.com',
#     'rahul@learnbay.co',
#     'saundarya@gmail.com',
#     'Nikhil@yahoo.com',
#     'krishna@hotmail.com',
#     'Aniket@learnbay.com',
#     'Neha@learnbay.in',
#     'Anshu@rediffmail.com'
# ]

# # Find the list of all usernames for all email ids
# usernames = list(map(
#     lambda email: email.split('@')[0],
#     my_lst
# ))

# print(usernames)


# # Find the list of email id where domain is learnbay and length of username is greater than 4
# result = list(filter(
#     lambda email: 'learnbay' in email.split('@')[1]
#                   and len(email.split('@')[0]) > 4,
#     my_lst
# ))

# print(result)

# # Find the list of all usernames where domain is learnbay and lenght of username is greater than 4
# result = list(
#     map(
#         lambda email: email.split('@')[0],    # Here 0 will be denoted towards username and 1 will be denoted towards domain name
#         filter(
#             lambda email: 'learnbay' in email.split('@')[1]  # Same as Ques 1 but the operatin will be performed in username only before the domain
#                           and len(email.split('@')[0]) > 4,
#             my_lst
#         )
#     )
# )
# print(result)





# Find out the product of the sum of each tuple in lst using reduce()

from functools import reduce

lst = [(1, 9), (0, 7), (8, 7), (6, 7), (4, 7), (2, 4), (5, 9), (9, 0)]
sums = map(lambda x: x[0] + x[1], lst)
result = reduce(lambda x, y: x * y, sums)
print(result)




# [1, [2, 3], [4, [5]]] -> find the sum of all elements in the nested list

