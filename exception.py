try:
    age=int(input("enter your age :"))
    result = age=18
    print("resulst is",result)
except ZeroDivisionError:
    print("you hve a zerodivisionerror")
except ValueError:
    print("plese enter int value")
finally:
    print("tis is final value")