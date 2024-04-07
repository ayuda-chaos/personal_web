user_input= (input("Enter Your Number"))
while user_input !="end":
    try:
        divisor=int(user_input)
        print(60//divisor)
    except ValueError:
        print("v")
    except ZeroDivisionError:
        print("z")
    user_input=input("enter your Number")
print("OK")