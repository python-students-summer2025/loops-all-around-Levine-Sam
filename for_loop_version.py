def get_starting_number():
    """
    User input validation
    
    """
    while True:
        user_input = input("How many bottles of beer on the wall? ")
        if user_input.isdigit() and int(user_input) >= 1:
            return int(user_input)
        

def sing(num_bottles):
    """
    sing function
    
    """
    for current_bottle in range(num_bottles, 0, -1):
        if current_bottle == 1:
            bottle_form = "bottle"
        else:
            bottle_form = "bottles"

        
        next_bottle = current_bottle - 1

        if next_bottle == 1:
            next_bottle_form = "bottle"
        else:
            next_bottle_form = "bottles"

        print(f"{current_bottle} {bottle_form} of beer on the wall, {current_bottle} {bottle_form} of beer.")

        if next_bottle == 0:
            print("Take it down, pass it around, no more bottles of beer on the wall!")
        else:
            if current_bottle == 1:
                print(f"Take it down, pass it around, {next_bottle} {bottle_form} of beer on the wall.")
            else: 
                print(f"Take one down, pass it around, {next_bottle} {next_bottle_form} of beer on the wall.")

        print()
