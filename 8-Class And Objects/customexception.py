class Error(Exception):
    pass

class dobException(Error):
    pass

year = int(input("Enter the dob"))
age = 2026 - year

try:
    if age<=30 and age >=20:
        print("The age is valid so you can apply for exam")
    else:
        raise dobException
except dobException:
    print("SOrry, your age should be greater than 20 and less than 30")