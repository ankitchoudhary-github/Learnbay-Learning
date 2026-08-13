# Exception Handling => Is the process of anticipating and responding to disruptions in a program in a controlled way.
# Unexpected termination of the program
# # Error Types
# 1. Compile Time Error - SyntaxError, IndentationError - Compiler
# 2. RunTime Error - NameError, ValueError, KeyError, TypeError etc
# 3. Logical Error


# Try Except Block
# try - Code which is going to raise the error
# except - code which should be executed since error occurs

def charge_customer(order_id, amount):
    try:
        response = payment_gateway.charge(order_id, amount)   # may time out
        return {"status": "success", "txn_id": response.txn_id}
    except Exception:
        # The server stays alive; this one order fails gracefully.
        return {"status": "failed", "message": "Payment could not be processed. Please retry."}


# try - code which is going to raise the error
# except - code whoch should be executed oince error occurs
# else - in else block we write the piece of code which we want to be executed if error does not occured
# finally - The code in finally block will be executed irrespective of the errors - cleanup code - closing the file, deleting the references etc

num1 = int(input('Enter first Number: '))
num2 = int(input('Enter second number: '))
try:
    print('Try block started!!!')
    res = num1/num2
    print('Try block Ended!!!')
except:
    print('except block started!!!')
    print('*******Divison by Zero is not possible*******')
    print('excpet block Ended!!!')
else:
    print('else block started!!!')
    print(f'Division result is {res}')
    print('else block Ended!!!')
finally:
    print('finally block started!!!')
    print(num1, num2)
    print('This block is used for cleanup work!!!')
    print('finally block Ended!!!')


def update_balance(user_id, amount):
    conn = db.connect()
    try:
        conn.execute("UPDATE accounts SET balance = balance + ? WHERE id = ?",
                     (amount, user_id))
    except db.IntegrityError:
        conn.rollback()
        print("Update rejected — constraint violation.")
    else:
        conn.commit()                       # only commit if no exception
        print("Balance updated successfully.")
    finally:
        conn.close()                        # ALWAYS release the connection


# 2. One try block may have multiple except Block
# 6. Child Exception should be followed by Parent exception
try:
    a = int(input('Enter 1st number: '))
    b = int(input('Enter 2nd number: '))
    res = a/b
except Exception as e3:
    print('Exception Except block')
    print(e3)
except ZeroDivisionError as e:
    print('ZeroDivisonError Except block')
    print('Division by 0 is not allowed')
    print(e)
except ValueError as e1:
    print('ValueError Except block')
    print('Invalid Input')
    print(e1)
except ArithmeticError as e2:
    print('ArithmeticError Except block')
    print(e2)
else:
    print('Else Block')
    print(res)
finally:
    print('Finally Block')
    print(a)
    try:
        print(b)
    except NameError as e4:
        print(e4)

# 1. Each try block should have at least one except block
# 2. One try block may have multiple except Block
# 3. One except block can not have multiple try block
# 4. The order of try and except is try -> except -> else -> finally, where else and finally blocks are Optional
# 5. In case nested try, we should have corresponding nested except block
# 6. Child Exception should be followed by Parent exception


# Define one user defined Exception with name "MyException"

# Define one function called "amount_withdraw(amt)"" - which takes an amount as an argument,
  # if amt is > 49999: raise MyException with message "Need pan for withdrawing this amount"
  # else:process the amount withdrawal

# Define one more funcion "pan_valid(pan_no)" -
  # Check the validity of pan - first 5 chracters are alphabets, next 4 numbers and last alphabet
    # If pan ios correct then process the amount withdrawal
  # else:
    # raise MyException with message wrong pan

# Write the code which calls amount_withdraw(amt - which should be given bu the user) -
  # if error is raised then you should handle it propery based on amount and pan card details.


class MyException (Exception):
    def __init__(self, msg):
        self.msg = msg


def amount_withdraw(amt):
    if amt > 49999:
        raise MyException('Need PAN for withdrawing this amount!!!')
    else:
        print('Procesing the amount withdrawal!!!')
        print('Please collect your cash...')


def pan_valid(pan_no):
    if pan_no[:5].isalpha() and pan_no[5:9].isdigit() and pan_no[-1].isalpha():
        print('Processing the amount Withdrawal!!!')
        print('Please collect your cash...')
    else:
        raise MyException('PAN no you have entered is wrong...')


amount = int(input('Enter an amount: '))
try:
    amount_withdraw(amount)
except MyException as e:
    print(e)
    pan = input('Enter your PAN No: ')
    try:
        pan_valid(pan)
    except MyException as e1:
        print(e1)
