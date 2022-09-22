import api
from api import User

api.users = {
    "u1": User("u1"),
    "u2": User("u2"),
    "u3": User("u3"),
    "u4": User("u4"),
}

if __name__ == "__main__":
    while True:
        # Get inputs
        line = input().strip() # Use strip to prevent leading & trailing spaces
        splitted = line.split(" ")
        command = splitted[0] # Get first element in splitted as command
        splitted = splitted[1:] # Remove first (by setting splitted to the remaining)

        # Execute commands
        if command == "SHOW":
            api.show(splitted)
        elif command == "EXPENSE":
            # Check
            if len(splitted) < 3:
                print("Invalid EXPENSE. Format: EXPENSE <payer> <balance> <number_of_payee> <payee1 payee2...> <method>")
                continue
            
            # Parse payer, balance, num_of_payee
            payer = splitted[0]
            balance = float(splitted[1])
            num_of_payee = int(splitted[2])
            splitted = splitted[3:] # Set splitted to the remaining
            
            # Check
            if num_of_payee <= 0:
                print("Number of payee should be at least 1")
                continue
            if len(splitted) < (num_of_payee + 1):
                print("Too few arguments")
                continue

            # Get payee
            payee = splitted[:num_of_payee]
            splitted = splitted[num_of_payee:] # Set splitted to the remaining

            # Get method
            method = splitted[0]
            splitted = splitted[1:]

            # Execute method
            if method == "EQUAL":
                api.expense_equal(payer, balance, payee)
            
            elif method == "EXACT":
                if len(splitted) != len(payee):
                    print("Number of EXACT arguments should equal to payee.")
                    continue
                # Convert exacts into float
                exacts = []
                for value in splitted:
                    exacts.append(float(value))
                api.expense_exact(payer, balance, payee, exacts)
            
            elif method == "PERCENT":
                if len(splitted) != len(payee):
                    print("Number of PERCENT arguments should equal to payee.")
                    continue
                # Convert exacts into float
                percents = []
                for value in splitted:
                    percents.append(float(value))
                api.expense_percent(payer, balance, payee, percents)

            else:
                print("Unknown method")

        else:
            print("Unknown command. Exit program")
            break