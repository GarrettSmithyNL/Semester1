#This is a library that is for validation
#Garrett Smith
#Nov 9 2023

def validateInt(value,  min = None, max = None):
    try:
        number = int(value)
    except ValueError or TypeError:
        print("Value not an int.")
        return False
    else:
        if min != None and number < min:
            print("Value under min.")
            return False
        if max !=  None and number > max:
            print("Value over max.")
            return False
        else:
            return True     

    
def validatefloat(value,  min = None, max = None):
    try:
        number = float(value)
    except ValueError or TypeError:
        print("Value not a float.")
        return False 
    else:
        if min != None and number < min:
            print("Value under min.")
            return False 
        if max !=  None and number > max:
            print("Value over max.")
            return False
        
        return True
    
def validateString(value):
    if value == "":
        print("Value is empty.")
        return False
    else:
        return True

