# a year is a leap year if it is divisible by 4 unless it is a century no divisible
# by 400. write a function that takes a year as a parameter and returns true
# if the year is a leap year and false otherwise
# 2.32
# defining a function leapyear with year as the parameter
def leapyear(year):
    # initializing the condition
    if (year % 100 == 0):
        print(" this is century")
        # there can be if condition inside an if condition
        # that's fine
        if (year % 4 ==0 and year % 400 == 0):
            print("true")
        else:
            print("false")
    else:
        print(" this is not a century")
        if (year % 4 == 0):
            print("true")
        else:
            print("false")
# calling the function to check the execution
leapyear(3000)
