while True:
    question = int(input("Please enter the question that you want to solve(1 or 2): "))

    while question < 1 or question > 2:
        question = int(input("Error! Please re-enter the question that you want to solve (1 or 2): "))

    if question == 1:
        exec(open("igrad_q1.py").read())
    else:
        exec(open("igrad_q2.py").read())

    choice = input("Press 'Y' to solve another question or any other keys to quit: ")
    choice = choice.upper()
    if choice == 'Y':
        True
    else:
        break
