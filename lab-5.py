
while True:
    try:
        number = int(input("Enter a number :"))
        assert number == 5
        print("the number is equal to 5 exit the loop")
        break
    except AssertionError:
        print("Enter another number")
    except:
        print("please enter a number")


