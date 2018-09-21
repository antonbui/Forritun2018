# Here is the definition of safe_input. It should contain this exception:
def safe_input(prompt, type):
    while True:
        try:
            myinput = type(input(prompt))
            return myinput
        except ValueError:
            if type == int:
                a_type = int
            elif type == float:
                a_type = float
            elif type == str:
                a_type = str
            print("Error: please enter a value of ", a_type)
                
# Do not change the lines below
print(safe_input('Please enter an integer: ', int))
print(safe_input('Please enter a float: ', float))
print(safe_input('Please enter a string: ', str))

