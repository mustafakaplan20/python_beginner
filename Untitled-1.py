# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep

# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

    # enter some variables that be declared

my_name=input("What's your name?: ")

pw=input("Password please: ")

# there can be used input as well
my_time=2 

print(f"Hello {my_name.upper()}\n"*5,f"Your Password is {pw}\n",end=f"This Screen "
f"will be closed in {my_time} sec(s)\n")

# sleep for 2 seconds after printing output
sleep(my_time)

# now call function we defined above
clear()

# after cleaning it shows only name
print(my_name.upper())