# use recursion to implement a countdown counter

global x
x = int(input("Type the number you want to countdwon "))

def countdown(x):
    if x == 0:
        print("You're done!")
        return
    else:
        print(x, " ... the countdown stills running")
        countdown(x-1)

countdown(x)
