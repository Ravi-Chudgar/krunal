def calculate(input_list):
    if not isinstance(input_list, list):
        return False

    total = 0
    for item in input_list:
        if isinstance(item, str):
            try:
                number = int(item)
                total += number
            except ValueError:
                continue
        elif isinstance(item, int):
            total += item

    return total

def main():
    user_input = input("Enter a list of values separated by spaces: ")
    
    # Check if the input contains spaces (indicating a list)
    if ' ' in user_input:
        input_list = user_input.split()  # Split the input string into a list of items
        result = calculate(input_list)
        if result is not False:
            print("Sum of integers in the list:", result)
        else:
            print("FALSE.")
    else:
        print("FALSE.")

if __name__ == "__main__":
    main()
