def check_password_strength(password):
    uppercase =0
    lowercase = 0
    number = 0
    spcl_char = 0
    if len(password)<8:
        return False
    elif password.isalnum()==True:
        return False
    elif password.find(" ")>=0:
        return False
    else:
        for ch in password:
            if ch>= 'A' and ch<= 'Z':
                uppercase+=1
            elif ch>= 'a' and ch<='z':
                lowercase+=1
            elif ch>= '0' and ch<= '9':
                number+=1
            elif ch=='!' or ch=='@' or ch=='#' or ch=="$" or ch=='%':
                spcl_char+=1
        print(uppercase,lowercase,number,spcl_char)
        if uppercase>0 and lowercase>0 and number>0 and spcl_char>0:
            return True
    
password = input("""
Minimum length: The password should be at least 8 characters long.
Contains both uppercase and lowercase letters.
Contains at least one digit (0-9).
Contains at least one special character (e.g., !, @, #, $, %).
Enter the password:
""")

strength = check_password_strength(password)
if strength == True:
    print("Your passowrd is strong.")
else:
    print("Your password is weak. Please enter a strong password")