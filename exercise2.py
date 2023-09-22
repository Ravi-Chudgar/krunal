def is_colorful_number(number):
    # Convert the number to a list of digits
    digits = [int(digit) for digit in str(number)]
    
    # Create a set to store the products
    products = set()
    
    # Check all consecutive subsets of digits
    for i in range(len(digits)):
        product = 1
        for j in range(i, len(digits)):
            product *= digits[j]
            if product in products:
                return False
            products.add(product)
    
    return True

# Test the function
if __name__ == "__main__":
    number = int(input("Enter a positive integer: "))
    if is_colorful_number(number):
        print(f"{number} TRUE.")
    else:
        print(f"{number} FALSE.")
