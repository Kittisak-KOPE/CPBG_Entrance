import datetime

print('Enter "x" for get current time : ', end="")
x = input()

if(x == 'x'):
    currentDate = datetime.datetime.now()
    print(currentDate.strftime("%Y-%m-%d %H:%M:%S"))
else:
    print("Please enter correct information.")