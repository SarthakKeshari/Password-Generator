import random

lowercase_alphabet = "abcdefghijklmnopqrstuvwxyz"
uppercase_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
special_charaters = "!@#$%^&*()_-=+{}[]:;/.,<>? "

all = lowercase_alphabet+uppercase_alphabet+digits+special_charaters

while(True):
    try:
        pswd_len = int(input("Enter length of password you want: "))
        password = "".join(random.sample(all, pswd_len))
        print(password)
        break
    except:
        print("Enter digits only")
