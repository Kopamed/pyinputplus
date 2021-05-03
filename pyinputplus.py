def inputMenu(options=[], prompt="Choose one of the following:"):
    if len(options) == 0:
        return
    while True:
        print(prompt)
        for opt in range(len(options)):
            print(f"[{opt}] {options[opt]}")

        response = input("> ")

        try:
            
            response = int(response)
            if response >= 0 and response <= (len(options)-1):
                return options[response]

            else:
                print("Please enter a number from the list")

        except:
            print("Enter a number please")




def inputFloat(prompt="Enter a number: "):
    while True:
        try:
            num = float(input(prompt))

            return num

        except:
            print("Please enter a number")


def inputInt(prompt="Enter a number: "):
    while True:
        try:
            num = int(input(prompt))

            return num

        except:
            print("Please enter a number")
