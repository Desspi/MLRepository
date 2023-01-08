def isEven(num:int) -> bool:
    if (num % 2 == 0):
        return True;
    else:
        return False;
    
check = isEven(11)
    
if (check == True):
    print("Even")
else:
    print("Odd")