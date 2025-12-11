# Exceptions = Errors that intrerupt the flow of a program
# 1. try, 2. except, 3. else, 4. finally

try:
    number = int(input("Type a number:" ))
    1/number
except: 
    print("you cannot devide a nr by 0")
except:
    print("You need to type in a number")
else: 
    print("There were no errors")
finally:
    print("This is the end")
