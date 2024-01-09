def gettime():
    import datetime
    return datetime.datetime.now()


def logbook():
    print('Welcome to Logbook')
    print('''
    1. Registered Food Details
    2. Registered Exercise Details
    ''')
    try:
        choice = int(input('Enter a choice: '))
        if choice == 1:
            user = input('Enter your name: ')
            content = input('Enter your Food: ')
            with open(f"{user}_food.txt",'a') as food:
                
                food.write(f"My name is - {user},{str([str(gettime())])},{content}\n")
                print('The data has been entered successfully.')
        
        elif choice == 2:
            user = input('Enter your name: ')
            content = input('Enter your exercise: ')
            with open(f"{user}_exercise.txt",'a') as food:
                food.write(f"My name is - {user},{str([str(gettime())])},{content}")
                print('The data has been entered successfully.')
        
        else:
            print('Invalid choice please enter 1 or 2')
            logbook()
    except ValueError:
        print('Please enter a valid integer choice.')
        logbook()
def retrive():
    print('Welcome to Retrive')
    print('''To show the record
        1. Show Food Details
        2. Show Exercise Details''')
    try:
        user_choice = int(input('Enter your choice: '))
        user = input('Enter your name: ')
            
        if user_choice == 1:
            with open(f"{user}_food.txt", 'r') as file:
                for line in file:
                    print(line, end="")
        elif user_choice == 2:
            with open(f"{user}_exercise.txt", 'r') as file:
                for line in file:
                    print(line, end="")
        else:
            print('Invalid choice. Please enter 1 or 2.')
            retrive()
    except ValueError:
        print('Please Enter a valid integer choice: ')
        retrive()


def main():
    print('''
    Welcome to the health management app
    -------------------------------------
        1. Register Log Book
        2. Retrive Log Data''')
    try:

        choice = int(input('Enter your choice : '))
        if choice == 1:
            print('Welcome to register log book')
            logbook()
        elif choice == 2:
            print('Welcome to Retrive Data')
            retrive()
        else:
            print('select 1 or 2')
            main()
    except ValueError:
        print('Please Enter a valid integer choice: ')
        retrive()

main()