# Homework

# Enter the tables with comma(,) as seperator : 2,3,4
# 2 x 1 = 2      |3 x 1 = 3      |4 x 1 = 4      |
# 2 x 2 = 4      |3 x 2 = 6      |4 x 2 = 8      |
# 2 x 3 = 6      |3 x 3 = 9      |4 x 3 = 12     |
# 2 x 4 = 8      |3 x 4 = 12     |4 x 4 = 16     |
# 2 x 5 = 10     |3 x 5 = 15     |4 x 5 = 20     |
# 2 x 6 = 12     |3 x 6 = 18     |4 x 6 = 24     |
# 2 x 7 = 14     |3 x 7 = 21     |4 x 7 = 28     |
# 2 x 8 = 16     |3 x 8 = 24     |4 x 8 = 32     |
# 2 x 9 = 18     |3 x 9 = 27     |4 x 9 = 36     |
# 2 x 10 = 20    |3 x 10 = 30    |4 x 10 = 40    |

tables = input("Enter the tables with comma (,) as separator: ").split(',')

for i in range(1, 11):
    for table in tables:
        table = int(table)
        print(table, "x", i, "=", table * i, end="|")
    print()


# Sir's COde:


# Calculating the Average Temperature

# Problem: You have a list of hourly temperature readings (integers) for a day
# and need to calculate the average temperature without using sum() or len().
# temperatures = [22, 24, 25, 27, 26, 23, 21, 20]


temperatures = [22, 24, 25, 27, 26, 23, 21, 20]

total = 0
count = 0

for temp in temperatures:
    total = total + temp
    count = count + 1

average = total / count

print("Average Temperature:", average)


# Finding the Highest Score
# Problem: You have a list of student scores and need to
# determine the highest score achieved without using the max() method.
# scores = [85, 92, 78, 95, 88, 99, 75]

scores = [85, 92, 78, 95, 88, 99, 75]

highest = scores[0]

for score in scores:
    if score > highest:
        highest = score
print("Highest Score:", highest)


# Counting Positive and Negative Stock Movements
# Problem: You have a list of daily stock price changes (positive for increase, negative for decrease)
# and need to count how many days the stock price went up (positive change) and how many days
# it went down (negative change).
# daily_changes = [0.5, -0.2, 1.1, 0.0, -0.7, 0.3, -0.1]

# Sir's Code:
daily_changes = [0.5, -0.2, 1.1, 0.0, -0.7, 0.3, -0.1]
positive_change_count = 0
negative_change_count = 0
for change in daily_changes:
    if change > 0:
        positive_change_count += 1
    elif change < 0:
        negative_change_count += 1
else:
    continue
print(f'Total Positive count is {positive_change_count}')
print(f'Total Negative count is {negative_change_count}')


# inp_str = 'peter piper picked a peck of pickled peppers'
# output1:- 'sreppep delkcip fo kcep a dekcip repip retep'  # for with range, convcatenation
# output2:- 'retep repip dekcip a kcep fo delkcip sreppep'  # len, slicing(should not be used for reversing), concatenation
# output3:- 'peppers pickled of peck a picked piper peter'

inp_str = 'peter piper picked a peck of pickled peppers'
for ind in range(-1, (-len(input_str)-1),-1):
    out_str +=inp_str [ind]
    print(out_str)


 