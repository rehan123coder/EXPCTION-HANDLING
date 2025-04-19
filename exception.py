try:
    num1,num2=eval(input("enter two numbers comma sperated by comma :"))
    result = num1/num2
    print("resulst is",result)
except ZeroDivisionError:
    print("you hve a zerodivisionerror")
except ValueError:
    print("plese enter int value")
finally:
    print("tis is final value")