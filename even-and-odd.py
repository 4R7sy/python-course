from colorama import Fore
number = int(input("Write a random number: "))
result = number % 2
if result == 0:
    print(Fore.BLUE + "Your number is EVEN")
else:
    print(Fore.GREEN + "Your number is ODD")