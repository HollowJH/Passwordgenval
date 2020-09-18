import random
import string
special = [
	    "@", "#", "$", "&", "/", "^", "*", "¿", "¡", "!", "-", "'", '"', ":", ";", ",", "?", "+", "×", "÷", "=", "%", "_", "€", "£", "£", "(", ")"]


def length(l=0):
    l=int(input())
    if l>4:
        return l
    else: 
        print("Password not long enough, try again")
        return length()

def create_pw(x):
	global pw
	global special
	pw = []
	al = list(string.ascii_lowercase) + list(string.ascii_uppercase)
	num = random.randint(1, x - 2)
	a = random.randint(1, x - num)
	pw += [str(random.randint(1, 9)) for i in range(num)]
	pw += [random.choice(al) for i in range(a)]
	pw += [random.choice(special) for i in range(x - len(pw))]
	random.shuffle(pw)
	pw="".join(pw)
	return pw if validate(pw) else create_pw(x)


def invalid():
    print("Invalid input")
    print("Exiting...")


def validate(x):
    global special
    if any([1 if i in special else 0 for i in x]) and any([i.isalpha() for i in x]) and any([i.isdigit() for i in x]):
        return True
    else:
        return False


print("Welcome to the password creator/validator")
print("\n")
print("Just input how long you want your password to be and we'll have it in no time")
print("Or, if you wish, input your password and we'll validate if it's strong enough")
print("\n")
print("The guidelines for it to be strong are:")
print("It has at least one number")
print("It has at least one special character")
print("It has at least one letter")
print("\n")
print("Having said that, Let's start")

while True:
    print("Write pass if you wish a randomly generated password")
    print("Write val if you wish to validate a password")
    print("Write end to exit the program")
    ip=input().lower()
    if ip=="pass":
        print("How long do you want your password to be?")
        try:
            length=length(length)
        except:
            invalid()
            break
        print("Your password is:",create_pw(length))
        print("\n")
    elif ip=="val":
        print("Write password to validate")
        print("The password is strong") if validate(input()) else print("The password is weak")
        print("\n")
    elif ip=="end":
        print("Goodbye!")
        break
    else:
        invalid()
        break