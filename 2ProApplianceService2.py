def greeting():
    print("Here are step by step instructions for disassembling an Acme Dryer.")

def main():
    print("Hello")
    greeting()
    menu()
    end()

def menu():
    print("Which step would you like to view today?")
    print("1. Unplugging the dryer.")
    print("2. Removing dryer screws.")
    print("3. Removing back panel.")
    print("4. Moving the dryer.")
    toDo = int(input());
    if (toDo == 1):
        unplug()
    elif (toDo == 2):
        screws()
    elif (toDo == 3):
        panel()
    else:
        move()

def unplug():
    print("Unplug the dryer and move it away form the wall.")

def screws():
    print("Remove the six screws from the back of the dryer.")

def panel():
    print("Remove the dryers back panel.")

def move():
    print("Pull the top of the dryer straight up.")
    
def end():
    print("Thanks for using our app!")

main()
